# manual review batch200_31 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_31_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/manual_work_residual_policy_v1.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## batch shape
- total:
  - `200 messages`
  - `190 threads`
- unique senders:
  - `80`
- interpretation:
  - long-tail but clustered around security, newsletters, games/rewards, and commerce notices
  - triage should be thread-first, not message-first

## dominant patterns

### 1) Security / verification / login cluster
- sender family:
  - `i-pin@koreacb.com`
  - `account_noreply@navercorp.com`
  - `no-reply@riotgames.co.kr`
  - `msonlineservicesteam@microsoftonline.com`
  - `account@twitch.tv`
  - `noreply@blizzard.com`
  - `help@accts.epicgames.com`
  - `help@fliphtml5.com`
  - `info@samsunghealth.com`
  - `sendalarm2@alba.co.kr`
- common subjects:
  - `새로운 환경에서 로그인 되었습니다.`
  - `이메일 인증번호가 도착하였습니다`
  - `회원님의 아이핀 인증처리가 되었습니다.`
  - `계정 이메일 인증 코드`
  - `로그인 인증번호`
  - `개인정보 분리보관 안내`
- recommended state:
  - `@GTD/Action` on first review
  - downgrade to `@GTD/Reference` after verification
- reason:
  - account/security burst is the only part that deserves immediate review
  - keep only one thread-level record after confirmation

### 2) Games / rewards / promo cluster
- sender family:
  - `do_not_reply@email.gog.com`
  - `store@mail.epicgames.com`
  - `news@updates.ubisoft.com`
  - `noreply@tripwireinteractive.com`
  - `noreply@discord.com`
  - `storyboard-that@storyboardthat.com`
  - `newsletter@homify.com`
  - `newsletter@gnu.kr`
  - `newsletter@jinhak.com`
  - `newsletter@manycam.com`
  - `newsletter@e.faithgateway.com`
- common subjects:
  - wishlist discounts / free games / special offers
  - `Items on your wishlist are now discounted!`
  - `무료 게임 및 특별 혜택`
  - `새로운 환경에서 로그인 되었습니다.`
  - `NEW LESSON PLANS`
  - `1 Month for Just $1!`
- recommended state:
  - `@GTD/Read`
  - `@GTD/Reference` only if you want to keep the message as a record
- reason:
  - mostly newsletter/promo/reward traffic
  - no task should be created unless a reply or signup is still required

### 3) Commerce / order / payment / notice cluster
- sender family:
  - `paypal@mail.paypal.com`
  - `order@interpark.com`
  - `webzeb@kosaf.go.kr`
  - `noreply@blizzard.com`
  - `customer@...?`
  - `cnu2@icerti.co.kr`
  - `no_reply@homify.com`
  - `info@samsunghealth.com`
  - `sendalarm2@alba.co.kr`
- common subjects:
  - `결제하신 내역을 안내드립니다`
  - `회원가입을 환영합니다`
  - `예매가 완료 되었습니다`
  - `통합포인트 소멸 예정`
  - `거래중지 예고`
  - `개인정보 분리보관 안내`
- recommended state:
  - `@GTD/Reference`
  - `@GTD/Action` only when missing payment / cancellation / follow-up is still needed
- reason:
  - record-heavy, not task-heavy
  - promotion-like notices should not create a new workflow

### 4) Academic / public / service notice cluster
- sender family:
  - `kostatin@korea.kr`
  - `webzeb@kosaf.go.kr`
  - `cnu2@icerti.co.kr`
  - `borisu2001@hanmail.net`
  - `maily-welcome@maily.so`
  - `noreply@coupang.com`
- common subjects:
  - policy / newsletter / certification / public notice
  - `웹진 발행 안내`
  - `재학증명서`
  - `개인정보처리방침 개정안내`
- recommended state:
  - `@GTD/Reference`
  - `@GTD/Read` for pure announcement-style mail
  - `@GTD/Waiting` only if a reply or submission is pending
- reason:
  - mostly notices and records
  - repeated messages should collapse into one thread state

## secondary patterns

- `aa01053208720@gmail.com`
  - travel planning
  - recommend `@GTD/Action`

- `hoam518@gmail.com`
  - course / backup / reply thread
  - recommend `@GTD/Waiting`

- `minjugim655@gmail.com`
  - project mentoring paperwork
  - recommend `@GTD/Waiting`

- `dptmf702@gmail.com`
  - grade / reply thread
  - recommend `@GTD/Waiting`

- `mimo4am@gmail.com`
  - score announcement
  - recommend `@GTD/Read`

- `outlook_7A89390CA06E025E@outlook.com`
  - offline meeting
  - recommend `@GTD/Action`

- `cnu2@icerti.co.kr`
  - certificate delivery
  - recommend `@GTD/Reference`

## dedupe notes

- This batch is long-tail: 80 senders over 190 threads.
- Thread-level dedupe is mandatory; message count overstates the work.
- Security/login senders should be reviewed once, then downgraded after verification.
- Newsletter/promo/game reward mail should stay out of Action unless a reply or signup is actually required.
- Do not add new auto-label rules from this batch; it is best handled as manual triage plus read/reference cleanup.

## practical triage guidance

1. Mark security/login/verification mail as `@GTD/Action` only once per thread, then downgrade.
2. Put games/rewards/newsletters in `@GTD/Read`.
3. Keep commerce/order/public notices in `@GTD/Reference`.
4. Use `@GTD/Waiting` for academic/admin/reply threads that are still open.
5. Process by thread, not by message.
