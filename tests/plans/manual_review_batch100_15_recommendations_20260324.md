# manual review batch100-15 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_15_20260324.json`
- query:
  - `has:nouserlabels`
- source pool:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_pool_generic_500_20260324.json`
- count:
  - `100`

## dominant patterns
- This batch is a generic residual slice, not a self-thread batch.
- The sampled prefix is dominated by transactional notifications, account/login alerts, shipping updates, and newsletter-style content.
- Observed sender families in the sample:
  - `learn@email1.asana.com`
  - `no-reply@everytime.kr`
  - `transaction@notice.aliexpress.com`
  - `daisomall_official@daiso.co.kr`
  - `sciencedaily@substack.com`
  - `glasp@substack.com`
- The first items are mostly one-message threads, so thread dedupe is mainly a sender-family rule rather than a self-thread rule.

## recommended triage
### `@GTD/Reference`
- `transaction@notice.aliexpress.com`
  - order / shipping start notices
  - keep as record-keeping mail
- `daisomall_official@daiso.co.kr`
  - privacy / data-use notices
  - keep as record-keeping mail
- `learn@email1.asana.com`
  - team invite / workspace invite
  - keep if no immediate action is needed beyond later reference
- `sciencedaily@substack.com`
  - newsletter series
  - keep as reference unless the article itself needs follow-up
- `glasp@substack.com`
  - creator / newsletter content
  - reference by default

### `@GTD/Action`
- `learn@email1.asana.com`
  - if the invite is still pending response or task ownership needs confirmation
- `no-reply@everytime.kr`
  - if the login alert indicates an unexpected device and needs account review

### `@GTD/Waiting`
- `learn@email1.asana.com`
  - if the thread is waiting on a teammate or project owner response
- account/security or service threads that explicitly ask for a follow-up after an action

### `@GTD/Read`
- editorial newsletter content that is informative but not needed as permanent reference
- can be used for lightweight Substack/newsletter items when no search value remains

## dedupe notes
- Treat one sender-family + one subject theme as a single triage decision when the thread is effectively a one-message notification series.
- Do not split transactional mail into multiple `Action` items unless the thread clearly contains separate tasks.
- For repeated newsletters, prefer one `Reference` or `Read` decision per thread family, not per issue.
- This batch does not show the self-thread pattern seen in `batch100-10`; use normal sender dedupe instead of self-thread dedupe.

## application notes
- This batch should be handled as a mixed `Reference`-first residual slice.
- Use `Action` sparingly for explicit login/security or invite-response cases only.
- Use `Read` for newsletter-style entries that do not need archival search value.
