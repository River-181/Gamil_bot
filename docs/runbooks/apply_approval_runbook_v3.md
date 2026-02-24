# Phase 6: 승인 기반 Apply Runbook (v3)

## 목적
정책 정규화(Phase 2)와 품질 게이트(Phase 5)를 통과한 상태에서, 실제 Gmail 변경 단계로 넘어가기 전 승인 절차와 실행/중단 규칙을 고정한다.

## 현재 범위
- 현재 엔트리포인트는 `plan-only`, `dry-run`, `connect-check`, `oauth-login` 중심으로 운영한다.
- 본 문서는 실제 mutate 실행 전에 필요한 승인 패키지와 롤백 판단 기준을 정의한다.

## 적용 전 필수 입력
- 정책 파일:
  - `config/labels.v3.json`
  - `config/filters.v3.json`
  - `docs/policy_normalization_v3.md`
- 런타임 상태:
  - OAuth 토큰 유효
  - `--connect-check --plan-only` 결과 `status=ok`
  - `--dry-run --sample tests/plans/phase3_sample_messages.json` 결과 `status=pass`

## 승인 게이트
1. Gate A: 정적 게이트
- 스키마 통과
- 라벨 수 `<= 15`
- 참조 정합성 위반 0건

2. Gate B: 정책 게이트
- `@SYS/Security` 보존 규칙 유지
- 충돌 규칙(`mutual_exclusive_group`, `conflict_with`) 위반 0건
- 동일 우선순위 다중 채택 가능성 0건(P1 차단)

3. Gate C: 운영 게이트
- `docs/mcp_contract_v3.md`, `docs/mcp_retry_policy_v3.md` 최신화
- Hook 가드(`mask_sensitive`, `log_only`, `fail_open`) 유지
- Phase 5 최종 판정서 `PASS`

## 승인 패키지 산출물
- `tests/plans/phase5_final_verdict_v3.md`
- `tests/plans/quality_gate_v3.md`
- `tests/plans/plan_checklist.md`
- 변경 요약(추가/삭제 규칙, 영향 범위, 예상 리스크)

## 실행/중단 규칙
- 승인 전에는 mutate 성격 작업 금지
- 401 반복, 429 초과, 5xx 반복 발생 시 즉시 중단
- 중단 시 `dead-letter` 형식으로 요약 기록 후 수동 재승인 필요

## 롤백 기준
- 보안 라벨 누락/삭제 징후 발생
- 인박스 스킵 오동작으로 중요 메일 누락 가능성 확인
- 우선순위 충돌로 동일 메일 다중 분기 발생

## 종료 조건
- 승인 기록 존재
- 운영자(사용자) apply 시작 확인
- 실패 시 재승인 루프로 복귀
