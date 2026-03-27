# manual review batch200_19 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_19_20260324.json`
- selection rule:
  - `has:nouserlabels`

## batch-level summary
- total messages: `200`
- dominant shapes:
  - newsletters / reading digests
  - product / service notifications
  - finance / billing statements
  - account / security alerts
- strong `@GTD/Action` or `@GTD/Waiting` clusters are not dominant in this batch.

## recommended triage by dominant pattern
### 1) reading / newsletter cluster
- recommended state: `@GTD/Read`
- use this for content that is meant to be skimmed or archived after reading.

#### dominant sender patterns
- `kostatin@korea.kr`
  - `17 messages`
  - policy / statistics newsletters
- `kird@kird.re.kr`
  - `9 messages`
  - research / career program announcements
- `mdis@korea.kr`
  - `5 messages`
  - survey / informational notice
- `yyj@korea.kr`
  - `3 messages`
  - survey / participation request
- `dailydevo@biblicaministry.com`
  - reading digest
- `niv@e.harpercollinschristian.com`
  - reading digest
- `noreply@playground.ru`
  - newsletter-style content
- `newsletter@deals.banggood.com`
  - promo/newsletter style content
- `do_not_reply@email.gog.com`
  - discount/newsletter style content
- `storyboard-that@storyboardthat.com`
  - promo/newsletter style content
- `no-reply@email.figma.com`
  - resource/newsletter style content
- `hello@email.freedom.to`
  - habit / reading digest style content
- `oliver@scholarcy.com`
  - reading / learning promo style content

#### practical guidance
- Collapse these by sender family and issue type.
- If there is no action required, prefer `@GTD/Read`.

### 2) service / product notification cluster
- recommended state: `@GTD/Reference`
- use this for informational notices, account updates, trial notices, and tool/service announcements.

#### dominant sender patterns
- `leeum.membership@samsung.com`
  - `13 messages`
  - membership / account notices
- `return@crm.interpark.com`
  - `8 messages`
  - I-Point / policy / service notice family
- `trialsupport@autodeskcommunications.com`
  - `7 messages`
  - trial expiry / product notices
- `account_noreply@navercorp.com`
  - `6 messages`
  - login / account alerts
- `notification@disquiet.io`
  - `4 messages`
  - product/community notifications
- `hyunsolpark@disquiet.io`
  - `3 messages`
  - related notification family
- `contact@lindale.io`
  - `4 messages`
  - informational product mail
- `support@suforyou.net`
  - `3 messages`
  - trial / service notice
- `no-reply@leeumhoam.org`
  - `4 messages`
  - membership expiry / notice
- `no-reply@hancom.com`
  - `2 messages`
  - account/service notice
- `no-reply-accounts@hancom.com`
  - `2 messages`
  - account/service notice
- `export-noreply@mail.notion.so`
  - `2 messages`
  - export ready / file delivery
- `noreply-maps-issues@google.com`
  - `2 messages`
  - issue / map fix notice
- `noreply-cloudshell@google.com`
  - `1 message`
  - cloud shell cleanup notice
- `webmaster@lottecinema.co.kr`
  - `1 message`
  - reservation complete
- `aihub@aihub.kr`
  - `1 message`
  - site update notice
- `no-reply@yanadoocorp.com`
  - `2 messages`
  - email verification / service notice
- `noreply@mate-914f3.firebaseapp.com`
  - `2 messages`
  - password reset / verification family

#### practical guidance
- These are mostly record-keeping or product-status mails.
- Default to `@GTD/Reference`.
- Move to `@GTD/Action` only if the thread requires a decision or follow-up.

### 3) finance / billing cluster
- recommended state: `@GTD/Reference`
- use `@GTD/Action` only for disputes, cancellations, or unresolved payment issues.

#### dominant sender patterns
- `easypay_noreturn@kicc.co.kr`
  - `4 messages`
  - payment / cancellation statements
- `cyberman@bill.kbcard.com`
  - card statement family
- `transaction@notice.aliexpress.com`
  - order/shipping/billing style notices
- `mypresent.ae0@mail.aliexpress.com`
  - discount / purchase campaign
- `mypresent.ae4@mail.aliexpress.com`
  - return / purchase campaign
- `starbucks@starbucks.co.kr`
  - card / policy notice
- `nikecs@inmomentfeedback.com`
  - feedback / account-related notice
- `nike@notifications.nike.com`
  - one-time code / account notice
- `return@crm.interpark.com`
  - finance/service policy changes

#### practical guidance
- Group by issuer and billing cycle.
- For payment confirmations and statements, `@GTD/Reference` is the right default.
- Escalate to `@GTD/Action` only if a dispute or change request is outstanding.

### 4) security / login alert cluster
- recommended state: `@SYS/Security`
- use this for account access, password reset, and login-event notifications.

#### dominant sender patterns
- `account_noreply@navercorp.com`
  - `6 messages`
  - `새로운 환경에서 로그인 되었습니다.`
- `no-reply@everytime.kr`
  - login alert family
- `via@viacharacter.org`
  - password reset / login family
- `noreply@mate-914f3.firebaseapp.com`
  - password reset / verification family
- `nike@notifications.nike.com`
  - one-time code / account verification

#### practical guidance
- Security alerts should not be mixed into `@GTD/Action` unless a recovery step is pending.
- Collapse repeated login/reset notices by event, not by raw message count.

## dedupe notes
- Newsletter families should be deduped by sender family and issue type.
- Product/service notices should be deduped by sender family and account/service scope.
- Finance notices should be deduped by issuer and billing cycle.
- Security notices should be deduped by login/reset event.
- This batch has no meaningful self-thread cluster.
- No new auto rule should be created for singleton residuals unless they repeat in a later batch.

## operational recommendation
- Use `@GTD/Read` for newsletters and reading digests.
- Use `@GTD/Reference` for product notices, exports, reservations, and finance statements.
- Use `@SYS/Security` for login/password-reset/verification alerts.
- Reserve `@GTD/Action` for the small set of threads with explicit follow-up or dispute handling.
