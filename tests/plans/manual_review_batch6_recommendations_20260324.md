# manual review batch6 recommendations 2026-03-24

## source
- pool:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_pool_400_20260324.json`
- sample slice:
  - `manual_like_primary[50:60]`

## recommended triage
- all 10 items
  - sender: `chany010713@gmail.com`
  - subject: `안녕하세요`
  - recommended state: `@GTD/Reference`
  - reason: self thread 반복, message 단위가 아니라 thread 단위로 하나만 보존하면 충분

## application notes
- `batch 5`와 동일 패턴이다.
- 실제 운영에서는 개별 message 10건이 아니라 동일 thread 1건으로 축약해서 처리해야 한다.
- Step A에서는 이런 self-thread 중복 제거가 체감량 감소에 중요하다.
