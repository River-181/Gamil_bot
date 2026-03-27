# self-thread 10 slice 2026-03-25

## scope
- 대상은 `self-thread / self-reference` 10개 슬라이스다.
- 기준 문서:
  - `/Users/river/tools/gmail-agent-sys/docs/self_thread_bulk_reference_rule_v1.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/next_50_gtd_plan_20260325.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batches_6_10_summary_20260324.md`

## current truth
- self-thread는 sender-only 자동화 대상으로 보지 않는다.
- decision unit은 message count가 아니라 thread family다.
- 반복 self-mail은 bulk `@GTD/Reference`가 기본이다.

## dominant thread families
- `chany010713@gmail.com`
  - `안녕하세요`
  - `삼겹살 600g`
  - `21 학기 기말고사 정리`
  - `실험 전 필독 사항 CAR`
- family-level conclusion:
  - 위 반복 self-thread는 bulk `@GTD/Reference`

## decision rule
1. self-sent / self-thread 여부를 먼저 본다.
2. 명시적 외부 액션이 없으면 `@GTD/Reference`로 묶는다.
3. 일정 조율, 제출, 환급, 계약, 후속 답장처럼 살아 있는 액션이 있으면 `@GTD/Action` 또는 `@GTD/Waiting`으로 뺀다.
4. 같은 subject family는 message 별로 나누지 않는다.

## exclusions
- 자기 자신에게 보낸 메모라도 실제 일정, 제출, 답장 대기, 행정 요청이 있으면 bulk 처리하지 않는다.
- 외부인과의 대화가 섞여 있으면 thread-level 수동 판단을 유지한다.

## recommended GTD default
- bulk default:
  - `@GTD/Reference`
- exception states:
  - `@GTD/Action`
  - `@GTD/Waiting`
  - `@GTD/Read`

## execution note
- `batch100_08~10`에 우선 적용한다.
- 이 slice는 sender rule 추가 없이 thread-level triage만 수행한다.
- 다음 50개 계획과도 충돌하지 않도록 유지한다.
