# manual review batch2 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch_50_20260324.json`
- sample slice:
  - items 11-20

## recommended triage
1. `19b1c08593b481fa`
- sender: `chany010713@gmail.com`
- subject: `(empty subject)`
- recommended state: `@GTD/Reference`
- reason: self/mail-draft 성격, 자동 분류보다 보존 쪽이 안전

2. `19a999974313c277`
- sender: `euclidsoft.edu@gmail.com`
- subject: `Re: [제출] R&D 프로젝트 멘토링_결과보고서 제출, 17-망상궤도-김주용`
- recommended state: `@GTD/Waiting`
- reason: 업무/멘토링 회신 스레드

3. `19a96d3903ecc583`
- sender: `euclidsoft.edu@gmail.com`
- subject: `Re: [제출] R&D 프로젝트 멘토링_결과보고서 제출, 17-망상궤도-김주용`
- recommended state: `@GTD/Waiting`
- reason: 동일 스레드

4. `19a90622727ffa4f`
- sender: `euclidsoft.edu@gmail.com`
- subject: `Re: [제출] R&D 프로젝트 멘토링_결과보고서 제출, 17-망상궤도-김주용`
- recommended state: `@GTD/Waiting`
- reason: 동일 스레드

5. `19a7b79537d6d655`
- sender: `euclidsoft.edu@gmail.com`
- subject: `Re: [제출] R&D 프로젝트 멘토링_결과보고서 제출, 17-망상궤도-김주용`
- recommended state: `@GTD/Waiting`
- reason: 동일 스레드

6. `19a7b66d3dcd435f`
- sender: `euclidsoft.edu@gmail.com`
- subject: `Re: [제출] R&D 프로젝트 멘토링_결과보고서 제출, 17-망상궤도-김주용`
- recommended state: `@GTD/Waiting`
- reason: 동일 스레드

7. `19a7058176b6e722`
- sender: `euclidsoft.edu@gmail.com`
- subject: `Re: [제출] R&D 프로젝트 멘토링_발표자료 제출, 17-망상궤도-김주용`
- recommended state: `@GTD/Waiting`
- reason: 멘토링 제출/회신 스레드

8. `199cc4d946abf45c`
- sender: `euclidsoft.edu@gmail.com`
- subject: `Re: [제출] R&D 프로젝트 멘토링_수행계획서, 17-망상궤도-김주용`
- recommended state: `@GTD/Waiting`
- reason: 멘토링 제출/회신 스레드

9. `1999f66aee136386`
- sender: `euclidsoft.edu@gmail.com`
- subject: `Re: [제출] R&D 프로젝트 멘토링_지출품의서 (망상궤도 김주용)`
- recommended state: `@GTD/Reference`
- reason: 행정/지출 증빙 성격이 강함

10. `1999e057a1164a50`
- sender: `minjugim655@gmail.com`
- subject: `Re: [ABC 프로젝트 멘토링 17기 망상궤도 품의서 제출 메일]`
- recommended state: `@GTD/Waiting`
- reason: 프로젝트 제출/후속 회신 스레드

## application notes
- `euclidsoft.edu@gmail.com`는 `promo`가 아니라 `manual-review`가 맞다는 근거가 추가로 강화됐다.
- 동일 스레드가 연속이면 message 단위보다 thread 단위로 상태 라벨을 하나로 묶는 편이 낫다.
- 멘토링 제출/회신성 메일은 `Waiting`, 행정 증빙성 메일은 `Reference`가 기본값이다.
