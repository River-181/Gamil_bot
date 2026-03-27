# read first bulk rule v1

## purpose
- generic residual 중 읽고 종료 가능한 콘텐츠성 메일을 빠르게 `Read` 레인으로 압축한다.

## target pattern
- newsletter
- article digest
- launch/update content
- recurring informational content with low operational risk

## sender family examples
- `ScienceDaily`
- `hello@linkingyourthinking.com`
- `hello@freedom.to`
- `Glasp`
- `British Museum`
- `Scholarcy`
- article / digest / content newsletter family

## default state
- `@GTD/Read`

## exclusion
- 로그인 / 인증 / password reset
- 결제 / 영수증 / 예약 확인
- 협업 / 초대 / 회신 대기
- 실제 follow-up이 필요한 직접 메일

## operator rule
1. sender-family와 subject-theme를 먼저 묶는다.
2. 읽고 끝나면 `Read`
3. 보존 가치가 더 크면 `Reference`
4. 실행 필요성이 보이면 `Action` 또는 `Waiting`

## note
- `batch200_16~20`에서 가장 큰 저비용 축이다.
