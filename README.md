# gmail-agent-sys 워크스페이스

## 목적
`/Users/river/tools/gmail-agent-sys`는 개인 Gmail 운영을 위한 **정책+운영 레이어**이다.
현재 기준은 `snapshot -> apply-snapshot -> trash-commit` 흐름으로 Gmail 정리와 유지 운영을 수행한다.

## 아키텍처(고정)
- `docs/` : 전략, 정합 정책, 흐름/Runbook
- `config/` : 라벨/필터 스키마 및 정규본 인스턴스
- `personas/` : 판단 주체별 운영 가이드
- `skills/` : 정책 감사/필터 정합 검사 계약
- `hooks/` : 세션 훅 및 보안 가드
- `tests/plans/` : 문서 기준 품질게이트

## Phase 2 고정 산출물
- 라벨 정규본: `config/labels.v3.json`
- 필터 정규본: `config/filters.v3.json`
- 충돌/우선순위 규약: `docs/policy_normalization_v3.md`

## 운영 제약(현재)
- direct `--apply-batch`는 유지하되 운영 기본경로는 `snapshot -> apply-snapshot -> trash-commit`
- `@AUTO/TrashCandidate`는 보존 후 삭제 후보 라벨로 사용
- 인증 비밀(클라이언트 시크릿/토큰)은 파일에 저장하지 않음

## 다음 단계
1. snapshot 기반 최근 메일 안정화 (`50 -> 200`)
2. backlog drain (`200 -> 500 -> 1000`)
3. delayed trash 및 rollback 운영

## 즉시 실행 커맨드 (plan-only)
- 환경 준비:
  - `GMAIL_CLIENT_SECRET_PATH`, `GMAIL_TOKEN_CACHE`, `GMAIL_TOKEN_FILE`, `GMAIL_TOKEN_STORE`, `GMAIL_OAUTH_SCOPES`를 환경변수에 설정
- 정책 정합성 확인:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --plan-only --pretty`
- snapshot 생성:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --build-snapshot --snapshot-limit 50 --snapshot-file .tokens/phase10_snapshot.json --pretty`
- snapshot 적용:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --apply-snapshot .tokens/phase10_snapshot.json --apply-run-id phase10-snapshot-run --apply-journal-file .tokens/phase10_apply_journal.jsonl --approve-text "<phase10 approval text>" --pretty`
- TrashCandidate commit:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --trash-commit --trash-limit 50 --trash-run-id phase10-trash-run --trash-journal-file .tokens/phase10_trash_journal.jsonl --approve-text "<phase10 trash approval text>" --pretty`
- 연동 전 체크:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --plan-only --connect-check --pretty`
- 실제 Gmail OAuth 연결(토큰 발급, 최초 1회):
  - `python3 -m gmail_agent_sys.mcp.entrypoint --oauth-login --pretty`
- 브라우저 인증이 막히면 수동 코드 교환:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --oauth-code <code> --pretty`
- 샘플 시뮬레이션(비실시간):
  - `python3 -m gmail_agent_sys.mcp.entrypoint --dry-run --sample tests/plans/phase3_sample_messages.json --pretty`

## 구현 상태
- `/Users/river/tools/gmail-agent-sys/gmail_agent_sys/mcp/entrypoint.py`는 `--build-snapshot`, `--apply-snapshot`, `--trash-commit`, `--trash-rollback`을 지원합니다.
- `@AUTO/TrashCandidate`를 포함한 v3.1 라벨/필터 정책이 적용됩니다.
- 운영 노하우 시리즈:
  - `docs/phase10_notes_01_snapshot_apply_trash.md`
  - `docs/phase10_notes_02_bulk_targeting_and_false_positive.md`
