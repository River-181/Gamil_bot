# Legacy 라벨 Shadow Archive 마이그레이션 Runbook v1

## 목적
- 기존 사용자 라벨을 즉시 삭제하지 않고 `#Archive/Legacy-20260305/<legacy_label>` 라벨로 이관한다.
- 기존 라벨은 유지하고, 기존 시스템 동작을 보존한다.

## 전제
- 정책 파일:
  - `config/labels.v3.json`
  - `config/filters.v3.json`
- 실행 문구 승인:
  - `Phase 9 Legacy 라벨 일괄 아카이브(Shadow Archive)로 전환합니다. 기존 라벨 유지 및 14일 내 삭제 보류를 승인합니다.`
- 실행 환경:
  - `.tokens` 토큰 유효
  - `connect-check` 통과

## 1) Baseline freeze
- Legacy 라벨 목록 산정: `legacy-user`
- v3 라벨 14개 제외
- 시스템 라벨 제외
- 아카이브 대상만 `#Archive/Legacy-20260305` 하위로 매핑

```bash
python3 -m gmail_agent_sys.mcp.entrypoint \
  --archive-migrate \
  --dry-run \
  --archive-root "#Archive/Legacy-20260305" \
  --migration-scope legacy-user \
  --batch-size 200 \
  --approve-text "Phase 9 Legacy 라벨 일괄 아카이브(Shadow Archive)로 전환합니다. 기존 라벨 유지 및 14일 내 삭제 보류를 승인합니다."
```

- 출력에서 `mapping.collisions`가 `[]`인지 확인한다.
- 출력의 `mapping.mapping`을 `tests/plans/phase9_archive_mapping_20260305.json`에 반영한다.

## 2) Dry-run (Stage A, 200건)
```bash
python3 -m gmail_agent_sys.mcp.entrypoint \
  --archive-migrate \
  --dry-run \
  --archive-root "#Archive/Legacy-20260305" \
  --migration-scope legacy-user \
  --batch-size 200 \
  --approve-text "Phase 9 Legacy 라벨 일괄 아카이브(Shadow Archive)로 전환합니다. 기존 라벨 유지 및 14일 내 삭제 보류를 승인합니다." \
  --run-id "$(date -u +%Y%m%dT%H%M%SZ)"
```

- 출력에서 다음 필수 항목 확인:
  - `status == ok`
  - `messages_mutated` 0 (dry-run)
  - `applied_records` 내 중복 `message_id` 없음
  - `next_stage` 값 확인(`A` 또는 `done`)

## 3) Stage A apply (200)
```bash
python3 -m gmail_agent_sys.mcp.entrypoint \
  --archive-migrate \
  --archive-root "#Archive/Legacy-20260305" \
  --migration-scope legacy-user \
  --batch-size 200 \
  --approve-text "Phase 9 Legacy 라벨 일괄 아카이브(Shadow Archive)로 전환합니다. 기존 라벨 유지 및 14일 내 삭제 보류를 승인합니다." \
  --run-id <RUN_ID>
```

- 실패율 10% 초과 또는 심각오류 발생 시 즉시 중단
- `journal_path`, `checkpoint_path` 보존

## 4) Stage B apply (1000)
- 동일 커맨드 재실행 (run-id 고정)
- 기존 `checkpoint`에서 stage 자동 확장 확인

## 5) Stage C apply (전체)
- 동일 커맨드 재실행 (run-id 고정)
- 상태가 `done`이 될 때까지 반복

## 6) 결과 점검
- `legacy` 라벨은 삭제하지 않음(keep archive copy)
- `messages_mutated`와 `failures` 추세 확인
- 오분류/보안/중요 규칙 변화가 있는지 수동 점검

## 종료 판단
- `--run-id <id>` 기준으로 journal/checkpoint이 일치해야 함
- 실패가 누적되면 즉시 `rollback`로 전환
- 기본 아티팩트 경로:
  - `.tokens/archive_migration_checkpoint_<run_id>.json`
  - `.tokens/archive_migration_journal_<run_id>.jsonl`
