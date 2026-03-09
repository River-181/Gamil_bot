# Phase 10 Notes 01: snapshot -> apply-snapshot -> trash-commit

## 목적
- `기타 9600 -> 0`, `has:nouserlabels -> 0` 목표를 위해 대량 처리 경로를 `snapshot -> apply-snapshot -> trash-commit`으로 고정한다.
- direct scan 후 즉시 mutate는 운영 기본경로에서 제외한다.
- backlog 처리는 `rule-family queue` 기준으로 분해한다.

## 현재 운영 기준
- 분류 apply는 항상 snapshot 파일을 먼저 만든 뒤 적용한다.
- `apply-snapshot`은 snapshot에 들어 있는 `message_id`만 건드린다.
- `TrashCandidate`는 즉시 삭제하지 않고 `14일 보존 후 TRASH`로 이동한다.
- rollback은 apply/trash journal 기준으로 수행한다.
- queue 기본값:
  - `bulk_low_value`
  - `social_newsletter`
  - `context_ops`
  - `critical_review`
  - `manual_residual`(review-only)

## 승인 문구
- apply:
  - `Phase 10 실제 분류 파일럿(최대 200건)을 승인합니다. self-sent 메일은 자동 변경하지 않고, 이상 징후 발생 시 즉시 중단하고 롤백 절차를 수행합니다.`
- trash:
  - `Phase 10 TrashCandidate 보존 메일을 TRASH로 이동하는 것을 승인합니다. 이상 징후 발생 시 즉시 중단하고 롤백 절차를 수행합니다.`

## 추천 실행 순서
1. `--build-snapshot --snapshot-queue <queue> --snapshot-limit 25`
2. snapshot 샘플 리뷰
3. `--apply-snapshot <file>`
4. 결과/저널 확인
5. 규모 확대:
  - 최근 구간: `25 -> 50 -> 200`
  - 중기/장기 구간: `50 -> 200 -> 500`
6. `@AUTO/TrashCandidate older_than:14d`부터 `--trash-commit`

## 핵심 가드
- self-sent는 자동 변경 금지
- `@SYS/Security`, `CNU OTP`, 금융/영수증/예약 계열은 trash 분류 금지
- `TrashCandidate`는 `label-first, trash-later`
- batch 확대는 직전 배치 실패율/오분류 리뷰 통과 후만 허용

## 산출물
- snapshot:
  - `.tokens/phase10_snapshot_*.json`
- apply journal:
  - `.tokens/phase10_apply_journal_*.jsonl`
- trash journal:
  - `.tokens/phase10_trash_journal_*.jsonl`

## 운영 메모
- 최근 30일 정리는 snapshot 50/200로 빠르게 수렴한다.
- 오래된 backlog는 `31~180d`, `181d+`처럼 구간을 쪼개야 한다.
- Gmail metadata 조회가 느리므로, 전체 snapshot보다 `queue 기반 targeted snapshot`이 더 안정적이다.
