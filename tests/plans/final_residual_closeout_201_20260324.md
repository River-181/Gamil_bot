# final residual closeout 201 2026-03-24

## current live residual
- `has:nouserlabels = 201`
- verified by live Gmail query:
  - `has:nouserlabels newer_than:3650d`

## current lane snapshot result
- `Security-first` -> `0`
- `Read-first` -> `0`
- `Reference-first` -> `0`
- `Manual-Work` -> `0`
- conclusion:
  - the remaining 201 are not covered by the current lane rule set.

## compression outcome
- remaining unlabeled mail has been compressed into lane-based apply-ready documents.
- however, the current lane rules do not yet reach the full residual.
- the next move is coverage expansion, not blind apply.

## source material
- `/Users/river/tools/gmail-agent-sys/tests/plans/apply_ready_security_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/apply_ready_read_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/apply_ready_reference_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/apply_ready_manual_work_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_master_summary_20260324.md`

## apply order
1. `Security-first`
2. `Read-first`
3. `Reference-first`
4. `Manual-Work`

## batch sizing guidance
- `Security-first`
  - small, high-confidence batches first
- `Read-first`
  - bulk apply is safe after security
- `Reference-first`
  - bulk apply after read
- `Manual-Work`
  - last, thread-based, review-gated

## success criteria
- `has:nouserlabels = 0`
- coverage for the remaining 201 is explicitly explained
- no new broad queues remain
- new inbound mail is handled by steady-state lanes

## note
- do not expand auto rules further.
- the remaining work is targeted coverage expansion plus final apply.
