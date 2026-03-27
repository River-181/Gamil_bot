# manual review batch8 recommendations 2026-03-24

## source
- pool:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_pool_400_20260324.json`
- sample slice:
  - `manual_like_primary[70:80]`

## recommended triage
### thread A
- sender: `chany010713@gmail.com`
- subject: `안녕하세요`
- messages:
  - `18a58d0fc9c845d8`
  - `18a58d0fc821f42f`
  - `18a58d0fc70a870b`
- recommended state: `@GTD/Reference`
- reason: self thread 반복

### thread B
- sender: `chany010713@gmail.com`
- subject: `삼겹살 600g`
- messages:
  - `189c8ffe98f3b9c2`
  - `189c8fed3e431c14`
  - `189c8fec5af579af`
  - `189c8feb9ed4e113`
  - `189c8fb86448862a`
  - `189c8f83184f17cb`
  - `189c8f7abb70571d`
- recommended state: `@GTD/Reference`
- reason: self thread 반복, 메모/기록 성격

## application notes
- `batch 8`은 10 message지만 실제 triage 단위는 2 thread다.
- self sender의 반복 subject는 Step A 진행률 계산에서 message 수보다 thread 수를 기준으로 본다.
