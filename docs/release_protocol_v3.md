# Gmail-Agent-SYS 릴리즈 프로토콜 (v3)

## 목적
정책 변경과 운영 전환을 승인 가능한 단위로 관리하고, 충돌/드리프트를 최소화한다.

## 릴리즈 단위
- `Policy Release`: `config/labels.v3.json`, `config/filters.v3.json`, `docs/policy_normalization_v3.md`
- `Runtime Release`: `docs/mcp_contract_v3.md`, `docs/mcp_retry_policy_v3.md`, `docs/runbooks/*`
- `Ops Release`: `hooks/hooks.v3.json`, `skills/*/SKILL.md`, `tests/plans/*`

## 변경 요청 규칙
1. 정책 변경은 `정규화 문서`를 먼저 수정하고 JSON 인스턴스를 맞춘다.
2. 라벨 신규 1개 추가 시 기존 1개 제거 원칙을 우선 검토한다.
3. 충돌 규칙을 바꾸면 `quality_gate_v3.md`에 테스트 시나리오를 같이 갱신한다.

## 릴리즈 게이트
1. 사전 검증
- `--plan-only` 통과
- `--dry-run` 통과
- Phase 5 판정 `PASS` 유지

2. 승인
- 사용자 승인 문구 확보
- 적용 범위(라벨/필터/훅) 명시
- 실패 시 중단 조건 명시

3. 릴리즈 기록
- 버전, 날짜, 변경 파일, 위험도, 롤백 조건 기록
- 운영자 확인 결과(승인/보류) 기록

## 버전 규칙
- 정책 버전: `v3.x.y`
- `x` 변경: 정책 의미 변경(충돌/우선순위 규칙)
- `y` 변경: 설명/주석/운영 문구 보완

## 금지 사항
- 시크릿/토큰 하드코딩
- 승인 없는 apply 실행
- 게이트 미통과 상태에서 릴리즈 태깅

## 운영 전환 조건
- `tests/plans/phase5_final_verdict_v3.md` 최신 `PASS`
- `docs/runbooks/apply_approval_runbook_v3.md` 기준 승인 완료
- 다음 단계에서 실제 mutate 구현/실행 범위 별도 승인
