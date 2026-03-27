# apply ready read 2026-03-24

## purpose
- `@GTD/Read` lane에 들어가는 콘텐츠성 메일을 실제 적용 후보로 압축한다.

## source material
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batches_11_15_summary_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batches_16_20_summary_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batches_21_30_summary_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_24_recommendations_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_25_recommendations_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_31_recommendations_20260324.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_batch200_32_recommendations_20260324.md`

## apply-ready families
- `ScienceDaily`
- `Glasp`
- `Freedom`
- `British Museum`
- `Scholarcy`
- `Linking Your Thinking`
- `newsletter@homify.com`
- `storyboard-that@storyboardthat.com`
- `marketing@twitch.tv`
- `newsletter@gnu.kr`
- `newsletter@jinhak.com`
- `newsletter@manycam.com`
- `newsletter@e.faithgateway.com`
- `news@updates.ubisoft.com`
- `store@mail.epicgames.com`
- `noreply@tripwireinteractive.com`
- `do_not_reply@email.gog.com`
- `noreply@discord.com`
- `announcement / digest / product update families`

## apply rule
1. newsletter / digest / low-value content goes to `@GTD/Read`.
2. if the sender is worth keeping for lookup, use `@GTD/Reference`.
3. do not escalate to `Action` unless explicit follow-up is present.

## dedupe rule
- one sender-family + one subject family = one apply decision.
- repeated newsletters should collapse to one `Read` decision per family.

## safety note
- `Read` is the lowest-risk bulk lane and should be applied before broader reference cleanup.
