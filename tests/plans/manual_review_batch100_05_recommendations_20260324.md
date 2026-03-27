# manual review batch100-05 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_05_20260324.json`
- query:
  - `has:nouserlabels from:@cnu.ac.kr`
- count:
  - `30`

## dominant patterns
- This batch is almost entirely CNU institutional mail.
- Recurring sender families dominate the set:
  - `humanrights@cnu.ac.kr`
  - `fric@cnu.ac.kr`
  - `cnuscc@cnu.ac.kr`
  - `janghak@cnu.ac.kr`
  - `huss@cnu.ac.kr`
  - `alma@cnu.ac.kr`
  - `suk.w.han@cnu.ac.kr`
  - `lib6025@cnu.ac.kr`
  - `lib7203@cnu.ac.kr`
  - `cnupr@cnu.ac.kr`
  - `reply@cnu.ac.kr`
  - `cybercnu@cnu.ac.kr`
  - `student@cnu.ac.kr`
  - `pdkim@cnu.ac.kr`
  - `chany010713@g.cnu.ac.kr`

## recommended triage
### `@GTD/Reference`
- `humanrights@cnu.ac.kr`
  - 7 card-news / policy notice items
  - treat as one repeating reference series
- `fric@cnu.ac.kr`
  - journal access / foreign journal notices
- `cnuscc@cnu.ac.kr`
  - social contribution / campaign notices
- `cnupr@cnu.ac.kr`
  - official webzine
- `reply@cnu.ac.kr`
  - generic institutional notice
- `cybercnu@cnu.ac.kr`
  - service outage notice
- `lib6025@cnu.ac.kr`
  - library notice
- `lib7203@cnu.ac.kr`
  - library education notice
- `student@cnu.ac.kr`
  - student office notice when no response is required
- `chany010713@g.cnu.ac.kr`
  - self/calendar-share style notification

### `@GTD/Action`
- `alma@cnu.ac.kr`
  - BK21 forum attendance / confirmation style invites
- `huss@cnu.ac.kr`
  - HUSS lecture / seminar coordination when attendance or confirmation is needed
- `janghak@cnu.ac.kr`
  - scholarship / administrative items when a reply or completion is pending

### `@GTD/Waiting`
- `suk.w.han@cnu.ac.kr`
  - class schedule / class update threads that still expect a response
- `pdkim@cnu.ac.kr`
  - reply thread to an active academic question

## dedupe notes
- Collapse recurring sender-series into one thread-level decision.
- The 7 `humanrights@cnu.ac.kr` items should be treated as one reference series, not 7 separate triage decisions.
- `fric@cnu.ac.kr`, `cnuscc@cnu.ac.kr`, and `janghak@cnu.ac.kr` also repeat as institutional series and should be grouped before applying labels.
- For Step A accounting, count `thread` decisions before `message` count when the sender series repeats.

## application notes
- This batch is safe to process as a mostly-`Reference` pass with a small `Action`/`Waiting` tail.
- Prefer sender-family grouping over message-by-message review when the sender is a recurring CNU office or center.
