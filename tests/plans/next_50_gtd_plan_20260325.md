# next 50 GTD plan 2026-03-25

## 목적
- 남은 residual을 `GTD state` 기준으로 가장 작은 실행 단위인 `50`개로 압축한다.
- 새 `@AUTO/*` sender rule은 추가하지 않는다.
- 기준 문서:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_master_summary_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/steady_state_ops_transition_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/tests/plans/apply_ready_manual_work_20260325.md`
  - `/Users/river/tools/gmail-agent-sys/config/filters.v3.json`

## current truth
- auto-safe sender families are effectively exhausted.
- the 7-thread manual/work sender snapshot returned `0` unlabeled candidates.
- remaining value is in `manual/work`, `self-thread`, and a small amount of long-tail `read/reference/security`.

## next 50 composition
### 1. manual/work `20`
- state target:
  - `@GTD/Action`
  - `@GTD/Waiting`
  - `@GTD/Reference`
- family examples:
  - `djglocal25@naver.com`
  - `doogie233@naver.com`
  - `euclidsoft.edu@gmail.com`
  - `outlook_7a89390ca06e025e@outlook.com`
  - `aa01053208720@gmail.com`
  - `minjugim655@gmail.com`
  - `hoam518@gmail.com`

### 2. self-thread / self-reference `10`
- state target:
  - `@GTD/Reference`
- family examples:
  - `chany010713@gmail.com`
  - `안녕하세요`
  - `삼겹살 600g`
  - `21 학기 기말고사 정리`

### 3. security-first `5`
- state target:
  - `@SYS/Security`
- family examples:
  - login alert
  - password reset
  - verification
  - account recovery
  - old acknowledged notices only if already confirmed safe

### 4. read-first content `5`
- state target:
  - `@GTD/Read`
- family examples:
  - `ScienceDaily`
  - `Glasp`
  - `Freedom`
  - `Linking Your Thinking`
  - other pure newsletter/content threads

### 5. reference-first service / commerce / platform `10`
- state target:
  - `@GTD/Reference`
- family examples:
  - `Notion`
  - `GitHub`
  - `OpenAI`
  - `n8n`
  - `Figma`
  - `Stripe`
  - `Trip.com`
  - `KB Card`
  - `AliExpress`
  - `Daiso`

## selection rule
- thread-level confirmation first.
- if a sender mixes project, admin, personal, or follow-up semantics, keep it in manual/work.
- do not split repeated self-thread mail into multiple actions.
- if a thread already has an explicit state in the existing summaries, keep that state unless a human has confirmed otherwise.

## execution order
1. `security-first`
2. `read-first`
3. `reference-first`
4. `manual/work`
5. self-thread bulk reference cleanup

## success criteria
- the next batch note should be small enough to apply or review in one pass.
- no new sender rules.
- the plan should remain compatible with the current `filters.v3.json`.
