# manual review batch100_13 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_13_20260324.json`
- query:
  - `has:nouserlabels`
- count:
  - `100`

## dominant patterns

### pattern A. newsletter / editorial / product-update fan-out
- recurring sender families:
  - `sciencedaily@substack.com`
  - `sciencedaily+quirky@substack.com`
  - `sciencedaily+society@substack.com`
  - `sciencedaily+environment@substack.com`
  - `sciencedaily+featured@substack.com`
  - `hello@linkingyourthinking.com`
  - `via@viacharacter.org`
  - `drgardener@creators.gumroad.com`
  - `hello@gamma.app`
  - `hello@email.freedom.to`
  - `support@wwiqtest-kr.com`
  - `noreply@newsletter.austrian.com`
  - `ahoy@notion.vip`
  - `notifications@gamma.app`
  - `community@figma.com`
  - `announcements@figma.com`
  - `team@email2.anthropic.com`
  - `info_at_raindrop_io_rctryzxm9f_fd0315b7@privaterelay.appleid.com`
  - `learn@email1.asana.com`
- common subjects:
  - `ScienceDaily: Featured - April 13, 2025`
  - `ScienceDaily: Environment - April 12, 2025`
  - `Are you losing YOU in the age of AI ?`
  - `Ideaverse Pro 2 launches tomorrow. Sneak Peek & Special Offer!`
  - `NEW—Calendar Views [Lite to Pro]`
  - `The Game-Changing Notion Feature You're Overlooking`
  - `Shipped: 한국어로 만나는 Figma`
  - `New Claude Features: Introducing Research and Google Workspace`
  - `Welcome to Raindrop.io`
  - `다시 한 번 Asana의 기능을 누려보세요`
- recommended state:
  - `@GTD/Read`
  - `@GTD/Reference` when the mail is a product announcement or feature update worth keeping
- reason:
  - mostly newsletter/marketing/content mail
  - useful to skim or retain, but rarely action-bearing

### pattern B. official account / security / payment / policy notices
- recurring sender families:
  - `no-reply@everytime.kr`
  - `naverpayadmin_noreply@navercorp.com`
  - `cyberman@bill.kbcard.com`
  - `easypay_noreturn@kicc.co.kr`
  - `noreply@kyobobook.co.kr`
  - `noreply@apple.com`
  - `webmaster@career.go.kr`
  - `no-reply@youversion.com`
  - `noreply@laftel.net`
  - `ec-system@ma.store.uniqlo.com`
  - `hello@backmarket.co.kr`
  - `google-gemini-noreply@google.com`
  - `no-reply@accounts.bitly.com`
- common subjects:
  - `[에브리타임] 새로운 기기(브라우저)에서 로그인 되었습니다.`
  - `네이버파이낸셜 서비스 이용약관 개정 안내`
  - `김*용님, 쿠팡(주)에서 [신용카드]결제하신 내역입니다.`
  - `[교보문고] 통합포인트가 소멸될 예정입니다.`
  - `계정에 복구 연락처가 추가되었습니다.`
  - `[통합회원] 2년주기 재동의 대상 안내`
  - `고난주간이 오늘 시작됩니다!`
  - `[라프텔] 휴면 계정 자동 탈퇴 예정 안내`
  - `【Back Market Korea】 중요 공지: 백마켓 한국 운영 종료`
  - `주용님, 이번 달 새로운 소식을 확인해 보세요`
- recommended state:
  - `@GTD/Reference` by default
  - `@GTD/Action` only when the notice clearly requires an explicit user action, such as re-consent or account update
- reason:
  - these are account, payment, policy, or service notices
  - usually worth keeping, but only some require action

### pattern C. academic / recruitment / research coordination
- recurring sender families:
  - `kird@kird.re.kr`
  - `cnu.global.study.abroad@gmail.com`
  - `suk.w.han@gmail.com`
  - `no-reply@news.ioi.dk`
  - `message from academic / study / event organizers`
- common subjects:
  - `[KIRD] 사회문제해결 R&D 모의기획 팀프로젝트 대학(원)생 연구팀 모집(교육/멘토링/연구비 지원사업)`
  - `자연 속으로 떠나는 휴식 여행`
  - `HITMAN is coming to Nintendo Switch 2 🍄`
  - `벼락치기와 기억에 끼치는 영향 문서가 처음 조회되었습니다`
  - `긴급휴강 공지`
- recommended state:
  - `@GTD/Action` for 모집, 신청, deadline-driven coordination
  - `@GTD/Reference` for announcement-only material
  - `@GTD/Read` for informational promotions without follow-up
- reason:
  - mixed academic, event, and announcement traffic
  - some threads are actionable, others are purely informational

## practical triage guidance
1. Treat `sciencedaily*`, `linkingyourthinking`, `gamma`, `figma`, `anthropic`, `asana`, `raindrop`, and similar product/newsletter families as a single newsletter/update class.
2. Keep account/payment/policy notices in `@GTD/Reference` unless the message explicitly asks for re-consent, verification, or account action.
3. Use `@GTD/Action` only for deadline-driven or response-required threads, not for generic update mail.
4. Do not promote these senders into `@AUTO/*` from manual review. This batch is residual triage, not auto-label calibration.

## dedupe notes
- There is no dominant self-thread family in this batch. Dedupe should be sender-family and subject-family based.
- `ScienceDaily` appears in multiple sub-address variants; collapse them into one newsletter family.
- `hello@linkingyourthinking.com` covers several product-launch and Ideaverse mails; keep one family state instead of splitting each announcement.
- `gamma`, `figma`, `anthropic`, `raindrop`, and `asana` are recurring product-update senders and should share the same high-level newsletter/update treatment.
- `no-reply@everytime.kr`, `noreply@apple.com`, and `webmaster@career.go.kr` look like official notices, but only the `career.go.kr` re-consent item is likely `Action`.

## recommended default states by family
- newsletter / editorial / product-update families -> `@GTD/Read` or `@GTD/Reference`
- account/security/payment/policy notices -> `@GTD/Reference`
- explicit recruitment / deadline / response-needed threads -> `@GTD/Action`

