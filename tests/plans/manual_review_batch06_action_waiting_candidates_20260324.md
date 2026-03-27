# manual review batch06 action waiting candidates 2026-03-24

## source
- batch artifact:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_06_20260324.json`
- recommendation:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_06_recommendations_20260324.md`

## purpose
- `batch100_06`에서 실제 우선 처리할 `Action/Waiting` thread를 분리한다.

## action candidates
### `djglocal25@naver.com`
- thread family:
  - `Re: [2026 장인학교 해커톤] 망상궤도 팀, 비교견적 및 계약 문의`
- target state:
  - `@GTD/Action`
- reason:
  - 계약/견적 문의는 명시적 follow-up 대상이다.

### `outlook_7a89390ca06e025e@outlook.com`
- thread family:
  - `오프라인 미팅`
- target state:
  - `@GTD/Action`
- reason:
  - 일정/대면 조율 성격이다.

### `aa01053208720@gmail.com`
- thread family:
  - `오사카 여행계획`
- target state:
  - `@GTD/Action`
- reason:
  - 계획성 개인 일정 메일이다.

## waiting candidates
### `doogie233@naver.com`
- thread family:
  - `Re: [환급신청]충남대 데이터베이스 수업 SQLD 자격증 수수료 환급 신청`
- target state:
  - `@GTD/Waiting`
- reason:
  - 신청 후속 / 회신 대기 성격이 강하다.

### `euclidsoft.edu@gmail.com`
- thread family:
  - 멘토링 제출 / 수행계획서 / 발표자료 / 결과보고서 회신
- target state:
  - `@GTD/Waiting`
- note:
  - 제출 완료본 / 지출품의서는 `Reference`로 분리

### `djglocal25@naver.com`
- thread family:
  - `Re: 장인학교 해커톤 대체과제 안내`
- target state:
  - `@GTD/Waiting`
- reason:
  - 계약 문의와는 다른 후속 안내 thread다.

## reference demotion rule
- 아래는 `Action/Waiting`이 아니라 `Reference`로 내린다.
  - 자료 전달
  - 성적/문서 보존
  - 제출 완료본
  - 이미 종료된 인증성 메일

## next step
1. 위 후보를 thread 기준으로 실제 message id와 연결한다.
2. `batch100_07`도 같은 방식으로 `Waiting`만 따로 분리한다.
3. 그 다음 `06~07` live apply 초안으로 묶는다.
