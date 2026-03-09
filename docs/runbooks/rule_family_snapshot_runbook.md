# Rule-Family Snapshot Runbook

## 목적
- backlog를 `rule-family queue` 단위로 잘라서 안전하게 snapshot/apply/trash 흐름으로 운영한다.

## 공통 규칙
- snapshot 생성은 `--snapshot-queue` 또는 `--snapshot-rule-ids` 중 하나만 사용한다.
- 시간창 분리는 `--snapshot-hours`와 `--snapshot-min-hours`를 같이 사용한다.
- 최근 구간 기본 배치: `25 -> 50 -> 200`
- 중기/장기 구간 기본 배치: `50 -> 200 -> 500`
- apply 전에는 샘플 리뷰를 남긴다.
- apply 후에는 journal 생성 여부와 오분류 표본을 기록한다.

## queue 템플릿
### `bulk_low_value`
```bash
python3 -m gmail_agent_sys.mcp.entrypoint \
  --build-snapshot \
  --snapshot-queue bulk_low_value \
  --snapshot-limit 25 \
  --snapshot-hours 720 \
  --snapshot-min-hours 0 \
  --snapshot-file .tokens/bulk_low_value_0_30d.json \
  --pretty
```

### `social_newsletter`
```bash
python3 -m gmail_agent_sys.mcp.entrypoint \
  --build-snapshot \
  --snapshot-queue social_newsletter \
  --snapshot-limit 25 \
  --snapshot-hours 720 \
  --snapshot-min-hours 0 \
  --snapshot-file .tokens/social_newsletter_0_30d.json \
  --pretty
```

### `context_ops`
```bash
python3 -m gmail_agent_sys.mcp.entrypoint \
  --build-snapshot \
  --snapshot-queue context_ops \
  --snapshot-limit 25 \
  --snapshot-hours 720 \
  --snapshot-min-hours 0 \
  --snapshot-file .tokens/context_ops_0_30d.json \
  --pretty
```

### `critical_review`
```bash
python3 -m gmail_agent_sys.mcp.entrypoint \
  --build-snapshot \
  --snapshot-queue critical_review \
  --allow-critical \
  --snapshot-limit 25 \
  --snapshot-hours 720 \
  --snapshot-min-hours 0 \
  --snapshot-file .tokens/critical_review_0_30d.json \
  --pretty
```

## apply 템플릿
```bash
python3 -m gmail_agent_sys.mcp.entrypoint \
  --apply-snapshot .tokens/<snapshot>.json \
  --apply-run-id <run-id> \
  --apply-journal-file .tokens/<journal>.jsonl \
  --approve-text "Phase 10 실제 분류 파일럿(최대 200건)을 승인합니다. self-sent 메일은 자동 변경하지 않고, 이상 징후 발생 시 즉시 중단하고 롤백 절차를 수행합니다." \
  --pretty
```

## trash 템플릿
```bash
python3 -m gmail_agent_sys.mcp.entrypoint \
  --trash-commit \
  --trash-older-than-days 14 \
  --trash-limit 25 \
  --trash-run-id <run-id> \
  --trash-journal-file .tokens/<trash-journal>.jsonl \
  --approve-text "Phase 10 TrashCandidate 보존 메일을 TRASH로 이동하는 것을 승인합니다. 이상 징후 발생 시 즉시 중단하고 롤백 절차를 수행합니다." \
  --pretty
```

## 샘플 리뷰 체크리스트
- self-sent 포함 여부
- `@SYS/*`, `@CNU/*` 오분류 신호
- finance/receipt/travel가 `TrashCandidate`로 잘못 들어가지 않았는지
- LinkedIn/Newsletter 중복 같은 경계 사례 재발 여부
- journal 생성 여부

## 시간 구간 예시
- `0~30d`
```bash
--snapshot-hours 720 --snapshot-min-hours 0
```
- `31~180d`
```bash
--snapshot-hours 4320 --snapshot-min-hours 720
```
- `181~365d`
```bash
--snapshot-hours 8760 --snapshot-min-hours 4320
```

## 중단/롤백 기준
- 실패율 `> 2%`
- self-sent 변경 `1건 이상`
- critical 오분류 `1건 이상`
- journal 파일 누락

## 수동 queue
- `manual_residual`은 직접 snapshot queue로 사용하지 않는다.
- rule-family queue를 모두 소진한 뒤 남은 무라벨 메일을 대상으로 조사/규칙 보강을 수행한다.
