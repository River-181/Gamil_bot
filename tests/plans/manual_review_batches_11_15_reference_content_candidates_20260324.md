# manual review batches 11-15 reference content candidates 2026-03-24

## source
- summary:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batches_11_15_summary_20260324.md`
- lane rule:
  - `/Users/river/tools/gmail-agent-sys/docs/reference_content_lane_rule_v1.md`

## purpose
- `batch100_11~15`에서 `Reference/Content lane` bulk 후보를 추린다.
- 이 문서는 다음 manual triage 압축 단계의 기본표다.

## read-first content family
- `ScienceDaily`
- `Glasp`
- `Freedom`
- `British Museum`
- `Scholarcy`
- `Linking Your Thinking`
- default state:
  - `@GTD/Read`
- note:
  - 읽고 종료 가능한 콘텐츠성 메일 우선

## reference-first platform family
- `Asana`
- `Supabase`
- `Threads`
- `Google Workspace`
- `OpenAI`
- `Figma`
- `Hancom`
- `Raindrop`
- default state:
  - `@GTD/Reference`
- note:
  - 제품/서비스 알림, 정책, 기록 보존 중심

## finance / booking / receipt family
- `Stripe`
- `KB Card`
- `KICC`
- `Inicis`
- `Trip.com`
- `Blue Ribbon Bags`
- `Kyobo`
- default state:
  - `@GTD/Reference`
- escalation:
  - 실제 후속 조치가 남아 있으면 `@GTD/Action`

## commerce / lifestyle family
- `AliExpress`
- `Daiso`
- `shop@email.stackcommerce.com`
- default state:
  - `@GTD/Reference`
- note:
  - 단순 확인/공지/프로모션 잔여 성격

## academic / collaboration family
- `comments-noreply@docs.google.com`
- `globaltalent@kird.re.kr`
- `munhyunsu@cs-cnu.org`
- `cnu2@icerti.co.kr`
- study abroad / 행사 / 모집 계열
- default state:
  - `@GTD/Reference`
- escalation:
  - 신청/응답/마감이 살아 있으면 `@GTD/Action`
  - 후속 회신 대기면 `@GTD/Waiting`

## operator rule
1. sender-family 단위로 먼저 묶는다.
2. 콘텐츠는 `Read`, 서비스/기록은 `Reference`를 기본값으로 둔다.
3. 초대/신청/응답 필요 케이스만 `Action/Waiting`으로 승격한다.

## next step
1. `11~15`에서 위 family별 샘플을 실제 message 수준으로 확인한다.
2. `Read`와 `Reference`를 나눠 bulk triage 초안을 만든다.
3. 그다음 다음 `100 x 5` generic residual과 연결한다.
