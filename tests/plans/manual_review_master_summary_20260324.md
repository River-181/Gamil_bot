# manual review master summary 2026-03-24

## objective
- `has:nouserlabels` 잔여를 전수에 가깝게 triage queue로 올리고, 실제 운영 가능한 lane 구조로 수렴시킨다.

## queue coverage
### batch100 series
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_01_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_02_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_03_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_04_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_05_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_06_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_07_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_08_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_09_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_10_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_11_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_12_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_13_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_14_20260324.json`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_15_20260324.json`
- total:
  - `1430`

### batch200 series
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_16_20260324.json` ~ `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_20_20260324.json`
- total:
  - `1000`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_21_20260324.json` ~ `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_25_20260324.json`
- total:
  - `849`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_26_20260324.json` ~ `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_30_20260324.json`
- total:
  - `506`
- `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_31_20260324.json` ~ `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_35_20260324.json`
- total:
  - `342`

### grand total
- triage queue coverage:
  - `4127`

## lane model
### lane 1. manual/work
- examples:
  - `djglocal25@naver.com`
  - `doogie233@naver.com`
  - `euclidsoft.edu@gmail.com`
  - `outlook_...@outlook.com`
  - direct CNU reply threads
- dominant states:
  - `@GTD/Action`
  - `@GTD/Waiting`
  - `@GTD/Reference`

### lane 2. self-thread / self-reference
- examples:
  - `chany010713@gmail.com`
  - `안녕하세요`
  - `삼겹살 600g`
  - self memo / self archive families
- dominant state:
  - `@GTD/Reference`

### lane 3. read-first content
- examples:
  - `ScienceDaily`
  - `Glasp`
  - `Freedom`
  - `Linking Your Thinking`
  - `British Museum`
  - `Scholarcy`
- dominant state:
  - `@GTD/Read`

### lane 4. reference-first service / commerce / platform
- examples:
  - `Asana`
  - `Notion`
  - `GitHub`
  - `OpenAI`
  - `n8n`
  - `Figma`
  - `AliExpress`
  - `Stripe`
  - `KB Card`
  - `Trip.com`
  - `Agoda`
  - `Skyscanner`
- dominant state:
  - `@GTD/Reference`

### lane 5. security-first
- examples:
  - `help@help.naver.com`
  - `account_noreply@navercorp.com`
  - `no-reply@everytime.kr`
  - `no-reply@dropbox.com`
  - password reset / verification / login alert families
- dominant state:
  - `@SYS/Security`
- demotion:
  - old acknowledged notice -> `@GTD/Read` or `@GTD/Reference`

## key operating rule
1. message 기준이 아니라 `thread`, `sender-family`, `subject-theme` 기준으로 triage 한다.
2. 새 `@AUTO/*` 규칙은 더 이상 늘리지 않는다.
3. 남은 long-tail은 manual lane으로 처리한다.
4. `Read`, `Reference`, `Security` 3레인으로 bulk 압축하고 `Action/Waiting`만 예외 처리한다.

## current state
- triage queue 관점에서는 전수에 가까운 수준까지 올라왔다.
- 현재 live residual은 `201`이다.
- 현재 lane snapshots(`Security`, `Read`, `Reference`, `Manual-Work`)은 3650d 창 기준 모두 `0`이다.
- 즉, 남은 201은 기존 lane coverage 밖의 residual이다.
- 이제 핵심은 새 큐 생성보다 실제 lane별 적용과 steady-state 운영이다.

## next step
1. lane coverage를 다시 넓혀 residual 201의 sender/subject family를 보강한다.
2. `Security-first`, `Read-first`, `Reference-first`, `Manual-Work` snapshot을 다시 만든다.
3. 그 다음 `has:nouserlabels = 0`까지 closeout한다.
