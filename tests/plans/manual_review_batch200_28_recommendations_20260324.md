# manual review batch200_28 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_28_20260324.json`
- query:
  - `has:nouserlabels`
- count:
  - `106`

## dominant patterns

### pattern A. account / login / dormancy / policy notices
- recurring sender families:
  - `account_noreply@navercorp.com`
  - `noreply@discord.com`
  - `no_reply@email.apple.com`
  - `notice-master@daum.net`
  - `skt-id@sk.com`
  - `webmaster@lottecinema.co.kr`
  - `kosaf-ng@kosaf.go.kr`
  - `master@gsretail.com`
  - `help@accts.epicgames.com`
  - `account@twitch.tv`
  - `no-reply@malangmalang.com`
- common subjects:
  - `새로운 환경에서 로그인 되었습니다.`
  - `새로운 지역에서의 Discord 로그인 인증`
  - `Your recent download with your Apple ID`
  - `회원님의 Daum 아이디가 휴면 상태로 전환될 예정입니다.`
  - `회원님의 계정이 휴면 상태로 변경되었습니다.`
  - `[롯데컬처웍스] 개인정보 수집 및 이용내역 안내`
  - `[한국장학재단] (~7/21까지) 국가장학금 정책연구 관련 설문조사 참여 요청`
  - `개인정보이용이력통지안내`
- recommended state:
  - `@GTD/Reference`
  - `@GTD/Action` only when the notice explicitly requires verification, reactivation, or re-consent
- reason:
  - account or policy notice mail
  - usually keep for lookup, but only some need action

### pattern B. game / software / platform update fan-out
- recurring sender families:
  - `news@updates.ubisoft.com`
  - `store@mail.epicgames.com`
  - `noreply@mk.totalwar.com`
  - `donotreply@vmware.com`
  - `storyboard-that@storyboardthat.com`
  - `announce@parallels-universe.com`
  - `do_not_reply@gog.com`
  - `newsletter@e.faithgateway.com`
  - `newsletter@homify.com`
  - `no_reply@homify.com`
  - `store-news@amazon.com`
  - `noreply_melon@kakaocorp.com`
  - `seezn@info.kt.com`
- common subjects:
  - `River-kingsman, Containment Event is live!`
  - `Epic Games Store의 새 소식을 확인하세요`
  - `Space Punks 얼리 액세스 받기`
  - `Parallels Desktop for Mac 평가판이 시작되었습니다!`
  - `VMware Fusion Player – Personal Use License`
  - `Hatchful / wishlist / features / trial / update` style subjects
  - `서비스 이전에 따른 Seezn(시즌) 개인정보 이전 안내`
  - `멜론 서비스 개인정보 이전 안내`
  - `Our Terms Have Changed`
- recommended state:
  - `@GTD/Read`
  - `@GTD/Reference` when it is a product announcement or policy change worth keeping
- reason:
  - mostly product or service update mail
  - skim/retain oriented, not immediate action

### pattern C. commerce / shipping / payment notices
- recurring sender families:
  - `paypal@mail.paypal.com`
  - `notice-buyer01.g@mail.aliexpress.com`
  - `notice-buyer03.g@mail.aliexpress.com`
  - `buyer-notice10.g@mail.aliexpress.com`
  - `buyer-notice12.g@mail.aliexpress.com`
  - `buyer-notice13.g@mail.aliexpress.com`
  - `buyer-notice9.g@mail.aliexpress.com`
  - `help@payple.kr`
  - `easypay_noreturn@kicc.co.kr`
  - `cyberman@bill.kbcard.com`
  - `noreply@coupang.com`
  - `info@wadiz.kr`
  - `sendalarm2@alba.co.kr`
- common subjects:
  - `한국 내 신속 배송`
  - `한국으로 24시간 내 발송`
  - `24시간 내 무료 발송`
  - `판매자가 메시지를 보냈습니다.`
  - `PayPal 은 여전히 US$5 리워드를 준비해 두었습니다`
  - `지금 바로 US$5 리워드를 신청하세요`
  - `우피 Oopy에서 결제한 내역입니다.`
  - `주용님, 마지막 기회입니다...`
  - `결제하신 내역을 안내드립니다`
- recommended state:
  - `@GTD/Reference` by default
  - `@GTD/Action` only when seller/support or explicit verification is needed
- reason:
  - order, shipping, billing, and payment notices
  - keep for lookup; only a few need active response

### pattern D. community / newsletter / promo
- recurring sender families:
  - `stevekwon@disquiet.io`
  - `contact@serenityforge.com`
  - `gamified newsletter / promo style senders`
  - `info@members.netflix.com`
  - `noreply@email.apple.com`
  - `noreply@discord.com`
  - `newsletter@homify.com`
- recommended state:
  - `@GTD/Read`
  - `@GTD/Reference` if the item is worth keeping
- reason:
  - mostly broadcast content or promotional update mail

## practical triage guidance
1. Keep account/login/policy mails in `Reference` unless the message explicitly needs a response or reactivation.
2. Treat game/software/platform announcements as `Read` or `Reference`, not `Action`.
3. Keep marketplace/payment/shipping notices in `Reference`.
4. Use `Action` only for explicit reply or verification requests.
5. Do not move these families into `@AUTO/*`; this batch is residual manual triage.

## dedupe notes
- Thread dedupe is limited: `104` unique threads out of `106` messages.
- Dedupe should be sender-family first, then subject theme, then thread.
- `account_noreply@navercorp.com` repeated login notices should stay one account-notice family.
- `paypal@mail.paypal.com` plus payment/billing variants should be one PayPal family.
- `discord`, `epicgames`, `parallels`, `vmware`, `ubisoft`, and `gog` should be treated as recurring platform-update families rather than separate operational buckets.

## recommended default states by family
- account / login / policy notices -> `@GTD/Reference`
- game / software / platform updates -> `@GTD/Read`
- commerce / shipping / billing notices -> `@GTD/Reference`
- explicit verification / reply-needed -> `@GTD/Action`

