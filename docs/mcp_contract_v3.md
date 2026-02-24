# Gmail MCP v3 계약 문서

## 1) 목적
`gmail-agent-sys`가 Gmail MCP를 호출할 때 공유할 최소 계약과 운영 제약을 정의한다.

## 2) 기본 전제
- 서버 ID: `gmail-agent-system`
- transport: `stdio`
- 실행 환경: `python3` + `gmail_agent_sys.mcp.entrypoint`
- 인증: OAuth(로컬 token 캐시), 비밀값 하드코딩 금지
- 기본 모드: `plan-only`

## 3) 필수 환경 변수
- `GMAIL_CLIENT_SECRET_PATH`
- `GMAIL_TOKEN_CACHE`
- `GMAIL_TOKEN_FILE`
- `GMAIL_TOKEN_STORE`
- `GMAIL_OAUTH_SCOPES`

## 4) 동작 모드
- `plan-only` (기본): 변경 없이 정책/루트/우선순위 계산만 수행
- `dry-run`: API 대상 dry-run 시뮬레이션
- `apply`: 실제 적용. 운영 승인(수동 승인) + 드라이런 사전통과 필수

## 5) 필수 API 기능
- auth.oauth
- labels:list
- labels:apply
- filters:list
- filters:test
- filters:create
- filters:delete
- mail:search
- mail:query:dry_run

## 6) 인증/재시도 룰
- 401: 즉시 토큰 갱신/재인증 플로우 유도
- 429: 60초 지수 백오프 + jitter, 최대 재시도 5회
- 5xx: 지수 백오프로 회복 시도
- 재시도 실패 시 dead-letter 기록(요약만 저장)

## 7) 안전 가드
- apply 모드에서 변경 전후 diff 생성
- 민감정보 헤더/토큰은 로그 마스킹
- plan-only 미동의 시 apply 차단
- 토큰 파일 권한: 사용자 홈 경로만 허용(권한 엄격)

## 8) 종료 조건(Phase 2~3)
- 라벨/필터 정합 검사 통과
- 보안 룰 우선권(401/보안 라우팅) 정책이 문서(`docs/policy_normalization_v3.md`)와 일치
- 드라이런에서 우선순위 충돌 없음 판정

