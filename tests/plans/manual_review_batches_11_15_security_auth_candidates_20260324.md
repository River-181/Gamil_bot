# manual review batches 11-15 security auth candidates 2026-03-24

## source
- summary:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batches_11_15_summary_20260324.md`
- lane rule:
  - `/Users/river/tools/gmail-agent-sys/docs/security_auth_lane_rule_v1.md`

## purpose
- `batch100_11~15`에서 `Security/Auth lane`만 따로 추린다.
- 이 문서는 실제 operator 검토 우선순위 표다.

## priority A
### `help@help.naver.com`
- pattern:
  - login
  - verification
  - password/auth notice
- default state:
  - `@SYS/Security`
- demotion rule:
  - 이미 확인 끝난 old notice면 `@GTD/Read`

### `no-reply@everytime.kr`
- pattern:
  - login notice
  - account/security confirmation
- default state:
  - `@SYS/Security`
- demotion rule:
  - history성 notice면 `@GTD/Reference`

### `ViaCharacter` password reset
- pattern:
  - password reset
- default state:
  - `@SYS/Security`

## priority B
### `Apple`
- pattern:
  - account/policy/update notice
- default state:
  - `@SYS/Security` 또는 `@GTD/Reference`
- note:
  - 실제 계정 확인이 필요하면 security, 단순 정책/기록은 reference

### `NaverPay`
- pattern:
  - official account / payment / auth mixed
- default state:
  - security 성격이면 `@SYS/Security`
  - 단순 거래기록이면 `@GTD/Reference`

## operator rule
1. 최근성 있는 계정 이벤트는 먼저 `Security`로 본다.
2. 이미 소진된 old notice는 `Read` 또는 `Reference`로 내린다.
3. marketing / newsletter와 섞이지 않게 별도 레인으로 유지한다.

## next step
1. `11~15` 실 message 샘플에서 위 sender를 먼저 확인한다.
2. `Security`와 `Reference`를 나눠 actual apply candidate를 만든다.
3. 그다음 `Reference/Content lane` bulk 후보를 처리한다.
