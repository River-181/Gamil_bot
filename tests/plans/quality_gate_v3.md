# Phase 5: 품질 게이트 (v3)

## 목적
`gmail-agent-sys`를 다음 단계로 넘기기 전에 정책/실행 계약이 충돌 없이 일관적인지 문서 기반으로 확정한다.

## 1) 정적 게이트 (실행 전 필수)
- JSON 스키마
  - `config/labels.schema.json` 유효성 통과
  - `config/filters.schema.json` 유효성 통과
- 정규본 일치
  - `config/labels.v3.json.version == v3.0.0`
  - `config/filters.v3.json.version == v3.0.0`
  - `config/labels.v3.json.labels.length == 14`
  - `config/filters.v3.json.filters.length >= 12`
  - `config/filters.v3.json.normalization_ref == docs/policy_normalization_v3.md`
- 라벨 제약
  - 라벨 총수 <= 15
  - `source_rule_ref` 존재, `STATE`은 `manual_state`만 허용
  - 경로 중복 없음
- 필터 제약
  - 각 필터 `priority` 정수
  - `from_patterns` 또는 `subject_patterns` 중 하나 존재
  - `actions.apply_labels` 최소 1개

## 2) 정책 게이트
- 보안 최상위 우선권 확인
  - `rule_sys_security`가 최상위 보안 규칙(정렬 상단)
  - `@SYS/Security` 제외 규칙 없음
- 충돌 규칙 확인
  - `@CNU` 계열(`cnu_student`, `cnu_notice`, `cnu_otp`)은 상호 배타/우선순위 해석 보유
  - `social_group`, `news_group`, `notification_group` 충돌 규칙 존재
  - 동일 priority + 동일 조건 교집합 시 1개 규칙만 채택(P1)
  - 동일 우선순위 + 그룹 다중 매칭 시 comparator 적용(`priority`, group 우선, kind 우선순위, source_rule_ref/id 정렬)
- 정책 문서 정합
  - `docs/policy_normalization_v3.md`, `docs/strategy_v3.md`, `config/*.json` 내용 일치

## 3) 운영 게이트
- MCP 계약 정합
  - `config/mcp.server.json` plan-only 우선, dry-run/plan-only에서 apply 금지
  - 재시도 정책과 dead-letter 개념이 `docs/mcp_retry_policy_v3.md`에 존재
- Skill/Hook 실행성
  - Phase 4 산출물 존재
  - 훅 출력이 JSON 요약 형식
  - Skill 상태 표준(`pass|warn|fail`) 사용

## 4) 실패 기준(블로커)
- P0(진입 불가): 라벨 수 초과/스키마 미통과/보안 우선권 위반/OAuth/시크릿 하드코딩
- P1(보류): 충돌 점검 미해결/동일 우선순위 다중 규칙 중치명 충돌/중요 경로 미기재
- P2(경고): 권고 조정 필요(예: 비효율 규칙, 불필요 중복)

## 5) 승인 루트
- Phase 5 완료 후 apply 실행은 사용자 승인과 별도 dry-run 합격 기록이 있어야만 허용
- 승인 문서에 최소 3개 항목 기록
  - 정적 게이트 통과 항목
  - 정책 게이트 통과 항목
  - 적용 위험도 요약

## 6) 단계 종료 산출물
- `/Users/river/tools/gmail-agent-sys/tests/plans/quality_gate_v3.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/plan_checklist.md`의 Phase 5 항목 체크 업데이트

## 7) Phase 3 런타임 검증 증적 (2026-02-24)
- OAuth 인증 완료 후 토큰 생성 확인:
  - `/Users/river/tools/gmail-agent-sys/.tokens/token.json` 존재
- `connect-check` 통과 조건 확인:
  - `GMAIL_CLIENT_SECRET_PATH`, `GMAIL_TOKEN_CACHE`, `GMAIL_TOKEN_FILE`, `GMAIL_TOKEN_STORE`, `GMAIL_OAUTH_SCOPES` 모두 설정 시 `status=ok`
- `dry-run` 시나리오 통과:
  - 샘플 6건 처리, 충돌/참조 위반 없음, 전체 `status=pass`

## 8) 최종 판정 (2026-02-24)
- 판정 결과: `PASS`
- 판정 근거 문서:
  - `tests/plans/plan_checklist.md`
  - `tests/plans/phase5_final_verdict_v3.md`
- 판정 조건:
  - 정적 게이트 통과
  - 정책 게이트 통과
  - 운영 게이트 통과
  - apply 미실행(`plan-only/dry-run`) 상태 유지

## 9) Phase 6 전환 기준 (승인 기반 apply 준비)
- 승인 런북:
  - `docs/runbooks/apply_approval_runbook_v3.md`
- 릴리즈 프로토콜:
  - `docs/release_protocol_v3.md`
- 전환 상태:
  - 문서 기준 전환 `완료`
  - 실제 mutate 실행 `미실행` (다음 단계 승인 필요)
