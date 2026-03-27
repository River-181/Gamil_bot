# manual work 20 slice 2026-03-25

## purpose
- `manual/work` lane의 첫 실행 단위인 `20`개를 thread-level GTD 기준으로 압축한다.
- 새 `@AUTO/*` sender rule은 추가하지 않는다.
- 이 slice는 자동 apply보다 수동 triage confirmation이 맞다.

## current truth
- auto-safe sender families are effectively exhausted.
- the 7-thread manual/work sender snapshot returned `0` unlabeled candidates.
- remaining value is in thread-level confirmation, not sender expansion.

## manual/work 20 slice
### confirmed minimum safe batch
| thread / sender | recommended GTD state | reason |
| --- | --- | --- |
| `djglocal25@naver.com` | `@GTD/Action` or `@GTD/Waiting` | project / contract / hackathon follow-up |
| `doogie233@naver.com` | `@GTD/Waiting` | refund / admin follow-up |
| `euclidsoft.edu@gmail.com` | `@GTD/Action` or `@GTD/Reference` | mentor / submission / report thread |
| `outlook_7a89390ca06e025e@outlook.com` | `@GTD/Action` | offline meeting / direct reply thread |
| `aa01053208720@gmail.com` | `@GTD/Action` | travel / planning / direct reply thread |
| `minjugim655@gmail.com` | `@GTD/Action` or `@GTD/Reference` | project / submission / mentor coordination |
| `hoam518@gmail.com` | `@GTD/Waiting` | refund / admin follow-up thread |

## remaining manual/work families
- direct university correspondence
  - `suk.w.han@cnu.ac.kr`
  - `pdkim@cnu.ac.kr`
  - `munhyunsu@cs-cnu.org`
- personal / reference-only direct mail
  - `oneulst1@naver.com`
  - `hihippo@lh.or.kr`
  - `olepensen@gmail.com`
- self-thread / self-reference
  - `chany010713@gmail.com`
- mixed-context direct reply
  - `invitations@linkedin.com`

## decision rule
- If a thread mixes project, admin, and personal contexts, keep it manual until a human confirms the final state.
- Repeated self/reply mail is not split into separate actions.
- `manual/work` lane should not be forced into auto-safe sender rules.

## next step
1. confirm the 7-thread minimum safe batch at thread level.
2. keep the rest in manual triage.
3. use `Read`, `Reference`, and `Security` bulk lanes separately.
