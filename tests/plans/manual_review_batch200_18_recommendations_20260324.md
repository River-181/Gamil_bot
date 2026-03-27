# manual review batch200_18 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_18_20260324.json`
- query:
  - `has:nouserlabels`
- count:
  - `200`

## dominant patterns

### pattern A. education / newsletter / learning fan-out
- recurring sender families:
  - `no-reply@t.mail.coursera.org`
  - `kmooc@wjtb.net`
  - `study@inflearn.com`
  - `kird@kird.re.kr`
  - `kostatin@korea.kr`
  - `korment9@kosaf.go.kr`
  - `master@positive.co.kr`
  - `noreply@newsletter.austrian.com`
  - `no-reply@youversion.com`
  - `hello@email.freedom.to`
- common subjects:
  - `김주용 님, 이번 달에 KMOOC에서 동료들이 배우는 내용은 다음과 같습니다.`
  - `[인프런] 지식공유자 코드팩토리님이 새소식을 등록했어요.📫`
  - `[K-MOOC 해외강좌] 코세라, 유데미 이용 종료(~6/14) 안내드립니다.`
  - `[한국장학재단] 제15기 사회리더 대학생 멘토링 뉴스레터 봄호 발행`
  - `[통계청 정책메일] 6월 첫째주 통계소식지`
  - `고난주간이 오늘 시작됩니다!`
- recommended state:
  - `@GTD/Read`
  - `@GTD/Reference` for official notices or course/admin reminders
- reason:
  - mostly newsletter, course digest, or informational mail
  - useful to keep, but rarely needs immediate action

### pattern B. commerce / order / account / receipt notices
- recurring sender families:
  - `notice@info.aliexpress.com`
  - `transaction@notice.aliexpress.com`
  - `ae-touch.ae3@mail.aliexpress.com`
  - `bestpen@bestpen.kr`
  - `support@macpaw.com`
  - `do-not-reply@watcha.com`
  - `info@members.netflix.com`
  - `noreply@email.apple.com`
  - `noreply@imweb.me`
  - `nexon_noreply@nexon.com`
  - `cyberman@bill.kbcard.com`
  - `easypay_noreturn@kicc.co.kr`
- common subjects:
  - `판매자가 메시지를 보냈습니다.`
  - `1101573717081132 주문 건: 배송 업데이트`
  - `베스트펜 주문내역서 확인 메일입니다.`
  - `CleanMyMac X - Plan for 1 Mac - 1 Year구매를 완료하세요...`
  - `MacPaw 액세스 링크`
  - `[WATCHA] 왓챠 개봉관 구매 내역 안내`
  - `김주용 님, 넷플릭스의 공개 예정작을 소개합니다`
  - `[넥슨] 이메일 인증을 위한 인증번호를 안내 드립니다.`
  - `김*용님, 쿠팡(주)에서 [신용카드]결제하신 내역입니다.`
- recommended state:
  - `@GTD/Reference` by default
  - `@GTD/Action` only for unresolved seller/support reply threads or explicit follow-up requests
- reason:
  - purchase, billing, verification, and order status mail
  - keep for lookup; only a subset needs a real action

### pattern C. product update / feature promo fan-out
- recurring sender families:
  - `members@arc.net`
  - `hello@super.so`
  - `announcements@figma.com`
  - `community@figma.com`
  - `team@email2.anthropic.com`
  - `google-gemini-noreply@google.com`
  - `noreply@steampowered.com`
  - `noreply@mk.totalwar.com`
  - `do-not-reply@watcha.com`
  - `hello@linkingyourthinking.com`
- common subjects:
  - `Arc Update | Never be late again`
  - `You can now crop images within Notion! 🔃 Here's how`
  - `Config 2024 초대장을 메일에서 확인하세요`
  - `New Claude Features: Introducing Research and Google Workspace`
  - `Gemini Advanced를 2개월간 무료로 사용해 보세요`
  - `Sun, Fun, and STAR TREK: Your Summer Starts With Update 13.5!`
  - `문의사항 관련`
- recommended state:
  - `@GTD/Read`
  - `@GTD/Reference` when the update is tied to a tool or feature the user may want to revisit
- reason:
  - mostly product marketing, launch, or feature update mail
  - good candidate for skim-only triage

### pattern D. reply-needed coordination / support threads
- recurring sender families:
  - `chaitanya@akiflow.com`
  - `williamjung@disquiet.io`
  - `no-reply@yanadoocorp.com`
  - `no-reply@t.mail.coursera.org`
- common subjects:
  - `Re: Hi! I'm a great user of Archflow. I have a question regarding payme...`
  - `만들면 안되는 AI UX 3가지`
  - `첫 lecture으로 시작하기`
  - `첫 supplement으로 시작하기`
  - `[야핏] 소멸 예정 포인트를 확인하세요!`
- recommended state:
  - `@GTD/Waiting` for reply or confirmation needed
  - `@GTD/Action` if the thread is a direct request or deadline-driven task
- reason:
  - these are the few threads that still look interactive rather than broadcast-only

## practical triage guidance
1. Treat `Coursera / KMOOC / Inflearn / KIRD / 통계청 / 장학재단` as one education/newsletter class and default it to `Read`.
2. Keep `AliExpress / BestPen / MacPaw / Watcha / Netflix / Apple / Nexon / KB Card / KICC` in `Reference` unless the thread explicitly needs a reply.
3. Put `Arc / Figma / Anthropic / Gemini / Notion / Super.so / Steam / Total War / Raindrop` in `Read` or `Reference` depending on whether the update is just informational or worth retaining.
4. Reserve `Action` for the handful of reply-needed or deadline-driven coordination threads.

## dedupe notes
- This batch has 193 unique threads and only 7 repeated twice, so thread-level dedupe is limited.
- Dedupe should be sender-family first, then subject family, then thread.
- `no-reply@t.mail.coursera.org` spans multiple course digest subjects and should be one family in triage.
- `notice@info.aliexpress.com` and `transaction@notice.aliexpress.com` are both marketplace notices and should not be split into separate operational categories.
- `members@arc.net`, `announcements@figma.com`, `community@figma.com`, and `team@email2.anthropic.com` are product-update families and should share the same `Read/Reference` treatment.

## recommended default states by family
- education / newsletter families -> `@GTD/Read`
- commerce / receipt / account notices -> `@GTD/Reference`
- product-update / feature mail -> `@GTD/Read` or `@GTD/Reference`
- reply-needed support / coordination -> `@GTD/Waiting` or `@GTD/Action`

