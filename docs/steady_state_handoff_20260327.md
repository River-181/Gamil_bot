# Steady-State Handoff (2026-03-27)

## 1) 현재 운영 기준선
- `has:nouserlabels`: `201`
- `in:inbox has:nouserlabels`: `201`
- `label:@AUTO/TrashCandidate older_than:14d`: `201`
- 정책 외 사용자 라벨의 루트 외 잔여: `0` (`-----` 하위로 정리 완료)

## 2) 오늘 수행된 마감 작업
- 정책 외 사용자 라벨 일괄 리네임:
  - root: `-----`
  - renamed: `105`
  - skipped: `0`
- 완료 보고서 작성:
  - `/Users/river/tools/gmail-agent-sys/docs/project_completion_report_20260327.md`

## 3) 일일 운영 루틴 (권장)
1. `--plan-only --connect-check --pretty`
2. `--build-snapshot` (queue/rule targeted, 50~200)
3. `--apply-snapshot` (승인문구 + 저널 필수)
4. `has:nouserlabels`, `in:inbox has:nouserlabels` 재측정
5. `label:@AUTO/TrashCandidate older_than:14d`가 기준 이상이면 `--trash-commit` 소배치 실행

## 4) 중단 기준 (즉시 stop)
- apply 실패율 `> 10%`
- `@SYS/*`, `@CNU/*` 오분류 1건 이상
- self-sent 자동변경 발생
- 저널/체크포인트 기록 실패

## 5) 롤백 명령
- apply 롤백:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --apply-rollback --apply-journal-file <journal.jsonl> --apply-run-id <run_id> --pretty`
- trash 롤백:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --trash-rollback --trash-journal-file <trash_journal.jsonl> --trash-run-id <run_id> --pretty`
- legacy archive 롤백:
  - `python3 -m gmail_agent_sys.mcp.entrypoint --archive-rollback --run-id <run_id> --checkpoint-file <checkpoint.json> --journal-file <journal.jsonl> --pretty`

## 6) 다음 액션 (최소 단위)
1. 잔여 `201`에 대해 safe slice 기준으로 `50 -> 100 -> tail` 적용
2. 각 배치 종료 시 저널/요약 문서 즉시 기록
3. `0` 도달 후 3일간 일일 모니터링으로 재발 여부 확인

