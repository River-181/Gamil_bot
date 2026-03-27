# residual_agent_08

## Scope
- residual slice: `A8`
- source tail: `/Users/river/tools/gmail-agent-sys/tests/plans/apply_ready_residual_100_20260325.md` (`idx 45~64`)
- objective: unresolved tail에서 message-level apply-ready action `20`건
- policy: **no new rules** (existing lane heuristic only)

## Apply-ready actions (20)
| idx | source_idx | message_id | thread_id | sender | subject | apply label |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 45 | 19417095e79fa4d2 | 19417095e79fa4d2 | "中国南方航空股份有限公司" <skypearl@edm.csair.com> | Mileage Change of Sky Pearl Club Membership Card | `@GTD/Reference` |
| 2 | 46 | 1941445a2f7908aa | 1941441059332abe | czmp@csair.com | 新会员重置密码中文邮件 | `@GTD/Reference` |
| 3 | 47 | 1941441059332abe | 1941441059332abe | czmp@csair.com | 新会员重置密码中文邮件 | `@GTD/Reference` |
| 4 | 48 | 19413e0cac0bd3ff | 19413e0cac0bd3ff | "롯데ON" <lotteon@lotte.net> | [롯데쇼핑] 전자금융거래약관 개정 및 개인정보 이전 안내 | `@GTD/Reference` |
| 5 | 49 | 1941063cc711d868 | 1940bfda5f7599f2 | Mail Delivery Subsystem <mailer-daemon@googlemail.com> | Delivery Status Notification (Failure) | `@GTD/Reference` |
| 6 | 50 | 1940bf2a1ed5ce2b | 1940bf2a1ed5ce2b | Agoda Customer Service <no-reply@agoda.com> | Agoda 예약 확정서 - 예약 번호: 1479454508 | `@GTD/Reference` |
| 7 | 51 | 1940b59582961e6a | 1940b59582961e6a | Typeform Notifications <notifications@typeform.com> | You're in! Accept your invite to the Notion Template Community! | `@GTD/Reference` |
| 8 | 52 | 19407ca8bc9f72d7 | 19407ca8bc9f72d7 | Agoda <no-reply@agoda.com> | Email OTP | `@SYS/Security` |
| 9 | 53 | 194037af0f77dc02 | 194037af0f77dc02 | "닥터가드너" <drgardener@creators.gumroad.com> | 이제는 시작할 때입니다. 🔮 D-0 | `@GTD/Reference` |
| 10 | 54 | 193fded3a43c28f1 | 193fded3a43c28f1 | "닥터가드너" <drgardener@creators.gumroad.com> | 이만큼 따라올 수 있을까요? ⚔️ D-1 | `@GTD/Reference` |
| 11 | 55 | 193eb7366b4854f9 | 193eb7366b4854f9 | "닥터가드너" <drgardener@creators.gumroad.com> | 곧 시작됩니다 : 올해 마지막, 단 3일간의 특별한 기회 | `@GTD/Reference` |
| 12 | 56 | 193ea139ccd42ee4 | 193ea139ccd42ee4 | Gumroad <noreply@gumroad.com> | Your authentication token is 304823 | `@SYS/Security` |
| 13 | 57 | 193ea04a89928004 | 193ea04a89928004 | Notion Marketplace Team <svc-marketplace-waitlist@makenotion.com> | Thank you joining the Marketplace Waitlist! | `@GTD/Reference` |
| 14 | 58 | 193dcb16233f9f72 | 193dcb16233f9f72 | Lufthansa <newsletter@your.lufthansa-group.com> | 루프트한자와 함께하는 즐거운 연말 | `@GTD/Read` |
| 15 | 59 | 193db32250d9914e | 193db32250d9914e | Notion VIP <ahoy@notion.vip> | Learn Notion Formulas in 10 Minutes | `@GTD/Reference` |
| 16 | 60 | 193d79c854709643 | 193d79c854709643 | Threads <no-reply@mail.threads.net> | You have unread threads from choi.openai, notionhq and more | `@GTD/Read` |
| 17 | 61 | 193d6ebfcb6e9089 | 193d6ebfcb6e9089 | Skyscanner <no-reply@sender.skyscanner.com> | 위시리스트 항공편 2개의 가격 변동 💙 | `@GTD/Reference` |
| 18 | 62 | 193d6b2c9763ebb0 | 193d6b2c9763ebb0 | IFTTT <mail@ifttt.com> | Your year on IFTTT | `@GTD/Reference` |
| 19 | 63 | 193d3daec6dea282 | 193d3daec6dea282 | Jennifer at Notion <billing@mail.notion.so> | 💳 Payment failure for Notion | `@GTD/Reference` |
| 20 | 64 | 193c5bd61002564d | 193c5bd61002564d | AliExpress <transaction@notice.aliexpress.com> | 주문 1109663893661132: 귀하의 국가/지역 도착 | `@GTD/Reference` |

## Execution note
- each row is apply-ready as a single-message action (`message_id` 기준)
- lane assignment reuses existing residual heuristic from source; no rule expansion
