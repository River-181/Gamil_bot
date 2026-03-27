# manual review batch200_22 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_22_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## batch shape
- total messages: `200`
- batch query:
  - `has:nouserlabels`
- dominant sender families:
  - `Disquiet <stevekwon@disquiet.io>`: `60`
  - `Parallels <noreply@parallels.com>`: `11`
  - `Zapier <learn@send.zapier.com>`: `10`
  - `AliExpress <mail.aliexpress.com>`: `15`
  - `Naver` account / pay notifications: `7`
  - `Adobe Creative Cloud for Students`: `6`
  - `Gumroad`, `Super`, `Tripwire`, `GOG`, `Samsung membership`, `LEEUM`, `Facebook`, `Evernote`, `Google Docs comments`, `KOSAF`, `Payple`, `Event-us`, `Sleep Cycle`
- dominant subjects:
  - `실험심리학_보고서3_초안`
  - `인식할 수 없는 웹 브라우저에서 Parallels 계정 액세스 확인`
  - `인식할 수 없는 모바일 장치에서 Parallels 계정 액세스 확인`
  - `Parallels Access 시작하기`
  - `새로운 환경에서 로그인 되었습니다.`
  - `1109663893661132 주문 건: ...`
  - `판매자가 메시지를 보냈습니다.`
  - `우피 Oopy에서 결제한 내역입니다.`
- thread pattern:
  - Parallels has multiple duplicate-message threads
  - AliExpress has duplicate purchase/shipping threads
  - Google Docs comments are multi-message live review threads
  - the rest is mostly newsletter, account, or notification traffic

## recommended triage
1. `stevekwon@disquiet.io`
- recommended state: `@GTD/Read`
- reason: newsletter / content feed traffic; consume or archive, no live action pressure

2. `noreply@parallels.com`, `cs@cleverbridge.com`
- recommended state: `@GTD/Reference`
- reason: account access checks and billing/auth notices are record-first

3. `learn@send.zapier.com`, `news@gather.town`, `mail@email.adobe.com`, `news@aspyr.email`, `team@comms.evernote.com`, `hello@super.so`
- recommended state: `@GTD/Read`
- reason: product/newsletter traffic; read if needed, otherwise archive

4. `mail.aliexpress.com`, `notice@info.aliexpress.com`, `no-reply@agoda.com`, `notifications@agoda-messaging.com`
- recommended state: `@GTD/Reference`
- reason: purchase/shipping/travel confirmation traffic is searchable record material

5. `comments-noreply@docs.google.com`
- recommended state: `@GTD/Waiting`
- reason: active document review loops should stay live until the review thread is closed

6. `account_noreply@navercorp.com`, `naverpayadmin_noreply@navercorp.com`, `kbinfo@kbmail.kbcard.com`, `cyberman@bill.kbcard.com`, `service@intl.paypal.com`, `help@payple.kr`
- recommended state: `@GTD/Reference`
- reason: account, billing, payment, and security notices are lookup material

7. `humanrights@cnu.ac.kr`, `huss@cnu.ac.kr`, `janghak@cnu.ac.kr`, `alma@cnu.ac.kr`, `fric@cnu.ac.kr`, `student@cnu.ac.kr`, `cnuscc@cnu.ac.kr`, `science@kosaf.go.kr`
- recommended state: `@GTD/Reference`
- reason: institutional/admin notices are searchable records unless a reply is explicitly needed

8. `chany010713@gmail.com`
- recommended state: `@GTD/Reference`
- reason: self-sent/manual residual traffic should be deduped by sender+subject and collapsed into one reference cluster

9. `chwi1192@naver.com`
- recommended state: `@GTD/Waiting`
- reason: if the exchange is still open, keep the thread live; otherwise downgrade to `@GTD/Reference`

## practical guidance
- Do not add new `@AUTO/*` sender rules from this batch alone.
- Collapse Parallels by thread, not by individual warning email.
- Collapse AliExpress by order/subject family, not by message count.
- Keep Google Docs comments as one live review thread per document.
- Treat newsletter and product-update traffic as `Read` unless it clearly carries a pending follow-up.
- Treat billing/account/security notices as `Reference`.

## dedupe notes
- Parallels has repeated thread families:
  - browser access verification
  - mobile device access verification
  - access-start / activation
  - billing authenticity notice
- AliExpress has repeated shipping / promo / cart-style notifications and should be grouped by order or subject family.
- Google Docs comment messages should be collapsed to one thread per document.
- `stevekwon@disquiet.io` should not be broken into individual messages; it is a single newsletter family.

## conclusion
- This batch is dominated by `@GTD/Read` and `@GTD/Reference`.
- `@GTD/Waiting` is limited to live collaboration threads like Google Docs comments or open personal threads.
- There is no strong `Action` cluster here.
- Thread-level dedupe is the main throughput lever for this batch.
