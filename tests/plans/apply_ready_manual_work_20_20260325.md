# apply ready manual work 20 slice 2026-03-25

## scope
- `manual/work 20` slice 중 thread-level로만 봐도 안전한 apply-ready 후보만 남긴다.
- 새 `@AUTO/*` sender rule은 추가하지 않는다.
- thread 단위로만 판단한다.

## apply-ready 4 threads

| thread / sender | recommended GTD state | reason |
| --- | --- | --- |
| `doogie233@naver.com` | `@GTD/Waiting` | refund / admin follow-up thread |
| `hoam518@gmail.com` | `@GTD/Waiting` | refund / admin follow-up thread |
| `outlook_7a89390ca06e025e@outlook.com` | `@GTD/Action` | offline meeting / direct reply thread |
| `aa01053208720@gmail.com` | `@GTD/Action` | travel / planning / direct reply thread |

## excluded manual/work threads
- `djglocal25@naver.com`
- `euclidsoft.edu@gmail.com`
- `minjugim655@gmail.com`

### exclusion reasons
- these threads still mix project / mentor / submission / hackathon contexts
- they remain better handled in manual triage until a human confirms the final state

## decision rule
- If a thread mixes project, admin, personal, and follow-up semantics, keep it manual.
- Repeated self/reply mail is not split into separate actions.
- No sender rules are added here.

## next step
1. apply the 4 safe threads only if thread-level confirmation is still consistent.
2. keep the excluded threads in manual triage.
3. do not expand auto-safe sender rules.
