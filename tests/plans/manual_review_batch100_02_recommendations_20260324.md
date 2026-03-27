# manual review batch100_02 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_02_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## batch shape
- total messages: `100`
- dominant sender:
  - `chany010713@gmail.com`
- sender variants:
  - `98` messages from `chany010713@gmail.com`
  - `2` messages from `"주용김" <chany010713@gmail.com>`
- dominant subject:
  - `삼겹살 600g`
  - `99` messages with that exact subject
  - `1` message with subject `삼겹살`
- thread pattern:
  - no multi-message Gmail threads in this slice
  - operationally this is still one repeated self-sent cluster, not 100 independent work items

## recommended triage
1. `chany010713@gmail.com`
- recommended state: `@GTD/Reference`
- reason: repeated self-sent micro-messages, no action queue value, mostly a single searchable note cluster

## practical guidance
- Do not split this batch into 100 separate work items.
- Treat it as one repeated self-sent reference cluster.
- If the same pattern continues in later batches, keep collapsing by sender+subject, not by message count.
- This is a `Reference` cluster, not `Action` or `Waiting`.
- No evidence here suggests a `Read` bucket is needed; retention/search is the main value.

## dedupe notes
- `chany010713@gmail.com` self-sent repeats should be deduped at triage time.
- The display-name variation (`"주용김"` vs plain address) is not a separate sender bucket.
- Subject variance (`삼겹살` vs `삼겹살 600g`) should still remain in the same self-reference cluster.

## conclusion
- This batch is overwhelmingly `@GTD/Reference`.
- It is a strong example of why the manual-review flow should compress repeated self-mail into one thread-level reference bucket rather than item-by-item handling.
