# gmail-agent-sys 워크스페이스

## 목적
`/Users/river/tools/gmail-agent-sys`는 개인 Gmail 운영을 위한 **설계·검토 전용 레이어**이다.
현재 단계는 OpenClaw 포함 외부 자동화 실행을 배제하고, 실행 가능한 정책 정합성만 확정한다.

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
- 실 API 호출/자동 적용은 보류
- `--dry-run`, `--plan-only` 우선 실행 체계만 문서/계약으로 유지
- 인증 비밀(클라이언트 시크릿/토큰)은 파일에 저장하지 않음

## 다음 단계
1. Phase 7-b: 실제 mutate 파일럿(5~10건) 승인 실행
2. Phase 7-b: 실행 로그/오분류/롤백 여부 기록
3. Phase 8: 사고 대응/백업 체계 운영 정착 + 리포트 자동화(주간 digest/드리프트 요약)

## 즉시 실행 커맨드 (plan-only)
- 환경 준비:
  - `GMAIL_CLIENT_SECRET_PATH`, `GMAIL_TOKEN_CACHE`, `GMAIL_TOKEN_FILE`, `GMAIL_TOKEN_STORE`, `GMAIL_OAUTH_SCOPES`를 환경변수에 설정
- 정책 정합성 확인:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --plan-only --pretty`
- 연동 전 체크:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --plan-only --connect-check --pretty`
- 실제 Gmail OAuth 연결(토큰 발급, 최초 1회):
  - `python3 -m gmail_agent_sys.mcp.entrypoint --oauth-login --pretty`
- 브라우저 인증이 막히면 수동 코드 교환:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --oauth-code <code> --pretty`
- 샘플 시뮬레이션(비실시간):
  - `python3 -m gmail_agent_sys.mcp.entrypoint --dry-run --sample tests/plans/phase3_sample_messages.json --pretty`

## 구현 상태
- `/Users/river/tools/gmail-agent-sys/gmail_agent_sys/mcp/entrypoint.py`는 `--apply` 파일럿 모드를 지원합니다.
- `--apply`는 승인 문구 일치, 건수 제한(5~10), critical 규칙 제외, 오류율 초과 시 중단/롤백 가드로 보호됩니다.
