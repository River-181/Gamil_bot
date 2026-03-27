# manual review batch100-10 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_10_20260324.json`
- query:
  - `has:nouserlabels from:chany010713@gmail.com`
- count:
  - `100`

## dominant patterns
- This batch is a self-sent / self-thread heavy slice.
- The sample begins with `SENT` items from `chany010713@gmail.com`, which means this batch is not an external triage queue.
- Subjects are mostly self-authored draft, note, file, and study/work thread names rather than incoming requests.
- Repeated patterns appear across:
  - draft-like self subjects
  - study / paper / note titles
  - file rename / revise style messages
  - local reminder / memo style messages

## recommended triage
### `@GTD/Reference`
- default for the batch
- use this for self-sent drafts, notes, exported text, file delivery, and record-keeping mail
- treat repeated self subjects as a single thread-level record

### `@GTD/Read`
- only if a self-sent thread is clearly informational and can be closed without follow-up
- use sparingly; most of this batch should not be split into many `Read` items

### `@GTD/Action`
- reserve only for self-sent messages that clearly represent an outstanding task item, not a note
- do not promote routine self drafts to `Action`

### `@GTD/Waiting`
- generally not expected in this batch
- only use when the self thread is explicitly waiting on an external reply or result

## dedupe notes
- Deduplicate by thread, not by message.
- If the same self subject appears multiple times, keep one `Reference` decision for the thread.
- The leading sample already shows `SENT` status, so message-count inflation should not be treated as 100 separate triage decisions.
- For Step A accounting, this batch should mostly count as self-thread `Reference`, with a small possible tail of `Read`.

## application notes
- This batch should be processed as a mostly-`Reference` self-thread block.
- If a later pass shows a few externally actionable replies inside the same sender family, split those exceptions only after thread grouping.
- This slice is best handled as a cleanup/archive-oriented manual review batch rather than a live action queue.
