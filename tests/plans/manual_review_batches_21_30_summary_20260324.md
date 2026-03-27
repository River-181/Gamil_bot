# manual review batches 21-30 summary 2026-03-24

## scope
- source batches:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_21_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_22_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_23_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_24_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_25_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_26_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_27_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_28_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_29_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_30_20260324.json`

## current evidence
- completed docs confirmed:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_21_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_22_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_23_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_29_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_30_recommendations_20260324.md`
- pending or not yet collected:
  - `24`
  - `25`
  - `26`
  - `27`
  - `28`

## executive summary
- `21~30`은 `generic residual lane`의 후반 구간이다.
- 구조는 이미 수렴했다.
  - `Read-first`
  - `Reference-first`
  - `Security-first`
  - minor `Waiting/Action`
- `29`, `30`은 empty batch였으므로, 실제 의미 있는 구간은 `21~28`이다.

## confirmed patterns
### batch200_21
- long-tail mixed residual
- dominant groups:
  - membership / community feed
  - security / account / verification
  - official / policy notice
  - commerce / order / shipping / payment
- decision:
  - `Read + Reference + Security`

### batch200_22
- dominant groups:
  - `Disquiet`
  - `Parallels`
  - `Zapier`
  - `AliExpress`
  - `Naver`
  - `Adobe`
  - `Google Docs comments`
- decision:
  - `Read + Reference`
  - collaboration comments만 `Waiting`

### batch200_23
- dominant groups:
  - `Disquiet`
  - `Arc`
  - `Linking Your Thinking`
  - `Ubisoft`
  - `StoryboardThat`
  - `Shopify`
  - `Steam`
  - `GOG`
- decision:
  - newsletter/update는 `Read`
  - commerce/finance/platform는 `Reference`
  - explicit follow-up만 `Action`

### batch200_29
- `count = 0`
- no-op

### batch200_30
- `count = 0`
- no-op

## operational meaning
- `21~23`만으로도 long-tail generic residual의 분류 기준은 충분히 드러났다.
- `24~28`도 같은 lane 구조일 가능성이 높다.
- 따라서 새 자동 rule을 늘리기보다,
  - `Read`
  - `Reference`
  - `Security`
기준으로 bulk manual triage를 이어가는 것이 맞다.

## pending note
- `24~28` 결과가 회수되면 이 문서를 최종본으로 승격할 수 있다.
