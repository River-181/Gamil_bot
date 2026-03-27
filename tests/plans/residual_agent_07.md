# residual_agent_07

## Scope
- residual slice: `A7`
- objective: unresolved tail에서 message-level apply-ready action `20`건 고정
- policy: **no new rules** (existing lane heuristic only)
- source: `/Users/river/tools/gmail-agent-sys/.tokens/sciencedaily_closeout_2.json` (`candidates` first `20`)

## Apply-ready actions (20)
| idx | message_id | sender | subject | apply_action | target_label | reason |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `194d176da4afd9d5` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - February 04, 2025` | `add label` | `@GTD/Read` | `newsletter/digest content` |
| 2 | `194c98581974393a` | `ScienceDaily <sciencedaily+featured@substack.com>` | `ScienceDaily: Featured - February 02, 2025` | `add label` | `@GTD/Read` | `featured newsletter issue` |
| 3 | `194c76e8ad18dedd` | `ScienceDaily <sciencedaily+environment@substack.com>` | `ScienceDaily: Environment - February 02, 2025` | `add label` | `@GTD/Read` | `topic newsletter issue` |
| 4 | `194c2a9dcf331f6d` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - February 01, 2025` | `add label` | `@GTD/Read` | `digest content, no follow-up` |
| 5 | `194bd920ba1c42a1` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - January 31, 2025` | `add label` | `@GTD/Read` | `content-only newsletter` |
| 6 | `194b36b066ec9bb7` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - January 29, 2025` | `add label` | `@GTD/Read` | `digest archive candidate` |
| 7 | `194addaee7054347` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - January 28, 2025` | `add label` | `@GTD/Read` | `repeated issue pattern` |
| 8 | `19493ae02cd52fd7` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - January 23, 2025` | `add label` | `@GTD/Read` | `digest content` |
| 9 | `1947f63d2b9e8799` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - January 19, 2025` | `add label` | `@GTD/Read` | `digest content` |
| 10 | `1946fa5de52df9f9` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - January 16, 2025` | `add label` | `@GTD/Read` | `digest content` |
| 11 | `1946519ba55575f5` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - January 14, 2025` | `add label` | `@GTD/Read` | `digest content` |
| 12 | `1944b99d88c16476` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - January 09, 2025` | `add label` | `@GTD/Read` | `newsletter backlog item` |
| 13 | `1942da27be607db7` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - January 03, 2025` | `add label` | `@GTD/Read` | `newsletter backlog item` |
| 14 | `193e65de7f54eb68` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - December 20, 2024` | `add label` | `@GTD/Read` | `newsletter backlog item` |
| 15 | `193da4edfd5cc922` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - December 18, 2024` | `add label` | `@GTD/Read` | `newsletter backlog item` |
| 16 | `193d5143aed38b4e` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - December 17, 2024` | `add label` | `@GTD/Read` | `newsletter backlog item` |
| 17 | `193d24b1360bba6b` | `ScienceDaily <sciencedaily+technology@substack.com>` | `ScienceDaily: Technology - December 16, 2024` | `add label` | `@GTD/Read` | `technology topic edition` |
| 18 | `193cfe82cdb26a09` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - December 16, 2024` | `add label` | `@GTD/Read` | `digest issue` |
| 19 | `193c07ca78d8f765` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - December 13, 2024` | `add label` | `@GTD/Read` | `digest issue` |
| 20 | `193bc37449480617` | `ScienceDaily <sciencedaily@substack.com>` | `ScienceDaily: All - December 12, 2024` | `add label` | `@GTD/Read` | `digest issue` |

## Execution note
- each row is apply-ready as a single-message action (`message_id` 기준)
- lane assignment reuses existing residual heuristic from the source snapshot; no rule expansion
