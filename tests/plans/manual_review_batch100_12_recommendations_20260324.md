# manual review batch100_12 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_12_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## batch shape
- total messages: `100`
- batch query:
  - `has:nouserlabels`
- dominant sender clusters:
  - `hello@linkingyourthinking.com` and Nick Milo newsletter traffic
  - `help@help.naver.com` auth / security traffic
  - `kbinfo@kbmail.kbcard.com` and `cyberman@bill.kbcard.com`
  - `service@intl.paypal.com`
  - `no-reply@canva.com`
  - `automatic-notifications+recovery@paddle.com`
  - `comments-noreply@docs.google.com`
  - multiple `cnu.ac.kr` institutional senders
  - repeated self-sent `chany010713@gmail.com` traffic
- dominant subjects:
  - `안녕하세요`
  - `새로운 환경에서 로그인 되었습니다.`
  - `요청하신 인증번호를 알려드립니다.`
  - `비밀번호가 변경되었습니다.`
  - `[네이버페이] 취소하신 내역을 안내해드립니다.`
  - `Student App Centre Plus (With 7 Day Trial)구매를 완료하세요...`
  - `완료되었습니다! "노화심리학_발표 마무리"이(가) 복사되었습니다`
  - `Welcome to Clipto - Enjoy your 7-Day Free Trial！`
- thread pattern:
  - `4` true multi-message Gmail threads were found
  - the rest is mostly self-mail, institutional reference mail, or one-off notification traffic

## recommended triage
1. `chany010713@gmail.com`
- recommended state: `@GTD/Reference`
- reason: repeated self-sent cluster; dedupe into one searchable reference bucket rather than 100 individual items

2. `help@help.naver.com`
- recommended state: `@GTD/Read`
- reason: login / auth / password / verification notifications are read-and-discard by default unless an active account issue is still open

3. `naverpayadmin_noreply@navercorp.com`, `account_noreply@navercorp.com`
- recommended state: `@GTD/Reference`
- reason: payment/account system notifications are useful as records but usually do not require a follow-up action

4. `kbinfo@kbmail.kbcard.com`, `cyberman@bill.kbcard.com`, `service@intl.paypal.com`
- recommended state: `@GTD/Reference`
- reason: card / billing / payment statements and security notices are retained for lookup, not treated as active tasks

5. `no-reply@canva.com`, `automatic-notifications+recovery@paddle.com`, `hello@clipto.com`
- recommended state: `@GTD/Reference`
- reason: product confirmation / trial / copy-complete / onboarding notifications are reference material unless they contain a pending action

6. `comments-noreply@docs.google.com`
- recommended state: `@GTD/Waiting`
- reason: collaborative document comments usually imply an open review loop; collapse repeated comment messages into one live thread state

7. `humanrights@cnu.ac.kr`, `huss@cnu.ac.kr`, `janghak@cnu.ac.kr`, `alma@cnu.ac.kr`, `suk.w.han@cnu.ac.kr`, `fric@cnu.ac.kr`, `student@cnu.ac.kr`, `cnuscc@cnu.ac.kr`
- recommended state: `@GTD/Reference`
- reason: institutional / admin / school notices are searchable records unless they explicitly request a reply

8. `DongWook Jung <zolaist@gmail.com>`, `Nicole S <nicoleshiosaki@gmail.com>`, `정창영 <chaeroo@gmail.com>`
- recommended state: `@GTD/Action` or `@GTD/Waiting` depending on the thread
- reason: these look like live personal / academic exchanges rather than passive records

9. `최민규 <chwi1192@naver.com>` thread with subject `과학`
- recommended state: `@GTD/Waiting`
- reason: this is the only clearly live non-self thread in the slice and should remain open until the thread goal is closed

## practical guidance
- Do not promote any of these senders into new `@AUTO/*` rules from this batch alone.
- Collapse repeated self-mail by sender+subject first, then by thread.
- Treat security/auth codes as `Read` unless they are part of an active recovery or investigation.
- Treat CNU/admin mail as `Reference` by default.
- Keep personal/academic back-and-forth in `Action` or `Waiting`, not `Reference`, when the thread is still live.

## dedupe notes
- `chany010713@gmail.com` appears under multiple display names:
  - `chany010713@gmail.com`
  - `"주용김" <chany010713@gmail.com>`
  - `"김주용" <chany010713@gmail.com>`
- Those are not separate triage buckets.
- The batch includes 4 duplicate thread pairs that should be collapsed at thread level:
  - `help@help.naver.com` verification / login notices
  - `comments-noreply@docs.google.com` Google Slides comments
  - `no-reply@canva.com` copy-complete notices
  - `automatic-notifications+recovery@paddle.com` trial / purchase notices
- Subject variance should not split the self-thread cluster when the sender and purpose are still the same.

## conclusion
- This batch is mostly `@GTD/Reference`, with a smaller `@GTD/Read` slice for auth / security traffic and a small `@GTD/Waiting` slice for live collaborative threads.
- Thread-level dedupe matters more than message-level classification for this batch.
- The strongest recurring patterns are self-mail, Naver auth, CNU admin, and notification/reference traffic from product senders.
