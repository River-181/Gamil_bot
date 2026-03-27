# manual review batches 16-20 summary 2026-03-24

## scope
- source batches:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_16_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_17_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_18_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_19_20260324.json`
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_20_20260324.json`
- recommendation docs:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_16_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_17_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_18_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_19_recommendations_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_20_recommendations_20260324.md`

## executive summary
- `16~20`은 self-thread가 아니라 `generic long-tail residual`이다.
- 대부분은 아래 3개 레인으로 수렴한다.
  - `Read-first`
  - `Reference-first`
  - `Security-first`
- `Action/Waiting`은 예외 처리 레인으로만 남긴다.

## dominant families
### read-first
- `ScienceDaily`
- `hello@linkingyourthinking.com`
- `hello@freedom.to`
- `Glasp`
- 기타 article / digest / launch / newsletter family

### reference-first
- `Asana`
- `Notion`
- `GitHub`
- `OpenAI`
- `n8n`
- `Figma`
- `Supabase`
- `Threads`
- `Google Workspace`
- `AliExpress`
- `Daiso`
- `Stripe`
- `KB Card`
- `KICC`
- `Inicis`
- `Trip.com`
- `Agoda`
- `Skyscanner`
- `Uber`

### security-first
- `account_noreply@navercorp.com`
- `help@help.naver.com`
- `no-reply@everytime.kr`
- `no-reply@dropbox.com`
- `workspace-noreply@google.com`
- `googleaistudio-noreply@google.com`
- password reset / login alert / verification family

### waiting / action exceptions
- booking coordination
- admin / reply thread
- invitation / explicit confirmation
- live academic / admin follow-up

## batch-level conclusion
### batch200_16
- `200 messages / 192 threads / 84 senders`
- 가장 분산된 long-tail batch
- sender-family보다 lane-based triage가 맞다

### batch200_17
- `ScienceDaily`, Naver auth, booking, card/payment alert 중심
- `Read + Reference` 주력

### batch200_18
- 교육/뉴스레터/주문/결제/계정/제품 업데이트 혼합
- `Read + Reference`로 압축 가능

### batch200_19
- `Read newsletter`, `Reference service/finance`, `Security login/auth` 3축이 명확
- `Action/Waiting`은 minor

### batch200_20
- `Asana invite`, `Everytime login`, `AliExpress shipping`, `Daiso privacy`, `ScienceDaily`, `Glasp`
- 기본 `Reference`, 예외적으로 `Action`과 `Read`

## decision
1. `16~20`은 message 단위가 아니라 sender-family / subject-theme 단위로 본다.
2. 새 자동 rule 추가보다 manual bulk lane 적용이 안전하다.
3. 다음 `1000`도 같은 구조로 반복 가능하다.
