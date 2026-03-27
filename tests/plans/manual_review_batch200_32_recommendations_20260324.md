# manual review batch200_32 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_32_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## batch shape
- total messages: `142`
- batch query:
  - `has:nouserlabels`
- dominant sender families:
  - `Storyboard That <storyboard-that@storyboardthat.com>`: `13`
  - `KCB i-PIN` / `아이핀 관리자 <i-pin@koreacb.com>`: `11`
  - `GNU Newsletter <newsletter@gnu.kr>`: `9`
  - `경상대학교 도서관 <auto@gnu.ac.kr>`: `8`
  - `Zoom Video Communications <teamzoom@zoom.us>`: `6`
  - `진학사 <newsletter@jinhak.com>` / `apply@jinhakapply.com`: `7`
  - `GOG.com`, `Evernote`, `Ubisoft`, `ManyCam`, `Apple`, `Samsung`, `NH농협`, `Kyobo`, `Coupang`, `L.POINT`, `PENUP`, `MyScript`
- dominant subjects:
  - `\[KCB 아이핀\] 회원님의 아이핀 인증처리가 되었습니다.`
  - `반납예정일 알림`
  - `김주용님 입학원서 접수가 완료되었습니다.`
  - `부재도서신고 처리알림`
  - `새로운 환경에서 로그인 되었습니다.`
  - `Items on your wishlist are now discounted!`
  - `Apple ID를 사용한 최근 다운로드`
  - `주문 확인 W841831412`
- thread pattern:
  - `5` duplicate-message threads in the slice
  - the batch is mostly auth, newsletter, library, and purchase/receipt traffic

## recommended triage
1. `i-pin@koreacb.com`
- recommended state: `@GTD/Read`
- reason: one-time 인증 / 처리 완료 알림; read-and-archive is appropriate

2. `newsletter@gnu.kr`, `auto@gnu.ac.kr`, `newsletter@jinhak.com`, `teamzoom@zoom.us`, `storyboard-that@storyboardthat.com`, `news@updates.ubisoft.com`, `comms.evernote.com`
- recommended state: `@GTD/Read`
- reason: newsletter / content / product-update traffic; consume if needed, otherwise archive

3. `apply@jinhakapply.com`
- recommended state: `@GTD/Reference`
- reason: 입학원서 접수 완료 / submission confirmation is record material, not active task traffic

4. `auto@gnu.ac.kr` / `경상대학교 도서관` and `i.love.kbs@kbs.co.kr`-style institutional notices
- recommended state: `@GTD/Reference`
- reason: library / institutional notices are searchable records unless they explicitly ask for a response

5. `no-reply@email.apple.com`, `service@intl.paypal.com`, `kbinfo@kbmail.kbcard.com`, `cyberman@bill.kbcard.com`, `ums-oto@ums-oto.nonghyup.com`, `noreturnmail@kyobobook.co.kr`, `noreply@coupang.com`, `lpoint@lpoint.com`, `penup@penup.com`
- recommended state: `@GTD/Reference`
- reason: account, billing, download, order, point, and membership notices are lookup material

6. `comments-noreply@docs.google.com`
- recommended state: `@GTD/Waiting`
- reason: if the thread is an active review loop, keep it live; otherwise downgrade to `@GTD/Reference`

7. `chany010713@gmail.com`
- recommended state: `@GTD/Reference`
- reason: self-sent/manual residual traffic should be deduped by sender+subject and collapsed into one reference cluster

## practical guidance
- Do not add new `@AUTO/*` sender rules from this batch alone.
- Collapse KCB i-PIN duplicates by thread; it is one auth family.
- Collapse GNU newsletter and 도서관 notices by family, not by message count.
- Collapse Jinhak application confirmations by thread; treat them as record material.
- Treat product/newsletter traffic as `Read` unless it clearly needs a response.
- Treat account/order/payment/point notices as `Reference`.

## dedupe notes
- `i-pin@koreacb.com` has duplicate message threads for the same 인증 완료 subject.
- `apply@jinhakapply.com` repeats with the same submission-complete subject.
- `auto@gnu.ac.kr` and `newsletter@gnu.kr` are separate sender families but the same institutional info theme.
- `chany010713@gmail.com` remains a self-reference cluster and should not be split into work items.

## conclusion
- This batch is dominated by `@GTD/Read` and `@GTD/Reference`.
- `@GTD/Waiting` is limited to live review threads if any are still open.
- There is no strong `Action` cluster here.
- Thread-level dedupe is the main throughput lever for this batch.
