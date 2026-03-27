# residual_agent_10

## Scope
- residual slice: `A10`
- source: `/Users/river/tools/gmail-agent-sys/tests/plans/manual_triage_batch_a_100_20260325.md`
- tail window: global rows `81~100` (`20` messages)
- policy: **no new rules** (message-level apply only)

## Apply-ready actions (20)
| idx | global_idx | message_id | thread_id | sender | subject | apply_action |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 81 | `19377274884ceb20` | `19377274884ceb20` | `Riot Games <RiotGames@em.riotgames.com>` | `[라이엇게임즈] 개인정보 이용내역 안내` | `add_label("@GTD/Reference"), archive:true` |
| 2 | 82 | `1937700c1752751e` | `1937700c1752751e` | `"롯데컬처웍스" <WebMaster@lottecinema.co.kr>` | `롯데컬처웍스 광고성 정보 수신동의 내역 안내` | `add_label("@GTD/Reference"), archive:true` |
| 3 | 83 | `19375a912dbd27a2` | `19375a912dbd27a2` | `"ktmoving 주소연락처변경서비스" <return@ktmoving.com>` | `ktmoving 주소연락처변경서비스 신청 확인 메일입니다.` | `add_label("@GTD/Action"), archive:true` |
| 4 | 84 | `193759e9fae71d06` | `193759e9fae71d06` | `Agoda <no-reply@agoda.com>` | `Email OTP` | `add_label("@GTD/Reference"), archive:true` |
| 5 | 85 | `1936e049b212a9d4` | `1936e049b212a9d4` | `"알바몬" <mailmaster@albamon.com>` | `[알바몬] 광고성 정보 수신동의 안내` | `add_label("@GTD/Reference"), archive:true` |
| 6 | 86 | `1936d91e87bd3989` | `1936d91e87bd3989` | `"Miles & More" <mail@mailing.milesandmore.com>` | `Milestone 4: earn miles in your everyday life` | `add_label("@GTD/Reference"), archive:true` |
| 7 | 87 | `1936cffac41e9bda` | `1936cffac41e9bda` | `k-club <k-club@kird.re.kr>` | `[KIRD] 「과학기술 인재개발 세미나」 개최 안내 및 초청 (2024.12.18)` | `add_label("@GTD/Reference"), archive:true` |
| 8 | 88 | `1936879ed681f125` | `1936879ed681f125` | `"닥터가드너" <drgardener@creators.gumroad.com>` | `신규 템플릿 업데이트 [PARA Note] 📱` | `add_label("@GTD/Read"), archive:true` |
| 9 | 89 | `193671cad858a799` | `193671cad858a799` | `Agoda Reviews <no-reply@agoda.com>` | `[Booking 1414705936] 💬💰 Save up to 18% by rating your stay` | `add_label("@GTD/Reference"), archive:true` |
| 10 | 90 | `19364e426aca3c32` | `19364e426aca3c32` | `Notion VIP <ahoy@notion.vip>` | `Mail Merge with Notion! Send Personalized Emails in Bulk` | `add_label("@GTD/Reference"), archive:true` |
| 11 | 91 | `193630c31f58154f` | `193630c31f58154f` | `Akiflow support <support@akiflow.com>` | `What Do You Think of Akiflow’s Latest Updates?` | `add_label("@GTD/Read"), archive:true` |
| 12 | 92 | `1936290826400b6e` | `1936290826400b6e` | `Agoda Reviews <no-reply@agoda.com>` | `Would you recommend APA Hotel Fukuoka Tenjinnishi to a friend?` | `add_label("@GTD/Reference"), archive:true` |
| 13 | 93 | `1936266de97d5a08` | `1936266de97d5a08` | `noreply@mail.fastretailing.com` | `<ユニクロ・ジーユー オンラインストア>会員登録ありがとうございました` | `add_label("@GTD/Reference"), archive:true` |
| 14 | 94 | `19362667dd90708a` | `19362667dd90708a` | `noreply@mail.fastretailing.com` | `<ユニクロ・ジーユー オンラインストア> メールアドレス確認` | `add_label("@GTD/Reference"), archive:true` |
| 15 | 95 | `1935409b881388d5` | `1935409b881388d5` | `Austrian Airlines <austrian@smile.austrian.com>` | `Find winter magic in Austria` | `add_label("@GTD/Reference"), archive:true` |
| 16 | 96 | `193534916f3115e8` | `193534916f3115e8` | `GamsGo <noreply@post.gamsgo.vip>` | `당신을 위한 GamsGo - 7% 할인 코드` | `add_label("@GTD/Reference"), archive:true` |
| 17 | 97 | `1935286d1b777d70` | `1935284954504c88` | `"네이버" <account_noreply@navercorp.com>` | `새로운 환경에서 로그인 되었습니다.` | `add_label("@GTD/Reference"), archive:true` |
| 18 | 98 | `19351ad9ec5530d2` | `19351ad9ec5530d2` | `Anthropic Team <team@email2.anthropic.com>` | `How to prompt Claude for the best responses (4/5)` | `add_label("@GTD/Reference"), archive:true` |
| 19 | 99 | `1934bc9987cdb3d3` | `1934bc9987cdb3d3` | `AliExpress <notice@info.aliexpress.com>` | `판매자가 메시지를 보냈습니다.` | `add_label("@GTD/Reference"), archive:true` |
| 20 | 100 | `193497baae729ac4` | `193497baae729ac4` | `"Miles & More" <mail@mailing.milesandmore.com>` | `Milestone 3: how to redeem your miles for an unforgettable flying experience` | `add_label("@GTD/Reference"), archive:true` |

## Notes
- all rows are concrete message-level apply actions from unresolved tail slice `A10`
- no sender rule creation, no rule edits
