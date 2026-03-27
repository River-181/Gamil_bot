# self-thread bulk apply checklist 2026-03-24

## scope
- target batches:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_08_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_09_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_10_20260324.json`
- rule reference:
  - `/Users/river/tools/gmail-agent-sys/docs/self_thread_bulk_reference_rule_v1.md`

## objective
- self-thread 중심 batch를 낮은 비용으로 `@GTD/Reference` 상태로 압축한다.
- message count가 아니라 thread family 기준으로 처리한다.

## pre-check
1. sender가 `chany010713@gmail.com`인지 확인
2. subject family가 self memo / self archive 성격인지 확인
3. 외부 수신자와 실제 대화가 섞인 thread가 아닌지 확인
4. 일정/계약/신청/제출처럼 살아 있는 action이 없는지 확인

## family examples
- `안녕하세요`
- `삼겹살 600g`
- `삼겹살`
- `21 학기 기말고사 정리`
- `실험 전 필독 사항 CAR`

## apply rule
1. 동일 subject family는 하나의 decision unit으로 묶는다.
2. 예외가 없으면 `@GTD/Reference`를 권장한다.
3. 명시적 follow-up이 보이면 그 thread만 `@GTD/Action` 또는 `@GTD/Waiting`으로 분리한다.

## do-not-bulk cases
- 외부인과 대화가 이어진 thread
- 특정 날짜/장소/행동이 필요한 reminder
- 제출 마감 또는 회신 대기 상태

## execution note
- `batch100_08`은 사실상 전부 bulk `Reference` 후보다.
- `batch100_09~10`은 bulk 후보가 대부분이지만, 일부 예외 thread를 먼저 걸러낸 뒤 처리한다.

## acceptance
- self-thread family를 message 기준이 아니라 thread family 기준으로 압축했는가
- `Action/Waiting` 예외를 놓치지 않았는가
- self-sent bulk 처리 후에도 manual-review 의미가 유지되는가
