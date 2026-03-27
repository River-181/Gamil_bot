# manual review batch200_23 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_23_20260324.json`
- query:
  - `has:nouserlabels`
- count:
  - `200`

## dominant patterns

### pattern A. community / newsletter / product-update fan-out
- recurring sender families:
  - `stevekwon@disquiet.io`
  - `notification@disquiet.io`
  - `members@arc.net`
  - `hello@linkingyourthinking.com`
  - `news@updates.ubisoft.com`
  - `storyboard-that@storyboardthat.com`
  - `support@logaster.com`
  - `noreply@coupang.com`
  - `support@oopy.io`
  - `hatchful@email.shopify.com`
  - `info@members.netflix.com`
  - `do_not_reply@email.gog.com`
  - `no-reply@malangmalang.com`
  - `noreply@steampowered.com`
  - `notices@t.elements.envato.com`
- common subjects:
  - `[9월 4주차] 메이커 팀빌딩 리스트`
  - `디스콰이엇 Must Reads #16`
  - `김주용님을 위한 제품 개발 & 마케팅 전술`
  - `김주용님에게 드리는 Building in Public 플레이북`
  - `Arc Update | Never be late again`
  - `One week until Config 👀`
  - `The (Inte)Greatest. Feature. Of. All. Time.`
  - `Items on your wishlist are now discounted!`
  - `새로운 환경에서 로그인 되었습니다.`
- recommended state:
  - `@GTD/Read`
  - `@GTD/Reference` when the update is something the user may want to revisit later
- reason:
  - mostly community digest, product-update, or marketing mail
  - skim/retain oriented, not immediate action

### pattern B. marketplace / shipping / order / billing notices
- recurring sender families:
  - `notice-buyer03.g@mail.aliexpress.com`
  - `notice-buyer01.g@mail.aliexpress.com`
  - `buyer-notice10.g@mail.aliexpress.com`
  - `buyer-notice12.g@mail.aliexpress.com`
  - `buyer-notice13.g@mail.aliexpress.com`
  - `buyer-notice9.g@mail.aliexpress.com`
  - `transaction@notice.aliexpress.com`
  - `ae-touch.ae3@mail.aliexpress.com`
  - `paypal@mail.paypal.com`
  - `paypal@emails.paypal.com`
  - `help@payple.kr`
  - `easypay_noreturn@kicc.co.kr`
  - `cyberman@bill.kbcard.com`
  - `support@macpaw.com`
  - `noreply@email.apple.com`
  - `noreply@imweb.me`
- common subjects:
  - `한국 내 신속 배송`
  - `한국으로 24시간 내 발송`
  - `24시간 내 무료 발송`
  - `판매자가 메시지를 보냈습니다.`
  - `우피 Oopy에서 결제한 내역입니다.`
  - `PayPal 이용약관이 곧 변경됩니다.`
  - `US$10 리워드`
  - `베스트펜 주문내역서 확인 메일입니다.`
  - `MacPaw 액세스 링크`
  - `김*용님, 쿠팡(주)에서 [신용카드]결제하신 내역입니다.`
- recommended state:
  - `@GTD/Reference` by default
  - `@GTD/Action` only if seller support or explicit reply/verification is needed
- reason:
  - order, shipping, billing, and payment notices
  - keep for lookup; only some threads need action

### pattern C. account / login / policy / verification notices
- recurring sender families:
  - `account_noreply@navercorp.com`
  - `no-reply@everytime.kr`
  - `google-gemini-noreply@google.com`
  - `sc-noreply@google.com`
  - `nexon_noreply@nexon.com`
  - `webmaster@career.go.kr`
  - `no-reply@accounts.bitly.com`
  - `noreply@mk.totalwar.com`
  - `no-reply@yanadoocorp.com`
  - `no-reply@t.mail.coursera.org`
- common subjects:
  - `새로운 환경에서 로그인 되었습니다.`
  - `Google 계정에서 저장한 주소를 관리하세요`
  - `[넥슨] 이메일 인증을 위한 인증번호를 안내 드립니다.`
  - `[통합회원] 2년주기 재동의 대상 안내`
  - `계정에 복구 연락처가 추가되었습니다.`
  - `[야핏] 소멸 예정 포인트를 확인하세요!`
  - `PayPal 이용약관이 곧 변경됩니다.`
- recommended state:
  - `@GTD/Reference` by default
  - `@GTD/Action` only for explicit re-consent, verification, or security response
- reason:
  - account, login, or policy notice mail
  - usually worth keeping, but only a subset needs action

### pattern D. reply-needed coordination / support threads
- recurring sender families:
  - `chaitanya@akiflow.com`
  - `williamjung@disquiet.io`
  - `support@oopy.io`
  - `no-reply@yanadoocorp.com`
- common subjects:
  - `Re: Hi! I'm a great user of Archflow. I have a question regarding payme...`
  - `만들면 안되는 AI UX 3가지`
  - `우피 Oopy에서 결제한 내역입니다.`
  - `첫 lecture으로 시작하기`
- recommended state:
  - `@GTD/Waiting` for reply/confirmation needed
  - `@GTD/Action` if the thread is a direct request or deadline-driven task
- reason:
  - these are the few threads that still look interactive rather than broadcast-only

## practical triage guidance
1. Collapse `Disquiet`, `Arc`, `Linking Your Thinking`, `Storyboarding`, `Ubisoft`, `Shopify`, `Steam`, `GOG`, and similar communities into one newsletter/update class.
2. Keep `AliExpress`, `PayPal`, `Oopy`, `Payple`, `KB Card`, `KICC`, `Apple`, `Nexon`, and `Navercorp` notices in `Reference` unless a thread explicitly asks for action.
3. Use `Action` only for reply-needed or verification/deadline threads.
4. Do not move these families into `@AUTO/*`; this batch is residual manual triage, not auto-label calibration.

## dedupe notes
- Thread dedupe is limited here: 192 unique threads and only a few duplicated twice.
- Dedupe should be sender-family first, then subject theme, then thread.
- `notice-buyer* @mail.aliexpress.com` variants should be treated as one marketplace shipping family.
- `paypal@mail.paypal.com` and `paypal@emails.paypal.com` are one PayPal notice family, not separate categories.
- `stevekwon@disquiet.io` is the dominant newsletter family and should remain one `Read/Reference` bucket.

## recommended default states by family
- newsletter / community / product-update families -> `@GTD/Read`
- commerce / shipping / billing / account notices -> `@GTD/Reference`
- reply-needed support / coordination -> `@GTD/Waiting` or `@GTD/Action`

