#!/usr/bin/env python3
"""Gmail MCP plan-only/dry-run entrypoint.

This entrypoint is intentionally non-destructive by default.
It validates policy artifacts and can run offline matcher simulations.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import os
import re
import sys
import hashlib
import math
from collections import defaultdict, Counter
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime, timezone, timedelta
from pathlib import Path
import secrets
import threading
import webbrowser
from functools import cmp_to_key
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlparse, quote
from urllib.request import Request, urlopen
from typing import Any, Dict, Iterable, List, Optional


ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"
REPO_ROOT = ROOT
GMAIL_API_BASE = "https://gmail.googleapis.com/gmail/v1/users/me"
PHASE7B_APPROVAL_TEXT = (
    "Phase 7-b 실제 mutate 파일럿(최대 10건)을 승인합니다. 이상 징후 발생 시 즉시 중단하고 롤백 절차를 수행합니다."
)


def _read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _collect_required_env(vars_: List[str]) -> Dict[str, Any]:
    missing = [name for name in vars_ if os.getenv(name) is None]
    status = "ok" if not missing else "warn"
    return {
        "status": status,
        "missing": missing,
        "env": {name: bool(os.getenv(name)) for name in vars_},
    }


def _read_client_secret(path: Path) -> Dict[str, str]:
    data = _read_json(path)
    app_data = data.get("installed") or data.get("web") or {}
    if not isinstance(app_data, dict):
        raise ValueError("client_secret.json must contain installed/web section")

    client_id = app_data.get("client_id")
    client_secret = app_data.get("client_secret")
    redirect_uris = app_data.get("redirect_uris", [])
    if not isinstance(redirect_uris, list) or not redirect_uris:
        redirect_uris = ["http://127.0.0.1:8765/"]

    if not client_id or not client_secret:
        raise ValueError("client_secret.json missing client_id/client_secret")

    return {
        "client_id": str(client_id),
        "client_secret": str(client_secret),
        "redirect_uris": [str(u) for u in redirect_uris if isinstance(u, str)],
    }


def _pick_redirect_uri(raw_redirect_uris: List[str]) -> str:
    for uri in raw_redirect_uris:
        parsed = urlparse(uri)
        if parsed.scheme == "http" and parsed.hostname in {"localhost", "127.0.0.1"}:
            if not parsed.path or parsed.path == "/":
                return uri
            return uri
    # OAuth desktop clients usually allow http://localhost without strict port.
    return "http://127.0.0.1:8765/"


def _start_local_oauth_server(
    expected_state: str,
    redirect_uri: str,
    timeout_seconds: int = 300,
) -> Dict[str, Optional[str]]:
    result: Dict[str, Optional[str]] = {"code": None, "error": None}
    parsed = urlparse(redirect_uri)
    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or 8765
    event = threading.Event()

    class CallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            code = (query.get("code", [None])[0] or "").strip()
            state = (query.get("state", [None])[0] or "").strip()
            error = (query.get("error", [None])[0] or "").strip()

            if state != expected_state:
                self._respond("state mismatch")
                result["error"] = "state_mismatch"
                event.set()
                return

            if error:
                self._respond(f"OAuth error: {error}")
                result["error"] = error
                event.set()
                return

            if not code:
                self._respond("Missing code")
                result["error"] = "missing_code"
                event.set()
                return

            result["code"] = code
            self._respond("Authentication completed. You may close this window.")
            event.set()

        def _respond(self, message: str):
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(message.encode("utf-8"))

        def log_message(self, fmt, *args):
            return

    try:
        server = HTTPServer((host, port), CallbackHandler)
    except OSError as exc:
        raise RuntimeError(f"failed to bind callback listener at {host}:{port}: {exc}") from exc

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    event.wait(timeout_seconds)
    server.shutdown()
    thread.join(timeout=2)
    server.server_close()
    if result["error"] is None and result["code"] is None:
        result["error"] = "timeout"
    return result


def _exchange_auth_code_for_tokens(
    code: str,
    client_id: str,
    client_secret: str,
    redirect_uri: str,
) -> Dict[str, Any]:
    payload = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }
    request = Request(
        "https://oauth2.googleapis.com/token",
        data=urlencode(payload).encode("utf-8"),
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urlopen(request, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        raise ValueError(f"token exchange failed: HTTP {exc.code}") from exc
    except URLError as exc:
        raise ValueError(f"token exchange failed: {exc}") from exc


def _gmail_me_profile(access_token: str) -> Dict[str, Any]:
    req = Request(
        "https://gmail.googleapis.com/gmail/v1/users/me/profile",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        raise ValueError(f"gmail profile request failed: HTTP {exc.code}") from exc
    except URLError as exc:
        raise ValueError(f"gmail profile request failed: {exc}") from exc


def _save_token_files(token_file: Path, token_cache: Path, tokens: Dict[str, Any]) -> None:
    token_file.parent.mkdir(parents=True, exist_ok=True)
    token_cache.parent.mkdir(parents=True, exist_ok=True)

    artifact = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "provider": "gmail-oauth2",
        **tokens,
    }

    token_file.write_text(json.dumps(artifact, ensure_ascii=False, indent=2), encoding="utf-8")
    cache_payload = {
        "generated_at": artifact["generated_at"],
        "tokens_saved": [token_file.name],
    }
    token_cache.write_text(json.dumps(cache_payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _run_oauth_login(oauth_code: Optional[str] = None) -> Dict[str, Any]:
    required_env = [
        "GMAIL_CLIENT_SECRET_PATH",
        "GMAIL_TOKEN_CACHE",
        "GMAIL_TOKEN_FILE",
        "GMAIL_OAUTH_SCOPES",
    ]
    status = _collect_required_env(required_env)
    missing = status["missing"]
    if missing:
        raise ValueError(f"missing required env vars: {', '.join(missing)}")

    secret_path = Path(os.environ["GMAIL_CLIENT_SECRET_PATH"])
    if not secret_path.exists():
        raise FileNotFoundError(f"missing client secret: {secret_path}")

    scopes = os.environ.get("GMAIL_OAUTH_SCOPES", "").split()
    if not scopes:
        raise ValueError("GMAIL_OAUTH_SCOPES is empty")

    secret = _read_client_secret(secret_path)
    redirect_uri = _pick_redirect_uri(secret["redirect_uris"])
    client_id = secret["client_id"]
    client_secret = secret["client_secret"]
    if oauth_code is None:
        state = secrets.token_urlsafe(16)
        params = {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "scope": " ".join(scopes),
            "access_type": "offline",
            "prompt": "consent",
            "state": state,
        }
        auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"

        print(f"[oauth] open this url in browser:\n{auth_url}")
        webbrowser.open(auth_url, new=1, autoraise=True)

        callback = _start_local_oauth_server(state, redirect_uri, timeout_seconds=300)
        if callback.get("error"):
            raise RuntimeError(f"oauth callback error: {callback['error']}")

        oauth_code = callback.get("code")
        if not oauth_code:
            raise TimeoutError("oauth callback timeout: code not returned within 300 seconds")

    else:
        print("[oauth] using provided oauth code")

    tokens = _exchange_auth_code_for_tokens(
        code=oauth_code,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
    )
    if "access_token" not in tokens:
        raise ValueError("token response missing access_token")

    profile = _gmail_me_profile(tokens["access_token"])
    _save_token_files(
        token_file=Path(os.environ["GMAIL_TOKEN_FILE"]),
        token_cache=Path(os.environ["GMAIL_TOKEN_CACHE"]),
        tokens={**tokens, "client_id": client_id, "client_secret": client_secret, "scopes": scopes},
    )

    return {
                "status": "ok",
                "oauth": {
                    "redirect_uri": redirect_uri,
                    "profile": {
                "email": profile.get("emailAddress"),
                "messages_total": profile.get("messagesTotal"),
                "threads_total": profile.get("threadsTotal"),
            },
            "access_scope": tokens.get("scope"),
            "token_type": tokens.get("token_type"),
        },
    }


def _load_token_artifact(token_file: Path) -> Dict[str, Any]:
    if not token_file.exists():
        raise FileNotFoundError(f"missing token file: {token_file}")
    data = _read_json(token_file)
    if not isinstance(data, dict) or "access_token" not in data:
        raise ValueError("token file is invalid: access_token missing")
    return data


def _write_token_artifact(token_file: Path, token_data: Dict[str, Any]) -> None:
    token_file.parent.mkdir(parents=True, exist_ok=True)
    token_file.write_text(
        json.dumps(token_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def _token_expired(token_data: Dict[str, Any]) -> bool:
    generated_at = token_data.get("generated_at")
    expires_in = token_data.get("expires_in")
    if not isinstance(generated_at, str) or not isinstance(expires_in, int):
        return False
    try:
        gen = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
    except ValueError:
        return False
    now = datetime.now(timezone.utc)
    # Refresh 2 minutes early.
    return now >= (gen + timedelta(seconds=max(0, expires_in - 120)))


def _refresh_access_token(token_data: Dict[str, Any]) -> Dict[str, Any]:
    refresh_token = token_data.get("refresh_token")
    client_id = token_data.get("client_id")
    client_secret = token_data.get("client_secret")
    if not all(isinstance(x, str) and x for x in [refresh_token, client_id, client_secret]):
        raise ValueError("refresh token flow requires refresh_token/client_id/client_secret")

    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }
    req = Request(
        "https://oauth2.googleapis.com/token",
        data=urlencode(payload).encode("utf-8"),
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urlopen(req, timeout=60) as resp:
        refreshed = json.loads(resp.read().decode("utf-8"))

    if "access_token" not in refreshed:
        raise ValueError("refresh response missing access_token")

    token_data["access_token"] = refreshed["access_token"]
    token_data["expires_in"] = int(refreshed.get("expires_in", token_data.get("expires_in", 3600)))
    token_data["token_type"] = refreshed.get("token_type", token_data.get("token_type", "Bearer"))
    token_data["generated_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    if isinstance(refreshed.get("scope"), str):
        token_data["scope"] = refreshed["scope"]
    return token_data


def _gmail_request(
    token_data: Dict[str, Any],
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, Any]] = None,
    retry_401: bool = True,
) -> Dict[str, Any]:
    url = f"{GMAIL_API_BASE}{path}"
    if params:
        query = urlencode(params, doseq=True)
        if query:
            url = f"{url}?{query}"
    headers = {
        "Authorization": f"Bearer {token_data['access_token']}",
        "Accept": "application/json",
    }
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json; charset=utf-8"
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")

    req = Request(url, method=method, headers=headers, data=data)
    try:
        with urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except HTTPError as exc:
        if exc.code == 401 and retry_401:
            token_data = _refresh_access_token(token_data)
            return _gmail_request(
                token_data=token_data,
                method=method,
                path=path,
                params=params,
                body=body,
                retry_401=False,
            )
        detail = exc.read().decode("utf-8", errors="ignore")
        raise ValueError(f"gmail api error {exc.code}: {detail[:400]}") from exc
    except URLError as exc:
        raise ValueError(f"gmail api request failed: {exc}") from exc


def _gmail_list_labels(token_data: Dict[str, Any]) -> Dict[str, str]:
    resp = _gmail_request(token_data, "GET", "/labels")
    mapping: Dict[str, str] = {}
    for item in resp.get("labels", []):
        if isinstance(item, dict) and isinstance(item.get("name"), str) and isinstance(item.get("id"), str):
            mapping[item["name"]] = item["id"]
    return mapping


def _gmail_create_label(token_data: Dict[str, Any], name: str) -> str:
    resp = _gmail_request(
        token_data,
        "POST",
        "/labels",
        body={
            "name": name,
            "labelListVisibility": "labelShow",
            "messageListVisibility": "show",
        },
    )
    label_id = resp.get("id")
    if not isinstance(label_id, str) or not label_id:
        raise ValueError(f"failed to create label: {name}")
    return label_id


def _gmail_list_recent_messages(token_data: Dict[str, Any], query: str, max_results: int) -> List[str]:
    resp = _gmail_request(
        token_data,
        "GET",
        "/messages",
        params={"q": query, "maxResults": max_results},
    )
    ids: List[str] = []
    for item in resp.get("messages", []):
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            ids.append(item["id"])
    return ids


def _gmail_get_message_metadata(token_data: Dict[str, Any], message_id: str) -> Dict[str, Any]:
    resp = _gmail_request(
        token_data,
        "GET",
        f"/messages/{quote(message_id, safe='')}",
        params={"format": "metadata", "metadataHeaders": ["From", "Subject"]},
    )
    headers = {}
    for h in resp.get("payload", {}).get("headers", []):
        if isinstance(h, dict) and isinstance(h.get("name"), str):
            headers[h["name"].lower()] = h.get("value", "")
    return {
        "id": resp.get("id", message_id),
        "threadId": resp.get("threadId"),
        "from": headers.get("from", ""),
        "subject": headers.get("subject", ""),
        "labelIds": resp.get("labelIds", []) if isinstance(resp.get("labelIds"), list) else [],
    }


def _gmail_modify_message(
    token_data: Dict[str, Any],
    message_id: str,
    add_label_ids: List[str],
    remove_label_ids: List[str],
) -> Dict[str, Any]:
    return _gmail_request(
        token_data,
        "POST",
        f"/messages/{quote(message_id, safe='')}/modify",
        body={"addLabelIds": add_label_ids, "removeLabelIds": remove_label_ids},
    )


def _normalize_text(value: Any) -> str:
    return str(value or "").strip().lower()


def _pattern_match(patterns: Iterable[str], target: str) -> bool:
    return any(p.lower() in target for p in patterns if isinstance(p, str) and p)


def _validate_labels(labels_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    errors = []
    required = {"version", "generated_at", "labels"}
    if not required.issubset(labels_data.keys()):
        errors.append(
            {
                "type": "schema",
                "message": "labels schema required fields missing: version, generated_at, labels",
            }
        )
        return errors

    labels = labels_data.get("labels") or []
    if not isinstance(labels, list):
        errors.append({"type": "schema", "message": "labels must be an array"})
        return errors

    if len(labels) > 15:
        errors.append(
            {
                "type": "policy",
                "message": f"labels count exceeds limit: {len(labels)} > 15",
            }
        )

    path_pattern = re.compile(r"^@([A-Za-z0-9_\-\uAC00-\uD7A3]+)(/([A-Za-z0-9_\-\uAC00-\uD7A3]+)){0,2}$")
    id_pattern = re.compile(r"^[a-z0-9_\-]+$")
    kinds = {"CTX", "AUTO", "SYS", "STATE"}

    seen_paths = {}
    seen_ids = set()
    for idx, item in enumerate(labels, 1):
        if not isinstance(item, dict):
            errors.append({"type": "schema", "message": f"label[{idx}] is not object"})
            continue
        for key in [
            "id",
            "path",
            "kind",
            "description",
            "source_rule_ref",
            "enabled",
            "caps",
        ]:
            if key not in item:
                errors.append(
                    {
                        "type": "schema",
                        "message": f'label[{idx}] missing required key "{key}"',
                    }
                )

        lid = item.get("id")
        kind = item.get("kind")
        path = item.get("path")
        source_refs = item.get("source_rule_ref")
        caps = item.get("caps", {})

        if not isinstance(lid, str) or not id_pattern.match(lid):
            errors.append(
                {"type": "schema", "message": f'label[{idx}] invalid id "{lid}"'}
            )
        elif lid in seen_ids:
            errors.append(
                {
                    "type": "schema",
                    "message": f'label[{idx}] duplicate id "{lid}"',
                }
            )
        else:
            seen_ids.add(lid)

        if not isinstance(path, str) or not path_pattern.match(path):
            errors.append(
                {"type": "schema", "message": f'label[{idx}] invalid path "{path}"'}
            )
        elif path in seen_paths:
            errors.append(
                {
                    "type": "schema",
                    "message": f'duplicate path "{path}" from {seen_paths[path]} and label[{idx}]',
                }
            )
        else:
            seen_paths[path] = f"label[{idx}]"

        if kind not in kinds:
            errors.append(
                {"type": "schema", "message": f'label[{idx}] invalid kind "{kind}"'}
            )

        if (
            not isinstance(source_refs, list)
            or len(source_refs) == 0
            or not all(isinstance(x, str) and x for x in source_refs)
        ):
            errors.append(
                {
                    "type": "schema",
                    "message": f"label[{idx}] source_rule_ref must be non-empty string list",
                }
            )
        else:
            if kind == "STATE":
                if source_refs != ["manual_state"]:
                    errors.append(
                        {
                            "type": "policy",
                            "message": f'label[{idx}] STATE must set source_rule_ref ["manual_state"]',
                        }
                    )
            else:
                if "manual_state" in source_refs:
                    errors.append(
                        {
                            "type": "policy",
                            "message": f'label[{idx}] non-STATE label cannot reference manual_state',
                        }
                    )

        if not isinstance(caps, dict):
            errors.append(
                {"type": "schema", "message": f'label[{idx}] caps must be object'}
            )
        else:
            if "inbox_priority" not in caps or caps["inbox_priority"] not in {
                "high",
                "normal",
                "low",
            }:
                errors.append(
                    {
                        "type": "schema",
                        "message": f'label[{idx}] caps.inbox_priority is required/high|normal|low',
                    }
                )
            if "requires_review" not in caps or not isinstance(caps["requires_review"], bool):
                errors.append(
                    {
                        "type": "schema",
                        "message": f'label[{idx}] caps.requires_review must be boolean',
                    }
                )
            if "max_depth" in caps:
                depth = caps.get("max_depth")
                if not isinstance(depth, int) or not (1 <= depth <= 3):
                    errors.append(
                        {
                            "type": "policy",
                            "message": f'label[{idx}] caps.max_depth must be integer 1..3',
                        }
                    )

    return errors


def _validate_filters(filters_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    errors = []
    required = {"version", "generated_at", "filters"}
    if not required.issubset(filters_data.keys()):
        errors.append(
            {
                "type": "schema",
                "message": "filters schema required fields missing: version, generated_at, filters",
            }
        )
        return errors

    filters = filters_data.get("filters")
    if not isinstance(filters, list):
        errors.append({"type": "schema", "message": "filters must be an array"})
        return errors

    ids = []
    id_pattern = re.compile(r"^[a-z0-9_\-]+$")

    for idx, rule in enumerate(filters, 1):
        if not isinstance(rule, dict):
            errors.append({"type": "schema", "message": f"filter[{idx}] is not object"})
            continue

        for key in [
            "id",
            "name",
            "priority",
            "enabled",
            "actions",
        ]:
            if key not in rule:
                errors.append(
                    {
                        "type": "schema",
                        "message": f'filter[{idx}] missing required key "{key}"',
                    }
                )

        rid = rule.get("id")
        priority = rule.get("priority")
        actions = rule.get("actions", {})

        if not isinstance(rid, str) or not id_pattern.match(rid):
            errors.append(
                {
                    "type": "schema",
                    "message": f'filter[{idx}] invalid id "{rid}"',
                }
            )
        else:
            ids.append(rid)

        if not isinstance(priority, int) or not (0 <= priority <= 999):
            errors.append(
                {
                    "type": "schema",
                    "message": f'filter[{rid or idx}] priority must be integer 0..999',
                }
            )

        from_patterns = rule.get("from_patterns", [])
        subject_patterns = rule.get("subject_patterns", [])
        if not (
            isinstance(from_patterns, list)
            and len(from_patterns) > 0
            and all(isinstance(x, str) and x for x in from_patterns)
        ) and not (
            isinstance(subject_patterns, list)
            and len(subject_patterns) > 0
            and all(isinstance(x, str) and x for x in subject_patterns)
        ):
            errors.append(
                {
                    "type": "schema",
                    "message": f'filter[{rid}] must define from_patterns or subject_patterns with at least 1 string',
                }
            )

        if not isinstance(actions, dict):
            errors.append(
                {"type": "schema", "message": f'filter[{rid}] actions must be object'}
            )
            continue

        apply_labels = actions.get("apply_labels")
        if (
            not isinstance(apply_labels, list)
            or len(apply_labels) == 0
            or not all(isinstance(x, str) and x for x in apply_labels)
        ):
            errors.append(
                {
                    "type": "schema",
                    "message": f'filter[{rid}] actions.apply_labels must be a non-empty list',
                }
            )

        for field in ("skip_inbox", "mark_read", "mark_important", "star"):
            if field in actions and not isinstance(actions.get(field), bool):
                errors.append(
                    {
                        "type": "schema",
                        "message": f'filter[{rid}] actions.{field} must be boolean',
                    }
                )

        if "conflict_with" in rule:
            if not isinstance(rule["conflict_with"], list) or not all(
                isinstance(x, str) and x for x in rule["conflict_with"]
            ):
                errors.append(
                    {
                        "type": "schema",
                        "message": f'filter[{rid}] conflict_with must be string array',
                    }
                )
        if "mutual_exclusive_group" in rule and rule["mutual_exclusive_group"] is not None:
            if not isinstance(rule["mutual_exclusive_group"], str) or not rule[
                "mutual_exclusive_group"
            ].strip():
                errors.append(
                    {
                        "type": "schema",
                        "message": f'filter[{rid}] mutual_exclusive_group must be non-empty string',
                    }
                )

    duplicates = [k for k, v in Counter(ids).items() if v > 1]
    for dup in duplicates:
        errors.append({"type": "schema", "message": f'duplicate filter id "{dup}"'})

    priorities = [rule.get("priority") for rule in filters if isinstance(rule, dict)]
    duplicate_priority = [p for p, c in Counter(priorities).items() if isinstance(p, int) and c > 1]
    if duplicate_priority:
        errors.append(
            {
                "type": "warn",
                "message": f"duplicate priorities detected: {sorted(set(duplicate_priority))}",
            }
        )

    return errors


def _load_and_validate(label_path: Path, filter_path: Path) -> Dict[str, Any]:
    labels_data = _read_json(label_path)
    filters_data = _read_json(filter_path)
    report = {
        "labels": {
            "version": labels_data.get("version"),
            "total": len(labels_data.get("labels", [])),
            "errors": _validate_labels(labels_data),
        },
        "filters": {
            "version": filters_data.get("version"),
            "total": len(filters_data.get("filters", [])),
            "errors": _validate_filters(filters_data),
        },
        "policy": {
            "label_refs_to_unknown_filters": [],
            "filter_labels_exist": [],
        },
    }

    known_paths = {item.get("path") for item in labels_data.get("labels", []) if isinstance(item, dict)}
    filter_ids = {item.get("id") for item in filters_data.get("filters", []) if isinstance(item, dict)}

    for item in labels_data.get("labels", []):
        if not isinstance(item, dict):
            continue
        refs = item.get("source_rule_ref", [])
        if item.get("kind") != "STATE":
            for ref in refs:
                if ref not in filter_ids:
                    report["policy"]["label_refs_to_unknown_filters"].append(
                        {"label": item.get("path"), "ref": ref}
                    )

    for rule in filters_data.get("filters", []):
        if not isinstance(rule, dict):
            continue
        for lbl in rule.get("actions", {}).get("apply_labels", []):
            if lbl not in known_paths:
                report["policy"]["filter_labels_exist"].append(
                    {"filter_id": rule.get("id"), "unknown_label": lbl}
                )

    return {"labels": labels_data, "filters": filters_data, "report": report}


def _kind_rank_from_label(path: str) -> int:
    if not isinstance(path, str):
        return 3
    prefix = path.strip().split("/", 1)[0].replace("@", "")
    return {"SYS": 0, "CNU": 0, "CTX": 1, "AUTO": 2, "GTD": 3}.get(prefix, 3)


def _simulate_one_rule(rule: Dict[str, Any], msg: Dict[str, str]) -> bool:
    from_patterns = [p.lower() for p in rule.get("from_patterns", []) if isinstance(p, str)]
    subject_patterns = [p.lower() for p in rule.get("subject_patterns", []) if isinstance(p, str)]
    exclude_patterns = [p.lower() for p in rule.get("exclude_patterns", []) if isinstance(p, str)]

    sender = _normalize_text(msg.get("from"))
    subject = _normalize_text(msg.get("subject"))

    from_ok = _pattern_match(from_patterns, sender) if from_patterns else True
    subject_ok = _pattern_match(subject_patterns, subject) if subject_patterns else True
    target_ok = from_ok and subject_ok
    if not target_ok:
        return False

    if _pattern_match(exclude_patterns, sender) or _pattern_match(exclude_patterns, subject):
        return False
    return True


def _compare_rules(rule_a: Dict[str, Any], rule_b: Dict[str, Any]) -> int:
    if rule_a["priority"] != rule_b["priority"]:
        return -1 if rule_a["priority"] < rule_b["priority"] else 1

    labels_a = rule_a.get("actions", {}).get("apply_labels", [])
    labels_b = rule_b.get("actions", {}).get("apply_labels", [])
    rank_a = min((_kind_rank_from_label(l) for l in labels_a), default=3)
    rank_b = min((_kind_rank_from_label(l) for l in labels_b), default=3)
    if rank_a != rank_b:
        return -1 if rank_a < rank_b else 1

    refs_a = "".join(sorted(rule_a.get("source_rule_ref", [])))
    refs_b = "".join(sorted(rule_b.get("source_rule_ref", [])))
    if refs_a != refs_b:
        return -1 if refs_a < refs_b else 1

    if rule_a["id"] != rule_b["id"]:
        return -1 if rule_a["id"] < rule_b["id"] else 1
    return 0


def _is_critical_label(path: str) -> bool:
    if not isinstance(path, str):
        return False
    return path.startswith("@SYS/") or path.startswith("@CNU/")


def _is_critical_rule(rule: Dict[str, Any]) -> bool:
    labels = rule.get("actions", {}).get("apply_labels", [])
    return any(_is_critical_label(p) for p in labels if isinstance(p, str))


def _select_rules_for_message(matches: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not matches:
        return []

    group_picks: Dict[str, Dict[str, Any]] = {}
    for rule in matches:
        group = rule.get("mutual_exclusive_group")
        if group is None:
            continue
        existing = group_picks.get(group)
        if existing is None or _compare_rules(rule, existing) < 0:
            group_picks[group] = rule

    grouped_ids = {r["id"] for r in group_picks.values()}
    selected = []
    for rule in matches:
        group = rule.get("mutual_exclusive_group")
        if group is not None and rule["id"] not in grouped_ids:
            continue
        selected.append(rule)

    selected_map = {r["id"]: r for r in selected}
    conflict_filtered = []
    for rule in selected:
        conflicts = set(rule.get("conflict_with", []))
        if any(
            (cid in selected_map)
            and _compare_rules(selected_map[cid], rule) < 0
            for cid in conflicts
        ):
            continue
        if any(
            (rule["id"] in selected_map.get(cid, {}).get("conflict_with", []))
            and _compare_rules(selected_map[cid], rule) < 0
            for cid in conflicts
        ):
            continue
        conflict_filtered.append(rule)
    return conflict_filtered


def _simulate(filters: List[Dict[str, Any]], messages: List[Dict[str, str]]) -> Dict[str, Any]:
    enabled_rules = [f for f in filters if isinstance(f, dict) and f.get("enabled", False)]
    enabled_rules.sort(key=lambda r: (r.get("priority", 999), r.get("id", "")))

    results = []
    for msg in messages:
        matches = []
        for rule in enabled_rules:
            if _simulate_one_rule(rule, msg):
                matches.append(rule)
        conflict_filtered = _select_rules_for_message(matches)

        labels = []
        for rule in conflict_filtered:
            labels.extend(rule.get("actions", {}).get("apply_labels", []))
        labels = sorted(set(labels))

        results.append(
            {
                "message_key": msg.get("id") or msg.get("message_id") or msg.get("subject", ""),
                "from": msg.get("from"),
                "subject": msg.get("subject"),
                "matched_rules": [r["id"] for r in conflict_filtered],
                "labels": labels,
                "skip_inbox": any(
                    bool(r.get("actions", {}).get("skip_inbox", False))
                    for r in conflict_filtered
                ),
            }
        )

    return {"processed": len(messages), "results": results}


def _run_apply_pilot(
    label_file: Path,
    filter_file: Path,
    pilot_limit: int,
    pilot_hours: int,
    approval_text: str,
    allow_critical: bool,
) -> Dict[str, Any]:
    if approval_text.strip() != PHASE7B_APPROVAL_TEXT:
        raise ValueError("approval text mismatch")
    if pilot_limit < 5 or pilot_limit > 10:
        raise ValueError("pilot_limit must be between 5 and 10")
    if pilot_hours <= 0:
        raise ValueError("pilot_hours must be positive")

    loaded = _load_and_validate(label_file, filter_file)
    report = loaded["report"]
    plan_fail = bool(
        report["labels"]["errors"]
        or report["filters"]["errors"]
        or report["policy"]["label_refs_to_unknown_filters"]
        or report["policy"]["filter_labels_exist"]
    )
    if plan_fail:
        raise ValueError("policy artifacts have blocking errors; fix before apply")

    required_env = [
        "GMAIL_TOKEN_FILE",
        "GMAIL_CLIENT_SECRET_PATH",
        "GMAIL_TOKEN_CACHE",
        "GMAIL_TOKEN_STORE",
    ]
    env_state = _collect_required_env(required_env)
    if env_state["missing"]:
        raise ValueError(f"missing required env vars: {', '.join(env_state['missing'])}")

    token_file = Path(os.environ["GMAIL_TOKEN_FILE"])
    token_data = _load_token_artifact(token_file)
    if _token_expired(token_data):
        token_data = _refresh_access_token(token_data)
        _write_token_artifact(token_file, token_data)

    filters_all = [f for f in loaded["filters"].get("filters", []) if isinstance(f, dict) and f.get("enabled")]
    filters_all.sort(key=lambda r: (r.get("priority", 999), r.get("id", "")))
    if allow_critical:
        filters_apply = filters_all
    else:
        filters_apply = [r for r in filters_all if not _is_critical_rule(r)]

    if not filters_apply:
        raise ValueError("no eligible rules for apply pilot")

    days = max(1, int(math.ceil(pilot_hours / 24)))
    query = f"newer_than:{days}d"
    list_max = min(100, max(30, pilot_limit * 6))
    message_ids = _gmail_list_recent_messages(token_data, query=query, max_results=list_max)
    if not message_ids:
        return {
            "status": "ok",
            "applied": 0,
            "message": "no candidate messages found",
            "query": query,
            "limit": pilot_limit,
        }

    needed_paths = set()
    for rule in filters_apply:
        for p in rule.get("actions", {}).get("apply_labels", []):
            if isinstance(p, str) and p:
                needed_paths.add(p)
    label_map = _gmail_list_labels(token_data)
    missing_paths = [p for p in sorted(needed_paths, key=lambda x: x.count("/")) if p not in label_map]
    for path in missing_paths:
        _gmail_create_label(token_data, path)
    if missing_paths:
        label_map = _gmail_list_labels(token_data)

    candidate_messages = []
    protected_skips = []
    for mid in message_ids:
        meta = _gmail_get_message_metadata(token_data, mid)
        msg = {"id": meta["id"], "from": meta.get("from", ""), "subject": meta.get("subject", "")}

        matches_all = [r for r in filters_all if _simulate_one_rule(r, msg)]
        selected_all = _select_rules_for_message(matches_all)

        if (not allow_critical) and any(_is_critical_rule(r) for r in selected_all):
            protected_skips.append(
                {
                    "message_id": meta["id"],
                    "from": meta.get("from", ""),
                    "subject": meta.get("subject", ""),
                    "matched_critical_rules": [r.get("id") for r in selected_all if _is_critical_rule(r)],
                }
            )
            continue

        matches_apply = [r for r in filters_apply if _simulate_one_rule(r, msg)]
        selected_apply = _select_rules_for_message(matches_apply)
        if not selected_apply:
            continue
        candidate_messages.append({"meta": meta, "selected_rules": selected_apply})
        if len(candidate_messages) >= pilot_limit:
            break

    if len(candidate_messages) < 5:
        raise ValueError(
            f"insufficient candidates for pilot: {len(candidate_messages)} found, require at least 5"
        )

    applied_records = []
    failures = []
    for item in candidate_messages:
        meta = item["meta"]
        selected_rules = item["selected_rules"]
        current_labels = set(meta.get("labelIds", []))

        label_paths = sorted(
            {
                p
                for rule in selected_rules
                for p in rule.get("actions", {}).get("apply_labels", [])
                if isinstance(p, str)
            }
        )
        add_label_ids = [label_map[p] for p in label_paths if p in label_map]
        remove_label_ids: List[str] = []
        if any(bool(r.get("actions", {}).get("skip_inbox", False)) for r in selected_rules):
            remove_label_ids.append("INBOX")
        if any(bool(r.get("actions", {}).get("mark_read", False)) for r in selected_rules):
            remove_label_ids.append("UNREAD")
        if any(bool(r.get("actions", {}).get("star", False)) for r in selected_rules):
            add_label_ids.append("STARRED")
        if any(bool(r.get("actions", {}).get("mark_important", False)) for r in selected_rules):
            add_label_ids.append("IMPORTANT")

        add_final = sorted(set(x for x in add_label_ids if x and x not in current_labels))
        remove_final = sorted(set(x for x in remove_label_ids if x and x in current_labels))
        add_final = [x for x in add_final if x not in remove_final]

        if not add_final and not remove_final:
            applied_records.append(
                {
                    "message_id": meta["id"],
                    "from": meta.get("from"),
                    "subject": meta.get("subject"),
                    "matched_rules": [r.get("id") for r in selected_rules],
                    "status": "noop",
                }
            )
            continue

        try:
            _gmail_modify_message(token_data, meta["id"], add_final, remove_final)
            applied_records.append(
                {
                    "message_id": meta["id"],
                    "from": meta.get("from"),
                    "subject": meta.get("subject"),
                    "matched_rules": [r.get("id") for r in selected_rules],
                    "add_label_ids": add_final,
                    "remove_label_ids": remove_final,
                    "status": "applied",
                }
            )
        except Exception as exc:
            failures.append({"message_id": meta["id"], "error": str(exc)})
            attempted = len([r for r in applied_records if r.get("status") in {"applied", "noop"}]) + len(failures)
            failure_rate = len(failures) / max(1, attempted)
            if failure_rate > 0.10:
                rollback_errors = []
                for done in reversed([r for r in applied_records if r.get("status") == "applied"]):
                    try:
                        _gmail_modify_message(
                            token_data,
                            done["message_id"],
                            done.get("remove_label_ids", []),
                            done.get("add_label_ids", []),
                        )
                        done["rollback"] = "ok"
                    except Exception as rb_exc:
                        done["rollback"] = "fail"
                        rollback_errors.append(
                            {"message_id": done["message_id"], "error": str(rb_exc)}
                        )
                return {
                    "status": "fail",
                    "query": query,
                    "limit": pilot_limit,
                    "applied_records": applied_records,
                    "protected_skips": protected_skips,
                    "failures": failures,
                    "rollback_errors": rollback_errors,
                    "message": "stopped: failure rate > 10%, rollback executed",
                }

    _write_token_artifact(token_file, token_data)
    return {
        "status": "ok",
        "query": query,
        "limit": pilot_limit,
        "selected_candidates": len(candidate_messages),
        "applied": len([r for r in applied_records if r.get("status") == "applied"]),
        "noop": len([r for r in applied_records if r.get("status") == "noop"]),
        "failures": failures,
        "protected_skips": protected_skips,
        "applied_records": applied_records,
    }


def run_plan(label_file: Path, filter_file: Path, sample_path: Optional[Path] = None) -> Dict[str, Any]:
    loaded = _load_and_validate(label_file, filter_file)
    report = loaded["report"]
    labels_data = loaded["labels"]
    filters_data = loaded["filters"]

    checks = []
    checks.extend(
        [
            {"name": "labels_schema", "status": "pass" if not report["labels"]["errors"] else "fail"},
            {"name": "filters_schema", "status": "pass" if not report["filters"]["errors"] else "fail"},
            {
                "name": "label_version",
                "status": "pass"
                if labels_data.get("version") == "v3.0.0"
                else "warn",
                "value": labels_data.get("version"),
            },
            {
                "name": "filter_version",
                "status": "pass"
                if filters_data.get("version") == "v3.0.0"
                else "warn",
                "value": filters_data.get("version"),
            },
            {
                "name": "label_count",
                "status": "pass" if len(labels_data.get("labels", [])) <= 15 else "fail",
                "value": len(labels_data.get("labels", [])),
            },
            {
                "name": "filter_count",
                "status": "pass" if len(filters_data.get("filters", [])) >= 12 else "warn",
                "value": len(filters_data.get("filters", [])),
            },
            {
                "name": "policy_refs",
                "status": "pass" if not (report["policy"]["label_refs_to_unknown_filters"] or report["policy"]["filter_labels_exist"]) else "fail",
                "details": report["policy"],
            },
        ]
    )

    failed = [c for c in checks if c["status"] == "fail"]
    plan = {
        "status": "pass" if not failed else "warn",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "mode": "plan-only",
        "checks": checks,
        "schema": {
            "labels_total": report["labels"]["total"],
            "filters_total": report["filters"]["total"],
        },
        "violations": {
            "labels": report["labels"]["errors"],
            "filters": report["filters"]["errors"],
            "policy": report["policy"],
        },
    }

    if sample_path:
        samples = _read_json(sample_path)
        if isinstance(samples, dict) and isinstance(samples.get("messages"), list):
            samples = samples["messages"]
        if not isinstance(samples, list):
            raise ValueError("sample_path must contain array or {\"messages\":[]}")
        plan["dry_run_simulation"] = _simulate(
            filters_data.get("filters", []), samples
        )

    return plan


def main() -> int:
    parser = argparse.ArgumentParser(description="gmail-agent-sys plan-only runtime")
    parser.add_argument("--plan-only", action="store_true", help="run static plan checks only")
    parser.add_argument("--dry-run", action="store_true", help="enable simulation mode")
    parser.add_argument("--apply", action="store_true", help="run limited mutate pilot apply mode")
    parser.add_argument("--sample", type=str, help="JSON sample file for dry-run")
    parser.add_argument(
        "--connect-check",
        action="store_true",
        help="validate MCP environment contract and required credentials/env",
    )
    parser.add_argument(
        "--oauth-login",
        action="store_true",
        help="run Gmail OAuth login flow and save token artifacts",
    )
    parser.add_argument(
        "--oauth-code",
        type=str,
        default=None,
        help="skip browser flow and exchange a manually copied Gmail auth code",
    )
    parser.add_argument("--labels", type=str, default=str(CONFIG_DIR / "labels.v3.json"))
    parser.add_argument(
        "--filters", type=str, default=str(CONFIG_DIR / "filters.v3.json")
    )
    parser.add_argument(
        "--pilot-limit",
        type=int,
        default=10,
        help="apply pilot message cap (must be 5..10)",
    )
    parser.add_argument(
        "--pilot-hours",
        type=int,
        default=24,
        help="candidate lookback window in hours",
    )
    parser.add_argument(
        "--approve-text",
        type=str,
        default="",
        help="exact phase7-b approval text",
    )
    parser.add_argument(
        "--allow-critical",
        action="store_true",
        help="allow critical SYS/CNU rules in apply pilot (disabled by default)",
    )
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    payload = {
        "status": "pass",
        "mode": "plan-only",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }

    label_path = Path(args.labels)
    filter_path = Path(args.filters)
    sample_path = Path(args.sample) if args.sample else None

    payload["artifact"] = {
        "labels": str(label_path),
        "filters": str(filter_path),
        "sample": str(sample_path) if sample_path else None,
    }

    if args.connect_check:
        required_env = [
            "GMAIL_CLIENT_SECRET_PATH",
            "GMAIL_TOKEN_CACHE",
            "GMAIL_TOKEN_FILE",
            "GMAIL_TOKEN_STORE",
            "GMAIL_OAUTH_SCOPES",
        ]
        payload["connect_check"] = _collect_required_env(required_env)
        secret_path = os.getenv("GMAIL_CLIENT_SECRET_PATH", str(Path.home() / ".config/gmail-agent-sys/client_secret.json"))
        token_file = os.getenv("GMAIL_TOKEN_FILE", str(Path.home() / ".cache/gmail-agent-sys/token.json"))
        payload["connect_check"]["client_secret_exists"] = Path(secret_path).exists()
        payload["connect_check"]["token_file_exists"] = Path(token_file).exists()
        if payload["connect_check"]["status"] == "warn":
            payload["status"] = "warn"

    if not label_path.exists() or not filter_path.exists():
        print(
            json.dumps(
                {
                    "status": "fail",
                    "message": f"Missing artifact: labels={label_path.exists()} filters={filter_path.exists()}",
                },
                ensure_ascii=False,
                indent=2 if args.pretty else None,
            )
        )
        return 1

    has_mode = args.plan_only or args.dry_run or args.connect_check or args.oauth_login or args.apply
    if not has_mode:
        payload = {
            "status": "fail",
            "message": "no mode selected. Use --plan-only/--dry-run/--apply.",
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None))
        return 1

    if args.plan_only or args.dry_run or args.connect_check or args.oauth_login or args.apply:
        plan = run_plan(label_path, filter_path, sample_path if args.sample else None)
        payload["plan"] = plan
        if plan["status"] != "pass":
            payload["status"] = plan["status"]

    if args.oauth_login:
        try:
            payload["oauth_login"] = _run_oauth_login(oauth_code=args.oauth_code)
        except Exception as exc:
            payload["oauth_login"] = {
                "status": "fail",
                "message": str(exc),
            }
            payload["status"] = "fail"

    if args.apply:
        try:
            payload["apply_pilot"] = _run_apply_pilot(
                label_file=label_path,
                filter_file=filter_path,
                pilot_limit=args.pilot_limit,
                pilot_hours=args.pilot_hours,
                approval_text=args.approve_text,
                allow_critical=args.allow_critical,
            )
            if payload["apply_pilot"].get("status") != "ok":
                payload["status"] = "fail"
        except Exception as exc:
            payload["apply_pilot"] = {"status": "fail", "message": str(exc)}
            payload["status"] = "fail"

    print(
        json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True)
    )
    return 0 if payload["status"] != "fail" else 1


if __name__ == "__main__":
    sys.exit(main())
