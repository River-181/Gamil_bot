# Release Notes - 2026-03-09

Commit: `d5c6284` (`feat: add snapshot-driven gmail cleanup workflow`)

## Summary
- Added snapshot-driven Gmail cleanup workflow for safer staged mutation.
- Added `@AUTO/TrashCandidate` as the 15th v3 label.
- Added journaling and rollback paths for apply/trash operations.
- Added operational notes and runbooks for archive migration and rollback.

## Product Changes
- New workflow: `build-snapshot -> apply-snapshot -> trash-commit`
- New rollback path: `trash-rollback`
- Direct bulk mutation remains available but is no longer the default operating path.

## Policy Changes
- Label count increased from 14 to 15 with `@AUTO/TrashCandidate`.
- Filter set expanded to 15 rules.
- `TrashCandidate` is stronger than `Promo`, but excludes security, CNU, finance, travel, social, notification, and self-sent mail.
- Added false-positive guards for finance/card/loan and LinkedIn newsletter overlap.

## Code Changes
- `/Users/river/tools/gmail-agent-sys/gmail_agent_sys/mcp/entrypoint.py`
  - Added snapshot build/apply/trash CLI paths
  - Added apply/trash journals and rollback support
  - Fixed `--apply-batch --dry-run` behavior
- `/Users/river/tools/gmail-agent-sys/config/labels.v3.json`
  - Added `@AUTO/TrashCandidate`
- `/Users/river/tools/gmail-agent-sys/config/filters.v3.json`
  - Added trash-candidate rules and guard rules

## Docs Added
- `/Users/river/tools/gmail-agent-sys/docs/phase10_notes_01_snapshot_apply_trash.md`
- `/Users/river/tools/gmail-agent-sys/docs/phase10_notes_02_bulk_targeting_and_false_positive.md`
- `/Users/river/tools/gmail-agent-sys/docs/runbooks/legacy_label_archive_migration_v1.md`
- `/Users/river/tools/gmail-agent-sys/docs/runbooks/legacy_label_rollback_v1.md`

## Verification
- `python3 -m py_compile /Users/river/tools/gmail-agent-sys/gmail_agent_sys/mcp/entrypoint.py`
- `python3 -m gmail_agent_sys.mcp.entrypoint --plan-only --pretty`

## Secret Scan Notes
- Local regex scan found no committed live secrets.
- Hits in `/Users/river/tools/gmail-agent-sys/gmail_agent_sys/mcp/entrypoint.py` were field names such as `client_secret`, not embedded credentials.
- GitHub repository visibility was confirmed as `public`; GitHub-side secret scanning/push protection status could not be confirmed from unauthenticated API responses.
