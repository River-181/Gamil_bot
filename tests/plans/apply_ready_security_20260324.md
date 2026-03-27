# apply ready security 2026-03-24

## purpose
- `@SYS/Security` lane에 들어가는 메일을 실제 적용 후보로 압축한다.

## source material
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batches_11_15_security_auth_candidates_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batches_16_20_summary_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batches_21_30_summary_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batches_11_15_summary_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_24_recommendations_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_28_recommendations_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_31_recommendations_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_32_recommendations_20260324.md`

## apply-ready families
### high priority
- `help@help.naver.com`
- `no-reply@everytime.kr`
- `account_noreply@navercorp.com`
- `account-update@amazon.com`
- `msonlineservicesteam@microsoftonline.com`
- `noreply@disqus.com`
- `support_kmooc@nile.or.kr`
- `hotline@ebs.co.kr`
- `no-reply@dropbox.com`
- `workspace-noreply@google.com`
- `googleaistudio-noreply@google.com`

### medium priority
- `no_reply@email.apple.com`
- `notice-master@daum.net`
- `skt-id@sk.com`
- `kosaf-ng@kosaf.go.kr`
- `help@accts.epicgames.com`
- `account@twitch.tv`
- `sec.store@samsung.com`
- `sa.noreply@samsung-mail.com`

### conditional security
- `no-reply@email.apple.com`
- `account@twitch.tv`
- `noreply@coupang.com`
- `webmaster@ums.nonghyup.com`
- `nexon_noreply@nexon.co.kr`

## apply rule
1. account/login/password reset/verification only.
2. if a thread is already acknowledged and historical, demote to `@GTD/Reference` or `@GTD/Read`.
3. do not mix security with newsletters or promo.

## safety note
- `@SYS/Security` is the first lane to apply because it carries the highest user risk.
- only confirmed, non-actionable notices should be demoted.
