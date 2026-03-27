# security auth lane rule v1

## purpose
- generic residual 중 계정/보안성 메일을 별도 레인으로 분리한다.
- 일반 `Reference`와 구분해 우선 검토 대상으로 다룬다.

## target pattern
- sender examples:
  - `help@help.naver.com`
  - `no-reply@everytime.kr`
  - `account-related no-reply`
  - password reset sender
- subject examples:
  - login
  - password reset
  - verification
  - 인증번호
  - 비밀번호 변경
  - 계정 보호

## default handling
1. 먼저 `@SYS/Security`로 본다.
2. 이미 확인된 old notice면 `@GTD/Read` 또는 `@GTD/Reference`로 내린다.
3. 아직 확인하지 않은 최근 login / reset / verification이면 `Action` 우선이다.

## decision table
### active risk
- 조건:
  - 최근 notice
  - password reset
  - unfamiliar login
  - 명시적 계정 변경
- state:
  - `@SYS/Security`
  - 필요 시 operator action

### acknowledged / historical
- 조건:
  - 예전 notice
  - 이미 조치 완료
  - 단순 기록 보존 목적
- state:
  - `@GTD/Reference`
  - 또는 `@GTD/Read`

## exclusion
- marketing / promo 메일은 security lane에 넣지 않는다.
- 단순 서비스 업데이트는 reference lane으로 보낸다.

## note
- 이 lane은 `batch100_11~15`에서 반복 출현했다.
- 특히 `Everytime`, `Naver auth`, password reset 계열은 content lane과 분리하는 것이 맞다.
