# Phase 7-b 실제 Mutate 파일럿 실행 로그 (2026-02-24)

## 실행 요약
- 실행 모드: `--apply`
- 승인 문구: 검증 통과
- 적용 범위: 최대 5건
- 조회 범위: `newer_than:3d` (초기 24시간은 후보 부족으로 재시도)
- 결과: `PASS`

## 실행 결과
- 선택 후보: 5건
- 실제 적용: 5건
- 실패: 0건
- noop: 0건
- 보호 스킵(critical): 1건 (`rule_cnu_otp`)

## 로그 파일
- 실패 실행(후보 부족):
  - `/Users/river/tools/gmail-agent-sys/tests/plans/phase7b_mutate_execution_result_20260224.json`
- 성공 실행:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/phase7b_mutate_execution_result_20260224_run2.json`

## 비고
- 보안/CNU critical 규칙은 mutate 대상에서 제외되어 안전 가드 유지
- 라벨 적용은 기존 v3 라벨 체계를 그대로 사용했고, 한 라벨 아래로 재집계하지 않음
