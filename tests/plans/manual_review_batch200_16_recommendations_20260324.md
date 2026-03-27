# manual review batch200_16 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_16_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/manual_work_residual_policy_v1.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## batch shape
- total:
  - `200 messages`
  - `192 threads`
- unique senders:
  - `84`
- interpretation:
  - almost all long-tail
  - triage should be thread-first, not message-first

## dominant patterns

### 1) Newsletter / reading queue
- sender family:
  - `sciencedaily@substack.com`
  - `sciencedaily+quirky@substack.com`
  - `sciencedaily+society@substack.com`
  - `sciencedaily+featured@substack.com`
  - `sciencedaily+environment@substack.com`
  - `hello@linkingyourthinking.com`
  - `hello@freedom.to`
  - `drgardener@creators.gumroad.com`
  - `noreply@post.gamsgo.vip`
  - `hello@duolingo.com`
- volume:
  - `major recurring cluster`
- recommended state:
  - `@GTD/Read`
  - `@GTD/Reference` only if you want to keep the issue as a record
- reason:
  - this is mostly newsletter / marketing / reading content
  - no action thread should be created unless the sender is explicitly asking for a reply

### 2) Security / login / password-reset queue
- sender family:
  - `account_noreply@navercorp.com`
  - `no-reply@dropbox.com`
  - `no-reply@everytime.kr`
  - `mtickets-noreply@corethree.net`
  - `uk.visas.and.immigration.home.office@notifications.service.gov.uk`
  - `czmp@csair.com`
  - `workspace-noreply@google.com`
  - `googleaistudio-noreply@google.com`
- common subjects:
  - `새로운 환경에서 로그인 되었습니다.`
  - `Your password reset link`
  - `Your ETA security code`
  - `비밀번호가 변경되었습니다.`
  - `Welcome to Google Workspace. See what you can do.`
- recommended state:
  - `@GTD/Action` on first review
  - downgrade to `@GTD/Reference` after verification
- reason:
  - account/security burst is the only part that deserves immediate review
  - once verified, keep only one thread-level record

### 3) Commerce / travel / fulfillment queue
- sender family:
  - `shipping_notification_kr@orders.apple.com`
  - `easypay_noreturn@kicc.co.kr`
  - `no-reply@agoda.com`
  - `no-reply@sender.skyscanner.com`
  - `newsletter@news.omio.com`
  - `promocioncomercial@aena.online`
  - `toktok@info.glovoapp.com`
  - `noreply@uber.com`
  - `brb@blueribbonbags.com`
  - `kr_flt_noreply@trip.com`
- common subjects:
  - delivery / payment / booking / travel promotions
  - `현재 배송 중입니다.`
  - `결제 완료 안내`
  - `Rate Your Recent Purchase`
  - `Save up to 18% by rating your stay`
- recommended state:
  - `@GTD/Reference`
  - `@GTD/Action` only when a payment, cancellation, or missing delivery needs follow-up
- reason:
  - these are record-heavy, not task-heavy
  - promotion-like travel mail should not create a new workflow

### 4) Platform / collaboration / product notices
- sender family:
  - `comments-noreply@docs.google.com`
  - `team@mail.notion.so`
  - `notify@mail.notion.so`
  - `messages-noreply@linkedin.com`
  - `no-reply@asana.com`
  - `learn@email1.asana.com`
  - `noreply@transactional.n8n.io`
  - `noreply@imweb.me`
  - `helpdesk@jobkorea.co.kr`
  - `office@spacecloud.kr`
  - `noreply@email.openai.com`
  - `help@arc.net`
  - `noreply@steampowered.com`
  - `noreply@kaggle.com`
  - `replies@oracle-mail.com`
  - `no-reply@email.github.com`
  - `notifications@github.com`
  - `noreply@kyobobook.co.kr`
- recommended state:
  - `@GTD/Reference`
  - `@GTD/Read` for announcement-style mail
  - `@GTD/Action` only for password resets or explicit reply-required threads
- reason:
  - most of these are status, update, or platform notices
  - keep only the active thread, not every notification message

## secondary patterns

- `cnu2@icerti.co.kr`
  - certificate delivery
  - recommend `@GTD/Reference`

- `munhyunsu@cs-cnu.org`
  - course/admin reply
  - recommend `@GTD/Waiting`

- `ade26594@gmail.com`
  - experiment participation / document exchange
  - recommend `@GTD/Waiting`

- `dptmf702@gmail.com`
  - grade / reply thread
  - recommend `@GTD/Waiting`

- `aa01053208720@gmail.com`
  - travel planning
  - recommend `@GTD/Action`

- `hoam518@gmail.com`
  - course / backup / reply thread
  - recommend `@GTD/Waiting`

- `minjugim655@gmail.com`
  - project mentoring paperwork
  - recommend `@GTD/Waiting`

- `mimo4am@gmail.com`
  - score announcement
  - recommend `@GTD/Read`

- `outlook_7A89390CA06E025E@outlook.com`
  - offline meeting
  - recommend `@GTD/Action`

## dedupe notes

- This batch is mostly long-tail: 84 senders over 192 threads.
- Thread-level dedupe is mandatory; message count overstates the work.
- Repeated newsletter senders should be collapsed to one `Read` or `Reference` per thread.
- Login/security senders should be reviewed once, then downgraded after verification.
- Do not add new auto-label rules from this batch; it is better handled as manual triage plus read/reference cleanup.

## practical triage guidance

1. Put newsletter-heavy senders in `@GTD/Read` first.
2. Handle security/login/password-reset threads in `@GTD/Action` only once per thread, then downgrade.
3. Keep travel/commerce receipts and platform notices in `@GTD/Reference`.
4. Use `@GTD/Waiting` for course/admin/reply threads that are still open.
5. Process by thread, not by message.
