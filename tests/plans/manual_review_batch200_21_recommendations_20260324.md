# manual review batch200_21 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_21_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/manual_work_residual_policy_v1.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## batch shape
- total:
  - `200 messages`
  - `194 threads`
- unique senders:
  - `70`
- interpretation:
  - mostly long-tail notices, memberships, and account/policy mail
  - triage should be thread-first, not message-first

## dominant patterns

### 1) Membership / community / content feed cluster
- sender family:
  - `leeum.membership@samsung.com`
  - `community@figma.com`
  - `notification@disquiet.io`
  - `hello@typed.do`
  - `hello@super.so`
  - `support@comicstack.io`
  - `storyboard-that@storyboardthat.com`
  - `help@fliphtml5.com`
- common subjects:
  - exhibition / event / community invites
  - product/community announcements
  - `Items on your wishlist are now discounted!`
  - `The upside of downtime`
  - `Introduce / launch / free plan policy` style mail
- recommended state:
  - `@GTD/Read`
  - `@GTD/Reference` only if you want to keep the announcement as a record
- reason:
  - mostly feed/newsletter/community traffic
  - no task should be created unless a reply or signup is still required

### 2) Security / account / verification cluster
- sender family:
  - `account_noreply@navercorp.com`
  - `noreply@coupang.com`
  - `support_kmooc@nile.or.kr`
  - `webmaster@ums.nonghyup.com`
  - `maily-welcome@maily.so`
  - `homepage@lguplus.co.kr`
  - `no-reply@cafe24shop.com`
  - `no-reply@email.gog.com`
  - `do_not_reply@email.gog.com`
- common subjects:
  - `새로운 환경에서 로그인 되었습니다.`
  - `비밀번호가 변경되었습니다.`
  - `인증번호를 입력해주세요`
  - `회원가입을 축하 드립니다.`
  - `전자금융 장기 미사용자에 대한 거래중지 예고`
- recommended state:
  - `@GTD/Action` on first review
  - downgrade to `@GTD/Reference` after verification
- reason:
  - account/security burst is the only part that deserves immediate review
  - keep only one thread-level record after confirmation

### 3) Official / policy / public notice cluster
- sender family:
  - `kostatin@korea.kr`
  - `noreply-maps-issues@google.com`
  - `replies@oracle-mail.com`
  - `noreply@tripwireinteractive.com`
  - `noreply@email.github.com`
  - `notifications@github.com`
  - `noreply@kyobobook.co.kr`
- common subjects:
  - policy mail
  - map / issue / platform notice
  - vendor announcements
  - account-policy reminders
- recommended state:
  - `@GTD/Reference`
  - `@GTD/Read` for announcement-style mail
  - `@GTD/Action` only for explicit password reset / reply-required threads
- reason:
  - most are notices, not tasks
  - repeated messages should collapse into one thread state

### 4) Commerce / order / shipping / payment cluster
- sender family:
  - `easypay_noreturn@kicc.co.kr`
  - `shipping_notification_kr@orders.apple.com`
  - `noreply@agoda.com`
  - `no-reply@sender.skyscanner.com`
  - `newsletter@news.omio.com`
  - `promocioncomercial@aena.online`
  - `toktok@info.glovoapp.com`
  - `noreply@uber.com`
  - `brb@blueribbonbags.com`
  - `kr_flt_noreply@trip.com`
- common subjects:
  - delivery / booking / payment / rating prompts
  - `현재 배송 중입니다.`
  - `결제 완료 안내`
  - `Save up to 18% by rating your stay`
- recommended state:
  - `@GTD/Reference`
  - `@GTD/Action` only when something is missing, canceled, or needs follow-up
- reason:
  - record-heavy, not task-heavy
  - promotion-like travel mail should not create a new workflow

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

- This batch is long-tail: 70 senders over 194 threads.
- `leeum.membership@samsung.com` is a multi-thread membership feed; keep one state per thread.
- `account_noreply@navercorp.com`, `noreply@coupang.com`, `support_kmooc@nile.or.kr`, `webmaster@ums.nonghyup.com`, and `maily-welcome@maily.so` should be reviewed once, then downgraded after verification.
- `noreply@email.github.com` and `notifications@github.com` belong to the same operational notice family; do not split them into separate task buckets if the thread intent is the same.
- Thread-level dedupe is mandatory; message count overstates the work.
- Do not add new auto-label rules from this batch; it is best handled as manual triage plus read/reference cleanup.

## practical triage guidance

1. Put membership/community feed mail in `@GTD/Read` first.
2. Handle login/password/verification mail in `@GTD/Action` only once per thread, then downgrade.
3. Keep policy, platform, and commerce notices in `@GTD/Reference`.
4. Use `@GTD/Waiting` for course/admin/reply threads that are still open.
5. Process by thread, not by message.
