# manual review batches 11-15 summary 2026-03-24

## scope
- source batches:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_11_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_12_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_13_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_14_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_15_20260324.json`
- recommendation docs:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_11_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_12_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_13_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_14_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_15_recommendations_20260324.md`

## executive summary
- `11~15`는 self-thread 구간이 아니라 `generic residual sender-family` 구간이다.
- 대부분은 `@GTD/Reference`로 수렴한다.
- 예외는 두 축뿐이다.
  - `Security/Auth lane`
  - 실제 후속이 남은 `Action/Waiting lane`

## dominant families
### security / auth
- `help@help.naver.com`
- `no-reply@everytime.kr`
- `Everytime` login notice
- `ViaCharacter` password reset
- 일부 `Apple`, `NaverPay`, 공식 계정 확인 메일

### reference / content
- `ScienceDaily`
- `Glasp`
- `Freedom`
- `British Museum`
- `Scholarcy`
- `Linking Your Thinking`
- `Asana`
- `Supabase`
- `Threads`
- `Google Workspace`
- `OpenAI`
- `Figma`
- `Hancom`
- `AliExpress`
- `Daiso`
- `Raindrop`

### finance / receipt / service notice
- `Stripe`
- `Inicis`
- `KB Card`
- `KICC`
- `Trip.com`
- `Blue Ribbon Bags`
- `Kyobo`

### academic / admin / collaboration
- `comments-noreply@docs.google.com`
- `globaltalent@kird.re.kr`
- `munhyunsu@cs-cnu.org`
- `cnu2@icerti.co.kr`
- study abroad / 모집 / 행사 메일

## batch-level conclusion
### batch100_11
- highly distributed long-tail batch
- 기본 `Reference`
- `Everytime` login은 `Action` 후 `Reference`

### batch100_12
- self-mail + auth + product notice + CNU admin 혼합
- 기본 `Reference`
- auth/security는 `Read`
- 살아 있는 협업 thread만 `Waiting`

### batch100_13
- newsletter / official notice family가 섞인 배치
- content/newsletter는 `Read` 또는 `Reference`
- 공식 알림은 `Reference`
- 일부 행사/지원/모집은 `Action`

### batch100_14
- content-heavy generic residual
- `ScienceDaily`, `Glasp`, `Freedom`, `Scholarcy`는 `Read`
- platform/service notice는 `Reference`
- login/password reset은 `Security`

### batch100_15
- commerce/content/platform mix
- 기본 `Reference`
- 로그인/초대/명시적 확인만 `Action`

## operational split
### lane A: security/auth
- 처리 기준:
  - 로그인 확인
  - 비밀번호 재설정
  - 인증번호
  - 계정 보호 notice
- state:
  - 우선 `@SYS/Security`
  - 확인 완료 후 필요 시 `@GTD/Reference` 또는 `@GTD/Read`

### lane B: reference/content
- 처리 기준:
  - 뉴스레터
  - 제품 업데이트
  - 서비스 공지
  - 영수증/명세
  - 읽고 보관할 정보성 메일
- state:
  - 기본 `@GTD/Reference`
  - 읽고 종료 가능 콘텐츠는 `@GTD/Read`

### lane C: live action/waiting exception
- 처리 기준:
  - 초대
  - 응답 필요
  - 신청/행사/모집 후속
- state:
  - `@GTD/Action`
  - `@GTD/Waiting`

## decision
1. `11~15`는 bulk manual triage 대상이다.
2. 새 자동 rule 추가보다 lane-based manual triage가 안전하다.
3. 다음 배치는 `Security/Auth`와 `Reference/Content` 기준으로 바로 분기한다.
