# manual review batches 6-10 summary 2026-03-24

## scope
- source batches:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_06_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_07_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_08_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_09_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_10_20260324.json`
- recommendation docs:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_06_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_07_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_08_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_09_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch100_10_recommendations_20260324.md`

## executive summary
- `batch100_06`은 실제 `manual/work residual` 핵심 구간이다.
- `batch100_07`은 `CNU/admin reference + self-reference` 혼합 구간이다.
- `batch100_08~10`은 거의 전부 `chany010713@gmail.com` self-thread 구간이다.
- 따라서 `06~07`은 세밀한 GTD triage가 필요하고, `08~10`은 bulk `@GTD/Reference` 기준으로 압축 처리하는 것이 맞다.

## batch-level conclusion
### batch100_06
- core senders:
  - `help@help.naver.com`
  - `euclidsoft.edu@gmail.com`
  - `doogie233@naver.com`
  - `djglocal25@naver.com`
- recommended mode:
  - `@GTD/Action`
  - `@GTD/Waiting`
  - `@GTD/Reference`
- note:
  - 인증/계약/멘토링/환급/미팅/자료전달이 섞인 실제 업무성 batch다.

### batch100_07
- core groups:
  - `manual_like_primary_2` 잔여
  - `manual_like_cnu_direct_2`
  - `manual_like_self` 일부
- recommended mode:
  - 기본 `@GTD/Reference`
  - 살아 있는 학업/회신 스레드만 `@GTD/Waiting`

### batch100_08
- `100/100` self-sent
- dominant subject family:
  - `삼겹살 600g`
  - `삼겹살`
- recommended mode:
  - 전부 `@GTD/Reference`

### batch100_09
- self-thread 중심
- repeated subject family:
  - `삼겹살 600g`
  - `21 학기 기말고사 정리`
  - `실험 전 필독 사항 CAR`
- recommended mode:
  - 기본 `@GTD/Reference`
  - 요청/후속 필요 thread만 `@GTD/Action` 또는 `@GTD/Waiting`

### batch100_10
- self-sent / self-thread 중심
- recommended mode:
  - 거의 전부 `@GTD/Reference`
- exception policy:
  - self memo라도 명시적 follow-up이 있으면 `@GTD/Action`

## operational split
### lane A: detailed manual triage
- 대상:
  - `batch100_06`
  - `batch100_07`
- 처리:
  - thread 기준으로 `Action/Waiting/Reference/Read`
- 목적:
  - 실제 남은 업무성 메일 수렴

### lane B: self-thread bulk reference
- 대상:
  - `batch100_08`
  - `batch100_09`
  - `batch100_10`
- 처리:
  - sender = `chany010713@gmail.com`
  - repeated self subject family
  - bulk `@GTD/Reference`
- 목적:
  - message count는 크지만 decision cost가 낮은 구간을 빠르게 축소

## decision
1. `06~07`은 manual triage apply draft를 먼저 만든다.
2. `08~10`은 self-thread bulk rule 문서로 별도 고정한다.
3. 이후 새 `100 x 5` batch를 이어서 만든다.
