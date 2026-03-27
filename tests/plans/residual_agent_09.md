# residual_agent_09

## Scope
- residual slice: `A9`
- source: `/Users/river/tools/gmail-agent-sys/tests/plans/manual_triage_batch_a_50_20260325.md` (rows `31-50`)
- policy: no new rules; message-level apply-ready actions only

## Apply-ready actions (20)
| idx | source_row | message_id | sender | subject | apply_action | target_label |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 31 | `1972e3aca49aa5eb` | `Subway <subcard@subcard.co.kr>` | `써브웨이 고객님의 소멸 예정 포인트를 확인하세요.` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 2 | 32 | `1968e9a74c08e925` | `Subway <subcard@subcard.co.kr>` | `써브웨이 고객님의 소멸 예정 포인트를 확인하세요.` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 3 | 33 | `1952fa5b0fa3d7f9` | `AliExpress <transaction@notice.aliexpress.com>` | `1111275438131132 주문 건: 배송 완료 확인 대기 중` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 4 | 34 | `1952f13e2b6d817f` | `AliExpress <transaction@notice.aliexpress.com>` | `1111275438131132 주문 건: 주문 확인 완료` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 5 | 35 | `1952fca647cee377` | `AliExpress <transaction@notice.aliexpress.com>` | `1111275438151132 주문 건: 배송 완료 확인 대기 중` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 6 | 36 | `1952eda672a8cf2c` | `AliExpress <transaction@notice.aliexpress.com>` | `1111275438151132 주문 건: 주문 확인 완료` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 7 | 37 | `19530364d8c0a1f3` | `AliExpress <transaction@notice.aliexpress.com>` | `1111275911901132 주문 건: 배송 완료 확인 대기 중` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 8 | 38 | `1952edaf2a9f2f53` | `AliExpress <transaction@notice.aliexpress.com>` | `1111275911901132 주문 건: 주문 확인 완료` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 9 | 39 | `19530364c4dd5885` | `AliExpress <transaction@notice.aliexpress.com>` | `1111275911921132 주문 건: 배송 완료 확인 대기 중` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 10 | 40 | `1952edaf2f3a7b71` | `AliExpress <transaction@notice.aliexpress.com>` | `1111275911921132 주문 건: 주문 확인 완료` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 11 | 41 | `19530364bc5ccdbf` | `AliExpress <transaction@notice.aliexpress.com>` | `1111275911941132 주문 건: 배송 완료 확인 대기 중` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 12 | 42 | `1952edaf16e6bbd8` | `AliExpress <transaction@notice.aliexpress.com>` | `1111275911941132 주문 건: 주문 확인 완료` | `add:@GTD/Waiting, archive:true` | `@GTD/Waiting` |
| 13 | 43 | `195455af6d627bc6` | `"Anaconda, Inc." <account@anaconda.cloud>` | `Anaconda Distribution Download` | `add:@GTD/Reference, archive:true` | `@GTD/Reference` |
| 14 | 44 | `1972f4de65dfa360` | `"네이버" <account_noreply@navercorp.com>` | `새로운 환경에서 로그인 되었습니다.` | `add:@GTD/Reference, archive:true` | `@GTD/Reference` |
| 15 | 45 | `196e65027b20175b` | `"네이버" <account_noreply@navercorp.com>` | `새로운 환경에서 로그인 되었습니다.` | `add:@GTD/Reference, archive:true` | `@GTD/Reference` |
| 16 | 46 | `196d149bcbdf9a6b` | `"네이버" <account_noreply@navercorp.com>` | `새로운 환경에서 로그인 되었습니다.` | `add:@GTD/Reference, archive:true` | `@GTD/Reference` |
| 17 | 47 | `195087f675d4463d` | `"네이버" <account_noreply@navercorp.com>` | `새로운 환경에서 로그인 되었습니다.` | `add:@GTD/Reference, archive:true` | `@GTD/Reference` |
| 18 | 48 | `194e022d49c77697` | `"네이버" <account_noreply@navercorp.com>` | `새로운 환경에서 로그인 되었습니다.` | `add:@GTD/Reference, archive:true` | `@GTD/Reference` |
| 19 | 49 | `1941afe80748731e` | `"네이버" <account_noreply@navercorp.com>` | `새로운 환경에서 로그인 되었습니다.` | `add:@GTD/Reference, archive:true` | `@GTD/Reference` |
| 20 | 50 | `1941afe2861b4944` | `"네이버" <account_noreply@navercorp.com>` | `차단한 해외 지역에서 로그인이 시도되었습니다.` | `add:@GTD/Reference, archive:true` | `@GTD/Reference` |

## Notes
- all actions are message-level and apply-ready by `message_id`
- no sender-rule expansion and no new rule proposals
