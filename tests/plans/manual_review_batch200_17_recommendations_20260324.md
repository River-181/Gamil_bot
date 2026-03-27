# manual review batch200_17 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_17_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## batch shape
- total messages: `200`
- batch query:
  - `has:nouserlabels`
- dominant sender families:
  - `ScienceDaily <sciencedaily@substack.com>` and variants: `45`
  - `AliExpress <transaction@notice.aliexpress.com>` and `notice@info.aliexpress.com`: `10`
  - `"네이버" <account_noreply@navercorp.com>` and `naverpayadmin_noreply@navercorp.com`: `12`
  - `KB국민카드` billing / statement traffic: `8`
  - `Agoda` / hostel booking traffic: `10`
  - `Miles & More`, `Gumroad`, `Akiflow`, `Aspyr`, `Google Gemini`, `Canva`, `Paddle`, `Clipto`, `LinkedIn`, `Strava`, `Notion VIP`, `KBS`, `KEPCO`, `KT moving`, `SNCF`, `Fast Retailing`
- dominant subjects:
  - `새로운 환경에서 로그인 되었습니다.`
  - `Reply from SSH Lk hostel || Booking ID: ...`
  - `1109663893661132 주문 건: ...`
  - `ktmoving 주소변경서비스 결과 메일 입니다.`
  - `한전:ON 인증번호 확인.`
  - `Email OTP`
  - `판매자가 메시지를 보냈습니다.`
  - `노화심리학_3조_독서 토론 리딩`
- thread pattern:
  - `4` duplicate-message threads in the slice
  - the main pressure is newsletter/notification traffic, not live action-heavy mail

## recommended triage
1. `sciencedaily@substack.com` and subject variants
- recommended state: `@GTD/Read`
- reason: newsletter family; read/consume or archive, not action-heavy

2. `account_noreply@navercorp.com`, `naverpayadmin_noreply@navercorp.com`
- recommended state: `@GTD/Read`
- reason: login / account / payment notifications are one-time review material

3. `notifications@agoda-messaging.com`
- recommended state: `@GTD/Waiting`
- reason: booking reply / trip coordination thread; keep live if travel is still open, otherwise downgrade to `@GTD/Reference`

4. `transaction@notice.aliexpress.com`, `no-reply@agoda.com`, `no-reply@email.hostelworld.com`, `mail@mailing.milesandmore.com`
- recommended state: `@GTD/Reference`
- reason: purchase / delivery / travel confirmation traffic is best kept as searchable records

5. `kbinfo@kbmail.kbcard.com`, `cyberman@bill.kbcard.com`, `service@intl.paypal.com`, `return@ktmoving.com`, `cyber_info@kepco.co.kr`, `monidentifiant.sncf`, `newsletter@your.lufthansa-group.com`, `noreply@mail.fastretailing.com`
- recommended state: `@GTD/Reference`
- reason: billing, account, transport, logistics, and merchant updates are record-oriented

6. `comments-noreply@docs.google.com`, `no-reply@canva.com`, `automatic-notifications+recovery@paddle.com`, `hello@clipto.com`, `ahoy@notion.vip`, `support@akiflow.com`, `google-gemini-noreply@google.com`, `team@email2.anthropic.com`, `news@aspyr.email`, `miricanvas@miridih.com`, `news@aspyr.email`, `news@aspyr.email`
- recommended state: `@GTD/Reference`
- reason: product updates, comments, copy confirmations, trials, and onboarding notices are reference-first unless they explicitly ask for a reply

7. `happykbs@kbs.co.kr`, `i.love.kbs@kbs.co.kr`
- recommended state: `@GTD/Read`
- reason: broadcast / notice / survey style content; generally read and archive

8. `chwi1192@naver.com` and similar personal thread mail
- recommended state: `@GTD/Waiting`
- reason: if the thread is still open or needs a reply, keep it live; otherwise fall back to `@GTD/Reference`

9. `chany010713@gmail.com` manual residual repeats
- recommended state: `@GTD/Reference`
- reason: self-thread / self-note traffic should be deduped and not treated as independent work items

## practical guidance
- Do not add new `@AUTO/*` sender rules from this batch alone.
- Collapse `ScienceDaily` by newsletter family, not by individual issue.
- Collapse Naver login/security messages by thread.
- Keep Agoda/hostel booking mail live only if the trip is still active.
- Treat merchant/account notices as `Reference` unless they explicitly require a response.
- Treat broadcast/newsletter content as `Read` unless the content is intentionally being archived as a note.

## dedupe notes
- The `Naver` login/security notices are duplicate thread families and should be collapsed at thread level.
- The `Agoda` / hostel booking thread also repeats and should be treated as one live booking thread.
- `ScienceDaily` has many sender variants but is one newsletter family.
- Same sender + same subject should not be counted as separate triage items when the message is only a notification or reminder.

## conclusion
- This batch is dominated by `@GTD/Read` and `@GTD/Reference`, with one main `@GTD/Waiting` family for booking coordination.
- There is no strong `Action` cluster here.
- Thread-level dedupe is the main throughput lever for this batch.
