# apply ready manual work thread batch 2026-03-25

## scope
- manual/work residual 중 thread-level로만 판단 가능한 최소 안전 배치.
- 새 sender rule 추가 없음.
- message 단위가 아니라 thread 단위로만 결정한다.

## smallest safe batch

| thread / sender | recommended GTD state | reason |
| --- | --- | --- |
| `djglocal25@naver.com` | `@GTD/Action` or `@GTD/Waiting` | project / contract / hackathon follow-up |
| `doogie233@naver.com` | `@GTD/Waiting` | refund / admin follow-up |
| `euclidsoft.edu@gmail.com` | `@GTD/Action` or `@GTD/Reference` | mentor / submission / report thread |
| `outlook_7a89390ca06e025e@outlook.com` | `@GTD/Action` | offline meeting / direct reply thread |
| `aa01053208720@gmail.com` | `@GTD/Action` | travel / planning / direct reply thread |
| `minjugim655@gmail.com` | `@GTD/Action` or `@GTD/Reference` | project / submission / mentor coordination |
| `hoam518@gmail.com` | `@GTD/Waiting` | refund / admin follow-up thread |

## decision rule
- If a thread mixes project, admin, and personal contexts, keep it manual until a human confirms the final state.
- Repeated self/reply mail is not split into separate actions.
- The safe batch size for this lane remains `25-50`, but these 7 threads are the smallest stable confirmation set.

## next step
1. confirm these 7 threads at thread level.
2. keep the rest in manual triage.
3. do not add new sender rules unless a new repeated safe family appears in fresh samples.
