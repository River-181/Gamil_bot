# manual review batch100_08 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_08_20260324.json`
- query:
  - `has:nouserlabels from:chany010713@gmail.com`
- count:
  - `100`

## dominant patterns

### pattern A. self sender note thread family
- dominant sender:
  - `chany010713@gmail.com`
- volume:
  - `100 / 100`
- common subjects:
  - `삼겹살 600g`
  - `삼겹살`
- recommended state:
  - `@GTD/Reference`
- reason:
  - self sender only
  - note-like and fragment-like content
  - no clear action item or external waiting state

## practical triage guidance
1. Treat the entire batch as one self-sender family and default it to `@GTD/Reference`.
2. Do not split these messages into `Action` or `Waiting` unless a future message adds a concrete external request or deadline.
3. Do not promote this pattern into `@AUTO/*`; it is manual/personal residual, not newsletter or promo.

## dedupe notes
- `99 / 100` messages share the same subject family `삼겹살 600g`.
- The remaining message uses the shorter subject `삼겹살`.
- Even though each message is its own thread id, operationally this is one repetitive self-note family and should be counted as a single triage pattern.
- If this sender appears again with the same subject family, collapse it into the existing `Reference` family instead of creating a new rule or a new manual category.

## recommended default state
- `chany010713@gmail.com` -> `@GTD/Reference`

