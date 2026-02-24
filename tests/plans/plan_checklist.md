# Gmail 워크스페이스 계획 점검 체크리스트

## Phase 1 점검 완료
- [x] 기본 문서/스키마/폴더 구조 정합
- [x] 14개 라벨 정합본 생성
- [x] 필터 정합본 작성
- [x] Hook/Skill/Persona 계약 문서화

## Phase 2 점검 항목 (정책 정규화)
1. [x] 라벨/필터 버전 동기화
   - `config/labels.v3.json` 버전: `v3.0.0`
   - `config/filters.v3.json` 버전: `v3.0.0`
   - `normalization_ref`: `policy_normalization_v3.md`

2. [x] 충돌·우선순위 고정
   - 우선순위 체인(`docs/policy_normalization_v3.md`) 준수
   - `@SYS` 계열 최상위 우선권 유지
   - `cnu_scope`, `social_group`, `news_group`, `notification_group` 상호 배타 규칙 준수

3. [x] 스키마 정합성
   - `config/labels.schema.json` 구조 준수
   - `config/filters.schema.json` 구조 준수
   - 필수 필드 누락 없음

4. [x] 운영 드리프트 금지 조건
   - 임시 규칙(`rule_gtd_state_apply`) 미적용 상태 유지
   - 라벨 총 수 15 초과 없음
   - 중복 필터 ID 없음
   - 민감정보 노출 항목 없음

## Phase 3 점검 항목 (MCP 계약)
1. MCP 설정 정합성
   - `config/mcp.server.json` 존재 및 `transport: stdio` 설정
   - `server_id: gmail-agent-system` 고정
   - `env`에 `GMAIL_CLIENT_SECRET_PATH`, `GMAIL_TOKEN_CACHE`, `GMAIL_TOKEN_FILE` 정의
   - `labels.v3.json`, `filters.v3.json`, `policy_normalization_v3.md` 참조 존재

2. 실행 모드 정책
   - 기본 모드 `plan-only` 유지
   - `dry-run` 존재 및 실제 apply 선행 조건 표현
   - apply 모드에서 승인/드라이런 게이트 존재

3. 오류 대응 규칙
   - `docs/mcp_retry_policy_v3.md`에서 401/429/5xx 대응 규정 존재
   - 재시도 상한/백오프/Dead-letter 항목 정의
   - 429·5xx에 대한 재시도 제한 정의

4. 보안 가드
   - 토큰 하드코딩 금지
   - 로그 마스킹 대상(Authorization 계열) 정의

## Phase 3 실행 증적 (2026-02-24)
- [x] OAuth 브라우저 인증 콜백 완료
- [x] 토큰 파일 생성 확인 (`/Users/river/tools/gmail-agent-sys/.tokens/token.json`)
- [x] `--connect-check --plan-only` 결과 `status=pass` 확인
- [x] `--dry-run --sample tests/plans/phase3_sample_messages.json` 결과 `processed=6`, `status=pass` 확인
- [x] 정책 정합성(`labels_schema`, `filters_schema`, `policy_refs`) 전부 `pass`

## Phase 4 점검 항목 (Skill + Hook)
1. Skill 계약
   - `gmail-policy-audit`/`gmail-filter-lint`/`gmail-label-health`의 입출력(JSON) 계약 존재
   - `status` 체계(`pass|warn|fail`) 사용 통일
   - 위반 시 `tests/plans/plan_checklist.md`에 근거 반영

2. Hook 실행 계약
   - `hooks/hooks.v3.json` 존재
   - 이벤트: SessionStart, UserPromptSubmit, PostToolUse, Stop, ErrorBoundary 정의
   - `mask_sensitive=true`, `log_only=true`, `fail_open=true`
   - 출력 필드(JSON 요약 존재)

3. 오케스트레이션
   - `docs/skills_hooks_integration_v3.md` 존재
   - 세션 핸드오버 항목(Stop hook) 존재

4. 보안
   - 하드코딩 훅 경로를 회피하고 워크스페이스 기반 경로 사용
   - 민감정보 마스킹 패턴 점검

## Phase 4 실행 증적 (2026-02-24)
- [x] Skill 계약 3종 존재 확인 (`gmail-policy-audit`, `gmail-filter-lint`, `gmail-label-health`)
- [x] Hook 레지스트리(`hooks/hooks.v3.json`) 이벤트 5종 정의 확인
- [x] Hook 스크립트 5종 존재 확인 (`session_start`, `user_prompt`, `post_tool_use`, `stop_handoff`, `error_boundary`)
- [x] 실행 경로 동결 문서 반영 (`docs/skills_hooks_integration_v3.md`)

## Phase 5 점검 항목 (품질 게이트)
1. 정적 게이트 통과
   - 스키마 통과(라벨/필터)
   - 라벨 수 <= 15
   - 필수 정책 참조 일치

2. 정책 게이트 통과
   - 보안 우선권 및 충돌 규칙 일관성 통과
   - 우선순위 체인과 실제 정합성 확인

3. 운영 게이트 통과
   - MCP contract/mode/retry 정책 존재
   - Skill/Hook JSON/요약 형식 통일

4. 승인 조건
   - Phase 5 문서 존재(`tests/plans/quality_gate_v3.md`)
   - 사용자 승인 문구 및 apply 게이트 정의 완료

## Phase 5 최종 판정 (2026-02-24)
- [x] 정적/정책/운영 게이트 `PASS`
- [x] 최종 판정 문서 생성 (`tests/plans/phase5_final_verdict_v3.md`)
- [x] 승인 기반 운영 전환 전제(`plan-only/dry-run 우선`) 유지

## Phase 6 진입 조건(Next)
- [x] Phase 5 체크리스트 전부 통과
- [x] 다음 턴에서 실행 준비 상태 승인
- [x] 정책 변경 요청/릴리즈 프로토콜 확정

## Phase 6 점검 항목 (승인 기반 Apply 전환 준비)
1. [x] 승인 기반 apply 런북 생성
   - `docs/runbooks/apply_approval_runbook_v3.md`
2. [x] 릴리즈 프로토콜 문서 생성
   - `docs/release_protocol_v3.md`
3. [x] 승인 게이트/중단 규칙/롤백 기준 문서화
4. [x] mutate 미실행 원칙 유지 (`plan-only`, `dry-run` 우선)

## Phase 7 점검 항목 (파일럿 apply + 대응/백업)
1. [x] 파일럿 apply 런북 생성
   - `docs/runbooks/phase7_pilot_apply_v3.md`
2. [x] 사고 대응/백업 플레이북 생성
   - `docs/runbooks/incident_backup_playbook_v3.md`
3. [x] 파일럿 범위 승인(건수/시간창/규칙 범위)
4. [x] 실행 전 백업 스냅샷 기록
5. [x] 실행 후 영향도/오류율/오분류 리뷰 완료
   - 실행 기록: `tests/plans/phase7_pilot_execution_20260224.md`

## Phase 7-b 점검 항목 (실제 mutate 파일럿 5~10건)
1. [x] 실행 런북 생성
   - `docs/runbooks/phase7b_mutate_pilot_v3.md`
2. [x] 실행 준비 판정 문서 생성
   - `tests/plans/phase7b_apply_readiness_20260224.md`
3. [x] 실행 직전 스냅샷 재생성
4. [x] 대상 메시지 ID 5~10건 확정
5. [x] 승인 문구 확인 후 mutate 실행
6. [x] 실행 로그/오분류/롤백 여부 기록
   - `tests/plans/phase7b_mutate_execution_log_20260224.md`
