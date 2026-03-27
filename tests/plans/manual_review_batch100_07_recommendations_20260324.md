# manual review batch100_07 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_07_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## batch shape
- total messages: `100`
- batch query:
  - `mixed manual residual / cnu / self`
- dominant sender clusters:
  - `chany010713@gmail.com`: `39`
  - `"주용김" <chany010713@gmail.com>`: `5`
  - `"김주용" <chany010713@gmail.com>`: `2`
  - `chany010713@g.cnu.ac.kr`: `1`
  - `"네이버" <help@help.naver.com>`: `8`
  - `"충남대학교 인권센터" <humanrights@cnu.ac.kr>`: `7`
  - `DongWook Jung <zolaist@gmail.com>`: `4`
  - `Nicole S <nicoleshiosaki@gmail.com>`: `4`
  - `"정창영" <chaeroo@gmail.com>`: `4`
  - multiple `cnu.ac.kr` institutional senders at `1-2` each
- dominant subjects:
  - `안녕하세요`: `39`
  - `(메일)`: `6`
  - `삼겹살 600g`: `5`
  - security/authentication one-time codes: `8`
  - `과학`: `2`
- thread pattern:
  - only `2` true multi-message Gmail threads in this slice
  - everything else is either a self-thread repeat or a one-off institutional/personal message

## recommended triage
1. `chany010713@gmail.com`
- recommended state: `@GTD/Reference`
- reason: repeated self-sent note cluster; should be deduped into one searchable reference bucket

2. `help@help.naver.com`
- recommended state: `@GTD/Read`
- reason: one-time authentication / verification code traffic; read-and-discard behavior is appropriate unless a related account issue is still open

3. `humanrights@cnu.ac.kr`
- recommended state: `@GTD/Reference`
- reason: institutional notice / record-bearing mail; archive value is higher than action value unless the subject explicitly requests a reply

4. `huss@cnu.ac.kr`, `janghak@cnu.ac.kr`, `alma@cnu.ac.kr`, `suk.w.han@cnu.ac.kr`, `fric@cnu.ac.kr`, `student@cnu.ac.kr`, `cnuscc@cnu.ac.kr`
- recommended state: `@GTD/Reference`
- reason: school/admin/reference mail cluster, typically searchable rather than actionable

5. `DongWook Jung <zolaist@gmail.com>`, `Nicole S <nicoleshiosaki@gmail.com>`, `정창영 <chaeroo@gmail.com>`
- recommended state: `@GTD/Action` or `@GTD/Waiting` depending on the thread
- reason: personal/academic exchange with unresolved back-and-forth is more likely than passive reference

6. `최민규 <chwi1192@naver.com>` thread with subject `과학`
- recommended state: `@GTD/Waiting`
- reason: the only non-self multi-message thread in this slice; treat it as a live thread until the thread goal is clearly closed

## practical guidance
- Do not split the self-sent cluster into 100 separate work items.
- Collapse repeated self-mail by sender+subject first, then by thread.
- Treat security/auth codes as `Read` unless they are part of an active account recovery or access issue.
- Treat CNU admin mail as `Reference` by default unless the subject explicitly asks for a response.
- Keep personal/academic back-and-forth in `Action` or `Waiting`, not `Reference`, when the thread is still live.

## dedupe notes
- `chany010713@gmail.com` appears under multiple display names:
  - `chany010713@gmail.com`
  - `"주용김" <chany010713@gmail.com>`
  - `"김주용" <chany010713@gmail.com>`
- Those are not separate triage buckets.
- Subject variants such as `안녕하세요`, `삼겹살 600g`, and `삼겹살` should remain in the same self-reference family if they are still self-sent note traffic.
- The `help@help.naver.com` verification-code pair is a true duplicate thread and should be collapsed at thread level.

## conclusion
- This batch is dominated by self-reference mail and institutional reference mail.
- The practical split is:
  - `@GTD/Reference` for self notes and CNU/admin records
  - `@GTD/Read` for one-time auth codes
  - `@GTD/Waiting` for the live personal thread with unresolved back-and-forth
- Thread-level dedupe matters more than message-level classification for this batch.
