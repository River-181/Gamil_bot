# manual review apply draft 06-07 2026-03-24

## scope
- target recommendation docs:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_06_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_07_recommendations_20260324.md`

## purpose
- `batch100_06~07`을 실제 GTD 상태 적용 가능한 초안으로 정리한다.
- 이 문서는 아직 live mutate가 아니라 operator review용 초안이다.

## apply draft
### group A: action first
- sender / thread family:
  - `djglocal25@naver.com`
    - 계약/견적 문의
    - 해커톤 관련 직접 action
  - `outlook_7a89390ca06e025e@outlook.com`
    - 오프라인 미팅
  - 일부 CNU admin thread
    - `alma@cnu.ac.kr`
    - `huss@cnu.ac.kr`
    - `janghak@cnu.ac.kr`
- target state:
  - `@GTD/Action`

### group B: waiting
- sender / thread family:
  - `doogie233@naver.com`
    - 환급신청 후속
  - `euclidsoft.edu@gmail.com`
    - 멘토링 제출/회신 대기 thread
  - `suk.w.han@cnu.ac.kr`
  - `pdkim@cnu.ac.kr`
- target state:
  - `@GTD/Waiting`

### group C: reference
- sender / thread family:
  - `euclidsoft.edu@gmail.com`
    - 제출 완료물 / 지출품의서 / 발표자료 보존본
  - `humanrights@cnu.ac.kr`
  - `fric@cnu.ac.kr`
  - `cnuscc@cnu.ac.kr`
  - `cnupr@cnu.ac.kr`
  - `cybercnu@cnu.ac.kr`
  - `lib*`
  - `reply@cnu.ac.kr`
  - `chany010713@gmail.com` self-reference 일부
- target state:
  - `@GTD/Reference`

### group D: read
- sender / thread family:
  - `help@help.naver.com`
    - 인증/비밀번호/로그인 코드 중 이미 확인된 건
  - 공지성이나 별도 후속이 없는 직접 수신 메일
- target state:
  - `@GTD/Read`

## operator rule
1. thread 기준으로 먼저 묶는다.
2. 같은 sender라도 thread 목적이 다르면 상태를 분리한다.
3. `euclidsoft.edu@gmail.com`는 sender 전체를 한 상태로 처리하지 않는다.
4. `help@help.naver.com`는 보안성 확인 전에는 `Read` 또는 예외 `Security` 검토가 필요하다.

## next step
1. `batch100_06`에서 `Action/Waiting` thread만 먼저 추린다.
2. `batch100_07`은 `Reference` 우선으로 압축한다.
3. live apply 전에 operator review를 한 번 거친다.
