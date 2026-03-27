# manual review batch200_24 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_24_20260324.json`
- selection rule:
  - `has:nouserlabels`

## batch-level summary
- total messages: `200`
- dominant shapes:
  - account activation / verification
  - shopping / promo notifications
  - service / trial notices
  - security / password reset
- `Action` is present only in a few setup/recovery threads.

## recommended triage by dominant pattern
### 1) account / verification / setup cluster
- recommended state: `@SYS/Security`
- use this for login, verification, password reset, and account activation mail.

#### dominant sender patterns
- `hatchful@email.shopify.com`
  - `15 messages`
  - brand asset / setup flow
- `elearning@able-edu.or.kr`
  - `11 messages`
  - email verification family
- `noreply@disqus.com`
  - `11 messages`
  - email verification / installation family
- `account_noreply@navercorp.com`
  - login alert family
- `account-update@amazon.com`
  - account data access attempt
- `sec.store@samsung.com`
  - account dormancy notice
- `sa.noreply@samsung-mail.com`
  - account privacy / dormancy notice
- `msonlineservicesteam@microsoftonline.com`
  - password reset notice
- `support_kmooc@nile.or.kr`
  - password reset
- `hotline@ebs.co.kr`
  - password reset verification code
- `noreply@mate-914f3.firebaseapp.com`
  - password reset / verification
- `analytics-noreply@google.com`
  - analytics onboarding

#### practical guidance
- Collapse repeated verification mail into event-level threads.
- Use `@SYS/Security` unless the message is asking for a human follow-up.

### 2) shopping / promo cluster
- recommended state: `@GTD/Read`
- use this for shopping promos, price drops, cart reminders, and purchase-interest mail.

#### dominant sender patterns
- `buyer-info5.g@mail.aliexpress.com`
- `buyer-notice3.g@mail.aliexpress.com`
- `buyer-notice.g@mail.aliexpress.com`
- `buyer-notice6.g@mail.aliexpress.com`
- `ae.buyer.notice.oth@mail.aliexpress.com`
- `ae.buyer.info.other@mail.aliexpress.com`
- `ae.buyer.notice.other@mail.aliexpress.com`
- `transaction@notice.aliexpress.com`
- `do_not_reply@email.gog.com`
- `news@updates.ubisoft.com`
- `newsletter@homify.com`
- `marketing@twitch.tv`
- `newsletter@deals.banggood.com`
- `storyboard-that@storyboardthat.com`
- `team@news.gather.town`

#### practical guidance
- These are reading-only unless a purchase decision or refund dispute exists.
- Collapse by sender family and campaign type.

### 3) service / trial / platform cluster
- recommended state: `@GTD/Reference`
- use this for trials, community notifications, platform setup, and informational service mail.

#### dominant sender patterns
- `support@oopy.io`
  - email verification
- `support@crisp.chat`
  - trial / setup mail
- `noreply@tripwireinteractive.com`
  - game launch / announcement family
- `hello@super.so`
  - site setup / welcome
- `publisher-success+cio@success.disqus.com`
  - installation / setup action
- `no-reply@yanadoocorp.com`
  - email verification
- `no-reply@lpoint.com`
  - service terms notice
- `notification@disquiet.io`
  - product/community notifications
- `contact@lindale.io`
  - product update / info

#### practical guidance
- These are mostly informational and can stay as `@GTD/Reference`.
- Use `@GTD/Action` only for actual installation/setup follow-up threads.

### 4) finance / billing cluster
- recommended state: `@GTD/Reference`
- use `@GTD/Action` only for disputes or unresolved payment tasks.

#### dominant sender patterns
- `paypal@mail.paypal.com`
  - reward / expiry notices
- `easypay_noreturn@kicc.co.kr`
  - card payment / cancellation statements
- `info@upbit.com`
  - finance/account notice
- `return@crm.interpark.com`
  - policy / billing / service changes
- `cyberman@bill.kbcard.com`
  - card statement family
- `starbucks@starbucks.co.kr`
  - card policy notice

#### practical guidance
- Keep statements and payment confirmations in `@GTD/Reference`.
- Escalate only unresolved disputes or cancellations to `@GTD/Action`.

### 5) security / login alerts
- recommended state: `@SYS/Security`
- use this for login, password reset, verification, and access alerts.

#### dominant sender patterns
- `account_noreply@navercorp.com`
  - login alert family
- `account-update@amazon.com`
  - account data access attempt
- `hotline@ebs.co.kr`
  - password reset code
- `msonlineservicesteam@microsoftonline.com`
  - password reset
- `sec.store@samsung.com`
  - account dormancy alert
- `sa.noreply@samsung-mail.com`
  - security/privacy alert

#### practical guidance
- Security alerts should not be mixed with `@GTD/Action` unless a recovery step is pending.
- Dedupe by login/reset event.

## dedupe notes
- Account verification / setup mail should be deduped by event and service family.
- Shopping promos should be deduped by campaign family, not per message.
- Service/trial notices should be deduped by sender family.
- Security alerts should be deduped by login/reset event.
- Only a few `Action` threads exist; do not promote bulk sender families to automatic action rules.

## operational recommendation
- Use `@SYS/Security` for verification, password reset, and access alerts.
- Use `@GTD/Read` for shopping promos and campaign mail.
- Use `@GTD/Reference` for service notices, trials, and finance statements.
- Use `@GTD/Action` only for explicit install/setup or unresolved dispute threads.
