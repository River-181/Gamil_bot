# Phase 9 마이그레이션 게이트 v2026-03-05

## 실행결과 요약 (run_id: 20260305T171000Z)
- `phase9_archive_mapping_20260305.json` 존재: 확인
- `phase9_legacy_label_baseline_20260305.md` 존재: 확인
- `collisions` 상태: `[]` (충돌 없음)
- 체크포인트: `.tokens/archive_migration_checkpoint_20260305T171000Z.json` (status=done)
- 저널: `.tokens/archive_migration_journal_20260305T171000Z.jsonl` (총 레코드 576건, message_id 중복 없음)
- 처리 결과: `messages_scanned=1392`, `run_messages=745`, `processed=745`, `failures=0`
- Stage A/B 진행 후 잔여 없음 (`next_stage` 종료)

## Gate 1: Baseline 정합성
- 레거시 라벨 분류 결과가 완성되어야 함
- `phase9_legacy_label_baseline_20260305.md` 존재 및 최신
- 충돌 없는 매핑 파일 존재 (`collisions: []`)

## Gate 2: Dry-run 안전성
- `--archive-migrate --dry-run --approve-text` 실행 시:
  - `status` == `ok`
  - `failures == []`
  - `legacy_labels_total > 0` 또는 해당 계정에서 명시적 0개 정책 존재 시 승인 결정
  - `next_stage`는 `A` 또는 `C`
- `rollback_ready`는 실패 시 `False`, 성공 시 `True` 허용

## Gate 3: Stage 200 전환
- `legacy` 대상 라벨 중 복구 가능한 아카이브 레이블이 생성되었는지 확인
- `messages_scanned` 및 `messages_mutated` 추적
- 실패율 `> 10%`면 즉시 중단
- 실패 사유가 보안/의미론적으로 심각하면 Stage B 이전 보류

## Gate 4: Stage 1000 전환
- Stage A 종료 후 Stage B에서 동일 기준 적용
- `journal_path`/`checkpoint_path` 존재
- `applied_records` 내 중복 메시지 ID 없음

## Gate 5: Stage C(전체) 종료
- `status` == `done` 또는 `stopped`(수동 중단)
- `rollback_ready` 검증
- 필요 시 즉시 `--archive-rollback --run-id <id>` 실행 검증

## Gate 6: 운영 위험 게이트
- 보안/CNU 라벨 오분류 또는 기존 라벨 삭제 없음
- 시스템 라벨(이전 라벨) 존재 불변
- 민감정보가 journal/checkpoint에 메시지 본문 형태로 남지 않음(메시지 ID 기반만 저장)

## 최종 판정
- Phase 9 Stage A/B 완료: Pass
- 운영 리스크 게이트: Pass(현재까지 메시지 본문 미저장, 오류율 0% 기반)
- 다음 단계 이동 조건:  
  - 14일 경과 후 정리 후보 승인(Phase 9 cleanup)  
  - 필요 시 `--archive-rollback --run-id 20260305T171000Z`로 576개 항목 역적용 가능성 확인
