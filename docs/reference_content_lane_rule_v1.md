# reference content lane rule v1

## purpose
- generic residual 중 대부분을 차지하는 콘텐츠/업데이트/기록성 메일을 저위험 레인으로 정리한다.

## target pattern
- newsletter / article digest
- product update
- service notice
- platform digest
- receipt / statement / booking confirmation
- 읽고 보관할 가치가 있는 informational mail

## sender family examples
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
- `Stripe`
- `KB Card`
- `KICC`
- `Inicis`
- `Trip.com`

## default handling
### reference default
- 아래는 기본 `@GTD/Reference`
  - 제품/서비스 공지
  - 영수증/명세서
  - 예약/확인 메일
  - 협업 기록 메일
  - 정책/업데이트 안내

### read default
- 아래는 기본 `@GTD/Read`
  - 뉴스레터
  - 읽고 끝낼 콘텐츠성 메일
  - 반복 아티클 digest

## escalation to action
- 아래 조건이면 `Reference`가 아니라 `Action`
  - 초대 수락 필요
  - 신청/응답 필요
  - 계정 확인 필요
  - 행사/모집/지원 마감이 살아 있음

## exclusion
- password reset / login / verification은 security lane으로 분리
- 직접 회신/계약/멘토링/행정 신청은 manual/work lane으로 분리

## note
- `batch100_11~15`는 이 lane이 주력이다.
- 새 자동 rule을 늘리기보다 sender-family 기준으로 manual triage 하는 편이 안전하다.
