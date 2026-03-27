# milestone step A 500 2026-03-24

## baseline
- `has:nouserlabels = 4015`
- `in:inbox has:nouserlabels = 3641`

## target
- `has:nouserlabels: 4015 -> 3515`
- `in:inbox has:nouserlabels: 3641 -> 3141`

## strategy
1. 남은 자동화 가능한 safe sender는 계속 소거
2. 핵심 축은 `manual-review batch` 운영으로 전환
3. `50건 x 10 batch`를 Step A 기본 단위로 본다

## workstreams
### 1. auto-safe residual
- `@AUTO/*`, `@CTX/*`, `@SYS/*`로 안전하게 들어가는 sender만 추가
- 신규 long-tail sender는 샘플 확인 후만 편입

### 2. manual-review queue
- source:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_pool_400_20260324.json`
- working batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch_50_20260324.json`
- batch 1~10으로 나눠 `@GTD/Action|Waiting|Reference|Read` 추천안 생성

## safety rules
- `promo/newsletter` 자동 금지 sender는 계속 유지
- 업무/개인 회신은 자동 적용하지 않음
- self sender는 `Reference` 우선
- 같은 thread는 message 단위보다 thread 단위로 상태를 묶는다

## completion criteria
- batch recommendation 문서가 10개 쌓일 것
- safe sender residual은 추가 발견 시 즉시 소거
- Step A 종료 시 baseline이 `3515` 부근까지 내려갈 것
