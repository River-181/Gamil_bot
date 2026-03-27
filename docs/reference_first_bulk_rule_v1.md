# reference first bulk rule v1

## purpose
- generic residual 중 서비스 알림, 기록 보존, 영수증, 예약, 플랫폼 업데이트를 `Reference` 레인으로 압축한다.

## target pattern
- service notice
- product update
- receipt / statement
- booking / shipping / fulfillment
- collaboration notice
- platform/system update

## sender family examples
- `Asana`
- `Notion`
- `GitHub`
- `OpenAI`
- `n8n`
- `Figma`
- `Supabase`
- `Threads`
- `Google Workspace`
- `AliExpress`
- `Daiso`
- `Stripe`
- `KB Card`
- `KICC`
- `Inicis`
- `Trip.com`
- `Agoda`
- `Skyscanner`
- `Uber`

## default state
- `@GTD/Reference`

## escalation
- 초대 수락 필요 -> `@GTD/Action`
- 신청/회신 대기 -> `@GTD/Waiting`
- 단순 읽고 끝나는 콘텐츠 -> `@GTD/Read`

## exclusion
- login / verification / password reset
- 직접 계약 / 제출 / 행정 회신

## note
- `batch200_16~20`의 주력 레인이다.
