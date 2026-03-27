# residual_agent_06

## Scope
- residual slice: `A6`
- objective: unresolved tail에서 message-level apply-ready action `20`건 고정
- policy: **no new rules** (existing lane heuristic only)
- source: `/Users/river/tools/gmail-agent-sys/tests/plans/apply_ready_residual_next100_20260325.md` (tail window: idx `81~100`)

## Apply-ready actions (20)
| idx | message_id | thread_id | sender | subject | apply label |
| --- | --- | --- | --- | --- | --- |
| 1 | 19384e9a775feb77 | 19384e9a775feb77 | "KB국민은행" <kbinfo@kbmail.kbstar.com> | [KB국민은행 고객정보 변경 안내] | `@GTD/Reference` |
| 2 | 19381ae735cd5f27 | 19381ae735cd5f27 | AliExpress <aliexpress@notice.aliexpress.com> | 고객님의 소중한 의견을 들려 주세요! | `@GTD/Reference` |
| 3 | 1937ce8c61a8b37e | 1937ce8c61a8b37e | Google One <googleone-noreply@google.com> | 주용님의 멤버십의 종료되었습니다 | `@GTD/Reference` |
| 4 | 19377274884ceb20 | 19377274884ceb20 | Riot Games <RiotGames@em.riotgames.com> | [라이엇게임즈] 개인정보 이용내역 안내 | `@GTD/Reference` |
| 5 | 1937700c1752751e | 1937700c1752751e | "롯데컬처웍스" <WebMaster@lottecinema.co.kr> | 롯데컬처웍스 광고성 정보 수신동의 내역 안내 | `@GTD/Reference` |
| 6 | 19375a912dbd27a2 | 19375a912dbd27a2 | "ktmoving 주소연락처변경서비스" <return@ktmoving.com> | ktmoving 주소연락처변경서비스 신청 확인 메일입니다. | `@SYS/Security` |
| 7 | 193759e9fae71d06 | 193759e9fae71d06 | Agoda <no-reply@agoda.com> | Email OTP | `@SYS/Security` |
| 8 | 1936e049b212a9d4 | 1936e049b212a9d4 | "알바몬" <mailmaster@albamon.com> | [알바몬] 광고성 정보 수신동의 안내 | `@GTD/Reference` |
| 9 | 1936d91e87bd3989 | 1936d91e87bd3989 | "Miles & More" <mail@mailing.milesandmore.com> | Milestone 4: earn miles in your everyday life | `@GTD/Reference` |
| 10 | 1936cffac41e9bda | 1936cffac41e9bda | k-club <k-club@kird.re.kr> | [KIRD] 「과학기술 인재개발 세미나」 개최 안내 및 초청 (2024.12.18) | `@GTD/Reference` |
| 11 | 1936879ed681f125 | 1936879ed681f125 | "닥터가드너" <drgardener@creators.gumroad.com> | 신규 템플릿 업데이트 [PARA Note] 📱 | `@GTD/Reference` |
| 12 | 193671cad858a799 | 193671cad858a799 | Agoda Reviews <no-reply@agoda.com> | [Booking 1414705936] 💬💰 Save up to 18% by rating your stay | `@GTD/Reference` |
| 13 | 19364e426aca3c32 | 19364e426aca3c32 | Notion VIP <ahoy@notion.vip> | Mail Merge with Notion! Send Personalized Emails in Bulk | `@GTD/Reference` |
| 14 | 193630c31f58154f | 193630c31f58154f | Akiflow support <support@akiflow.com> | What Do You Think of Akiflow’s Latest Updates? | `@GTD/Read` |
| 15 | 1936290826400b6e | 1936290826400b6e | Agoda Reviews <no-reply@agoda.com> | Would you recommend APA Hotel Fukuoka Tenjinnishi to a friend? | `@GTD/Reference` |
| 16 | 1936266de97d5a08 | 1936266de97d5a08 | noreply@mail.fastretailing.com | <ユニクロ・ジーユー オンラインストア>会員登録ありがとうございました | `@GTD/Reference` |
| 17 | 19362667dd90708a | 19362667dd90708a | noreply@mail.fastretailing.com | <ユニクロ・ジーユー オンラインストア> メールアドレス確認 | `@GTD/Reference` |
| 18 | 1935409b881388d5 | 1935409b881388d5 | Austrian Airlines <austrian@smile.austrian.com> | Find winter magic in Austria | `@GTD/Reference` |
| 19 | 193534916f3115e8 | 193534916f3115e8 | GamsGo <noreply@post.gamsgo.vip> | 당신을 위한 GamsGo - 7% 할인 코드 | `@GTD/Reference` |
| 20 | 1935286d1b777d70 | 1935284954504c88 | "네이버" <account_noreply@navercorp.com> | 새로운 환경에서 로그인 되었습니다. | `@SYS/Security` |

## Execution note
- each row is apply-ready as a single-message action (`message_id` 기준)
- lane assignment reuses existing residual heuristic from the source file; no rule expansion
