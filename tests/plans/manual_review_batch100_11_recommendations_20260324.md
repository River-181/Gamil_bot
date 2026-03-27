# manual review batch100_11 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_11_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/manual_work_residual_policy_v1.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## dominant patterns

### 1) Immersed / product notification cluster
- sender:
  - `info@immersed.com`
- volume:
  - `6 messages`
  - `6 threads`
- recommended state:
  - `@GTD/Reference`
- reason:
  - product/notification traffic, not active work
  - keep only one reference state per thread

### 2) Everytime / login-security cluster
- sender:
  - `no-reply@everytime.kr`
- volume:
  - `5 messages`
  - `5 threads`
- common subject:
  - `새로운 기기(브라우저)에서 로그인 되었습니다.`
- recommended state:
  - `@GTD/Action`
- reason:
  - login/security burst should be reviewed once
  - if already verified, downgrade to `@GTD/Reference`

### 3) AI Hub / survey / notice cluster
- sender:
  - `letter@panelpower.net`
- volume:
  - `3 messages`
  - `2 threads`
- common subjects:
  - `[AI허브] AI 허브 이용자 대상 데이터 및 서비스 만족도 설문조사`
  - `[정정] 2025년 AI 허브 활용현황 설문조사 안내(추첨을 통한 소정의 상품 제공)`
- recommended state:
  - `@GTD/Reference`
- reason:
  - survey/notice traffic, useful only as record unless action is still pending

### 4) GitHub / developer notification cluster
- sender:
  - `notifications@github.com`
  - `no-reply@email.github.com`
- volume:
  - `5 messages`
  - `4 threads`
- common subjects:
  - repository / product notification
  - promotional GitHub Universe email
- recommended state:
  - `@GTD/Reference`
  - `@GTD/Read` for promo-style email
- reason:
  - operational notifications should be retained as reference
  - promo-like announcements can be read and closed

### 5) Commerce / billing / service confirmation cluster
- sender:
  - `shop@email.stackcommerce.com`
  - `invoice+statements+acct_15YpNsJAmnYVOvfn@stripe.com`
  - `inimail@inicis.com`
  - `kr_flt_noreply@trip.com`
  - `brb@blueribbonbags.com`
  - `noreply@kyobobook.co.kr`
- volume:
  - repeated but mostly short-lived threads
- common subjects:
  - `Rate Your Recent Purchase`
  - `Your Clipto.AI subscription has been Canceled`
  - `[교보문고] 통합포인트가 소멸될 예정입니다.`
  - `Blue Ribbon Bags - Your Service Confirmation`
  - `[트립닷컴] 결제 완료 안내`
- recommended state:
  - `@GTD/Reference` for receipts, confirmations, and account records
  - `@GTD/Action` only if payment or cancellation still needs follow-up
- reason:
  - these are record-heavy and should not be auto-promoted to action unless a pending task exists

### 6) Identity / account / policy notice cluster
- sender:
  - `noreply@imweb.me`
  - `no-reply@newsletter.socar.kr`
  - `helpdesk@jobkorea.co.kr`
  - `office@spacecloud.kr`
  - `noreply@transactional.n8n.io`
  - `noreply@email.openai.com`
  - `help@arc.net`
  - `noreply@steampowered.com`
  - `noreply@kaggle.com`
  - `replies@oracle-mail.com`
- recommended state:
  - `@GTD/Reference`
  - `@GTD/Action` only for actual password reset / verification / account recovery threads
- reason:
  - these are mostly policy, account, or platform notices
  - one thread should hold one state; do not split repeated notices by message

### 7) Academic / CNU / research / submission cluster
- sender:
  - `cnu2@icerti.co.kr`
  - `munhyunsu@cs-cnu.org`
  - `globaltalent@kird.re.kr`
  - `comments-noreply@docs.google.com`
- recommended state:
  - `@GTD/Reference`
  - `@GTD/Waiting` when a reply or submission is still pending
- reason:
  - this batch is mostly school/research/admin record traffic
  - collaboration comments can stay as reference unless they block an open task

## secondary patterns

- `aa01053208720@gmail.com`
  - `오사카 여행계획`
  - recommend `@GTD/Action`

- `ade26594@gmail.com`
  - `Re: 실험참가 메뉴얼과 서류`
  - recommend `@GTD/Waiting`

- `dptmf702@gmail.com`
  - `Re: 심리통계 1 성적 문의 답변드립니다.`
  - recommend `@GTD/Waiting`

- `hoam518@gmail.com`
  - `Re: 데이터 활용과 문제해결 수강생 김주용`
  - `Fwd: [충남대 디지털 HUSS사업단] ChatGPT 대화내용 백업 관련`
  - recommend `@GTD/Waiting` for active reply threads, `@GTD/Reference` for archived material

- `minjugim655@gmail.com`
  - project mentoring paperwork
  - recommend `@GTD/Waiting`

- `djglocal25@naver.com`
  - one-off coordination / contract thread
  - recommend `@GTD/Action` or `@GTD/Waiting` based on current thread state

- `mimo4am@gmail.com`
  - score announcement
  - recommend `@GTD/Read`

- `oneulst1@naver.com`
  - photo delivery
  - recommend `@GTD/Reference`

- `outlook_7A89390CA06E025E@outlook.com`
  - offline meeting
  - recommend `@GTD/Action`

## dedupe notes

- This batch is highly fragmented: 74 unique senders and 93 unique threads in 100 messages.
- Repeated sender groups should be collapsed by thread, not by message count.
- `help@help.naver.com` is not the dominant cluster here; do not import the batch100_06 Naver-login logic into this batch.
- `no-reply@everytime.kr` is a repeated security thread family; keep one action state per thread and downgrade after verification.
- `notifications@github.com` and `no-reply@email.github.com` should not be split into separate task buckets if they belong to the same operational context.
- Do not create new auto-label rules from this batch; it is mostly manual triage plus a few reference-worthy notices.

## practical triage guidance

1. Mark login/security/account changes as `@GTD/Action` only once per thread, then downgrade to `@GTD/Reference` after verification.
2. Keep receipts, service confirmations, policy notices, and survey mail in `@GTD/Reference`.
3. Use `@GTD/Waiting` for academic/admin threads that are still awaiting a reply or a submission result.
4. Use `@GTD/Read` for one-off announcement or score/result mail that needs no further action.
5. Thread dedupe is the main control mechanism in this batch; message-level counting will overstate the real work.
