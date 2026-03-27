# apply ready manual work safe slice 2026-03-25

## scope
- `manual/work 20`에서 thread-level로도 안전성이 높은 것만 남긴 apply-ready note.
- 새 `@AUTO/*` sender rule 추가 없음.
- thread 단위로만 판단한다.

## truly thread-level safe threads

| thread / sender | recommended GTD state | reason |
| --- | --- | --- |
| `doogie233@naver.com` | `@GTD/Waiting` | refund / admin follow-up thread |
| `hoam518@gmail.com` | `@GTD/Waiting` | refund / admin follow-up thread |
| `outlook_7a89390ca06e025e@outlook.com` | `@GTD/Action` | offline meeting / direct reply thread |
| `aa01053208720@gmail.com` | `@GTD/Action` | travel / planning / direct reply thread |

## excluded from apply-ready
- `djglocal25@naver.com`
- `euclidsoft.edu@gmail.com`
- `minjugim655@gmail.com`

### exclusion reasons
- these threads still mix project / mentor / submission / hackathon contexts
- they are better kept in manual triage until a human confirms final state

## decision rule
- If a thread mixes project, admin, personal, and follow-up semantics, keep it manual.
- Repeated self/reply mail is not split into separate actions.
- No sender rules are added here.

## next step
1. apply the 4 safe threads only if thread-level confirmation is still consistent.
2. keep the excluded threads in manual triage.
3. do not expand auto-safe sender rules.
