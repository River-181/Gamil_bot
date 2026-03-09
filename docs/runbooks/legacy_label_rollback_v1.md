# Legacy 라벨 아카이브 마이그레이션 롤백 Runbook v1

## 목적
- Stage A/B/C 적용 중/후 오분류 또는 운영 영향이 있을 때 즉시 역적용한다.

## 필수 입력
- `run_id`: 마이그레이션 실행 ID
- `checkpoint_file`: 기본 `.tokens/archive_migration_checkpoint_<run_id>.json`
- `journal_file`: 기본 `.tokens/archive_migration_journal_<run_id>.jsonl`

## 롤백 실행
```bash
python3 -m gmail_agent_sys.mcp.entrypoint \
  --archive-rollback \
  --run-id <RUN_ID> \
  --checkpoint-file .tokens/archive_migration_checkpoint_<RUN_ID>.json \
  --journal-file .tokens/archive_migration_journal_<RUN_ID>.jsonl
```

## 기대 출력
- `status` : `ok`(완전 롤백) 또는 `warn`(잔여 남음)
- `rolled_back`: 롤백 시도 적용 수
- `rollback_failures`: 실패 상세
- `remaining_impacted_messages`: 재시도 필요 개수

## 롤백 규칙
- 역순 재생
- 메시지당 `archive_label_ids`만 제거
- 기존 라벨은 되돌리지 않음(이번 단계에서는 추가-only 정책 준수)
- 실패 항목은 별도 retry list로 분리

## 확인
- `remaining_impacted_messages == 0`일 때 완전 롤백 완료
- 미해결이 있으면:
  - 환경 이슈인지, 특정 메시지 접근권한 이슈인지 분리
- 완료 후 `--plan-only --connect-check` 및 `--connect-check` 검증 반복
