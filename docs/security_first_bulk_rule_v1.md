# security first bulk rule v1

## purpose
- generic residual 중 계정/인증/로그인성 메일을 우선 분리한다.

## target pattern
- login alert
- verification
- password reset
- account notice
- suspicious access / security confirmation

## sender family examples
- `account_noreply@navercorp.com`
- `help@help.naver.com`
- `no-reply@everytime.kr`
- `no-reply@dropbox.com`
- `workspace-noreply@google.com`
- `googleaistudio-noreply@google.com`

## default state
- `@SYS/Security`

## demotion rule
- 이미 확인된 오래된 notice
  - `@GTD/Read`
  - 또는 `@GTD/Reference`

## exclusion
- 단순 제품 업데이트
- 영수증 / 예약 / 배송
- 뉴스레터 / 콘텐츠

## note
- `batch200_16~20`에서는 volume은 작지만 우선순위가 가장 높다.
