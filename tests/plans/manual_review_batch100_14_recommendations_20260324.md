# manual review batch100_14 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_14_20260324.json`
- selection rule:
  - `has:nouserlabels`

## batch-level summary
- total messages: `100`
- this batch is a generic residual mix, but the dominant shapes are clear:
  - newsletters / reading digests
  - service / product notifications
  - finance / billing statements
  - security / login alerts
- there is no strong self-thread cluster in this batch.

## recommended triage by dominant pattern
### 1) reading / newsletter cluster
- recommended state: `@GTD/Read`
- use this for items that are clearly intended for reading rather than action.

#### dominant sender patterns
- `sciencedaily@substack.com`
  - `14 messages`
  - examples:
    - `ScienceDaily: All - March 22, 2025`
    - `ScienceDaily: All - March 21, 2025`
    - `ScienceDaily: All - March 20, 2025`
    - `ScienceDaily: All - March 19, 2025`
- `glasp@substack.com`
  - `6 messages`
  - examples:
    - `You’re unsubscribed.`
    - `How to Thrive in Change and Uncover Your Core Value | Jason Feifer | Glasp Talk #44`
- `hello@email.freedom.to`
  - `2 messages`
  - examples:
    - `How to Form a Habit (That Actually Lasts)`
    - `How to Make Morning Routines a Habit`
- `emails@britishmuseum.org`
  - `2 messages`
  - examples:
    - `Final weeks | Picasso exhibition 🎨`
    - `New exhibition | Ancient India: living traditions ✨🌸`
- `hello@linkingyourthinking.com`
  - `1 message`
  - example:
    - `Ideaverse Pro 2.0 launches April 16th`
- `oliver@scholarcy.com`
  - `2 messages`
  - examples:
    - `Enjoy 25% off Scholarcy today`
    - `How Omar achieved his postgrad vision with the help of Scholarcy`

#### practical guidance
- These are reading items, not work items.
- Collapse by sender family, not by individual message.
- If you want to keep the inbox lighter, `@GTD/Read` is the right default.

### 2) service / product notification cluster
- recommended state: `@GTD/Reference`
- use this for account notices, product updates, trial expirations, and informational service mail.

#### dominant sender patterns
- `learn@email1.asana.com`
  - `6 messages`
  - example:
    - `⏰ 아직 Asana로 돌아갈 수 있어요`
- `via@viacharacter.org`
  - `4 messages`
  - examples:
    - `Your Kit for Success 🏆`
    - `Reset your VIA password`
    - `A letter from the VIA Team`
- `ant@supabase.com`
  - `3 messages`
  - examples:
    - product/account update style mail
- `no-reply@everytime.kr`
  - `3 messages`
  - example:
    - `[에브리타임] 새로운 기기(브라우저)에서 로그인 되었습니다.`
- `no-reply@mail.threads.net`
  - `2 messages`
  - example:
    - `choi.openai recently posted on Threads`
- `no-reply@community.gpters.org`
  - `2 messages`
- `workspace-noreply@google.com`
  - `2 messages`
  - example:
    - `cnu-psy-stu.notion.site의 Google Workspace Business Standard 평가판 사용 기간이 종료됨`
- `noreply@email.openai.com`
  - `1 message`
  - example:
    - `OpenAI o1 and o3-mini API access`
- `announcements@figma.com`
  - `1 message`
  - example:
    - `Ready to level up?`
- `no_reply@yanolja.com`
  - `1 message`
  - example:
    - `서비스 이용 약관 및 개인정보 처리방침 개정 안내`
- `no-reply@hancom.com`
  - `2 messages`
  - example:
    - account / service notice style mail

#### practical guidance
- These are mostly informational and can stay as `@GTD/Reference`.
- If a specific service mail requires a decision, move only that thread to `@GTD/Action`.
- `ViaCharacter` password reset-like items should remain reference unless an account recovery action is pending.

### 3) finance / billing cluster
- recommended state: `@GTD/Reference`
- use `@GTD/Action` only if there is a dispute, cancellation, or follow-up task.

#### dominant sender patterns
- `easypay_noreturn@kicc.co.kr`
  - `4 messages`
  - examples:
    - `김*용님, 쿠팡(주)에서 [신용카드]결제하신 내역입니다.`
    - `김*용님, 쿠팡(주)에서 [신용카드]취소하신 내역입니다.`
- `cyberman@bill.kbcard.com`
  - `2 messages`
  - examples:
    - `(KB국민카드) 김*용님 2025년03월 명세서`
    - `(KB국민카드) 김주용님 2025년02월 KB국민체크카드 내역서`
- `no-reply-accounts@hancom.com`
  - `2 messages`
  - account/billing style notices
- `no-reply@hancom.com`
  - `2 messages`
  - same billing/account family

#### practical guidance
- Finance mail is record-first, not action-first, unless a dispute or pending payment task exists.
- Group by issuer and billing cycle.
- Do not create new automation for one-off statement variants.

### 4) security / login alert cluster
- recommended state: `@SYS/Security`
- use this for account access, password reset, and login-event notifications.

#### dominant sender patterns
- `no-reply@everytime.kr`
  - `3 messages`
  - example:
    - `[에브리타임] 새로운 기기(브라우저)에서 로그인 되었습니다.`
- `via@viacharacter.org`
  - `1 message`
  - example:
    - `Reset your VIA password`

#### practical guidance
- Security alerts should not be mixed into `@GTD/Action` unless there is an explicit recovery step.
- Collapse repeated alerts by event, not by raw message count.

## dedupe notes
- Newsletter senders should be deduped by sender family and issue type.
- Finance senders should be deduped by issuer and billing cycle.
- Security alerts should be deduped by login/reset event.
- This batch does not have a meaningful self-thread pattern.
- No new auto rule should be created for one-off residual senders unless they repeat in a later batch.

## operational recommendation
- Use `@GTD/Read` for reading/newsletter items.
- Use `@GTD/Reference` for service notices and finance statements.
- Use `@SYS/Security` for login and password-reset alerts.
- Escalate to `@GTD/Action` only when a thread requires an explicit decision, reply, or dispute resolution.
