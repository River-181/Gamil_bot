# residual_agent_01

## Scope
- source docs: `apply_ready_residual_25_1_20260325.md`, `apply_ready_residual_100_merged_20260325.md`
- focus: unresolved tail (`Manual/Work`) only
- policy: no new rules; message-level apply-ready actions only

## Apply-ready actions (20)
| idx | message_id | target_label | reason |
| --- | --- | --- | --- |
| 1 | 19498602be96d9f0 | @GTD/Reference | airline campaign/itinerary context; service/ops record value is higher than action need |
| 2 | 1948e7452bedb1df | @GTD/Reference | transport provider promo/update; keep as travel-service reference |
| 3 | 1948b88170c8060b | @GTD/Reference | nonprofit newsletter-style notice; informational archive without follow-up task |
| 4 | 1947a0bde4d15850 | @GTD/Reference | Trip.com itinerary message is booking/travel record |
| 5 | 1946f885c2e4549d | @GTD/Reference | Alsa realtime trip/update notice; service traceability record |
| 6 | 1946f708675dfa5d | @GTD/Reference | Alsa discount/promo from known service sender; reference lane for residual cleanup |
| 7 | 1946980b1ade8793 | @GTD/Reference | email-confirmation step notice from transport service; keep as account/service reference |
| 8 | 194692a2854880f0 | @GTD/Reference | Agoda cashback eligibility is booking/account-related transaction context |
| 9 | 1946731196f7eaf7 | @GTD/Reference | points-expiry notification is account status information, not immediate action in this pass |
| 10 | 19460fd315c3b8c4 | @GTD/Reference | Skyscanner wishlist fare update is recurring travel alert history |
| 11 | 1945e401b7c8dc3c | @GTD/Reference | product discount mail from vendor sender; low-risk residual reference classification |
| 12 | 19459e8658eb4746 | @GTD/Reference | Omio ticket message is explicit travel booking record |
| 13 | 19459e3beaa595cc | @GTD/Reference | refund confirmation from ticketing channel; financial/travel record retention |
| 14 | 194310aaab788a41 | @GTD/Reference | Agoda booking review reminder tied to booking id; retain with booking history |
| 15 | 19430bbab6b88a0b | @GTD/Reference | Airbnb stay follow-up/review request belongs to trip record context |
| 16 | 1942d227c96a67fc | @GTD/Reference | Lufthansa refund confirmation is transaction evidence |
| 17 | 1942cafeefeb32a7 | @GTD/Reference | subscription cancellation confirmation is service-account record |
| 18 | 1942af8403202171 | @GTD/Reference | Uber pre-ride service message is mobility service context archive |
| 19 | 194286e3a6d3af93 | @GTD/Reference | BlaBlaCar departure platform notice is trip execution detail |
| 20 | 19427e18790f14ff | @GTD/Reference | Uber fare-estimate guidance is service informational residual |

## Notes
- all actions intentionally avoid new sender rules
- labels use existing GTD taxonomy only
