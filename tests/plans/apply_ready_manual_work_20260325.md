# apply ready manual work 2026-03-25

## purpose
- 남은 `manual/work residual` 중 실제 적용 가능한 최소 후보만 남긴다.
- 새 `@AUTO/*` 규칙은 추가하지 않는다.

## current truth
- auto-safe sender families are effectively exhausted.
- fresh sender-targeted snapshot for the 7-thread set returned `0` current unlabeled candidates, so the remaining value is in manual triage, not broad automation.
- the next 1000 goal should be chased by manual/work compression, not new sender rules.

## smallest safe candidate set
These are the only threads worth re-checking for apply-ready manual/work handling:

1. `djglocal25@naver.com`
- reason: project / contract / hackathon follow-up
- likely state: `@GTD/Action` or `@GTD/Waiting`

2. `doogie233@naver.com`
- reason: refund / admin follow-up
- likely state: `@GTD/Waiting`

3. `euclidsoft.edu@gmail.com`
- reason: mentor / submission / report thread with mixed work context
- likely state: `@GTD/Action` or `@GTD/Reference`

4. `outlook_7a89390ca06e025e@outlook.com`
- reason: direct offline meeting / reply thread
- likely state: `@GTD/Action`

5. `aa01053208720@gmail.com`
- reason: travel / planning / direct reply thread
- likely state: `@GTD/Action`

6. `minjugim655@gmail.com`
- reason: project / submission / mentor coordination
- likely state: `@GTD/Action` or `@GTD/Reference`

7. `hoam518@gmail.com`
- reason: refund / admin / follow-up thread
- likely state: `@GTD/Waiting`

## why these remain manual/work
- These senders mix project, admin, personal, or follow-up semantics.
- A single sender rule would overfire and create false positives.
- Message/thread context matters more than sender identity here.

## safety notes
- one thread = one GTD decision.
- repeated self/thread mail is not split into separate actions.
- if a sender mixes project/admin/personal contexts, keep it in manual triage instead of auto-routing.

## recommended next batch size
- `25-50`
- reason:
  - this lane is human-judgment heavy
  - bulk auto apply is no longer the right unit

## next step
1. keep the 7 threads in manual triage unless a human confirms thread-level action.
2. do not add new sender rules unless a new repeated safe family appears in fresh samples.
