# manual review batch200-20 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_20_20260324.json`
- query:
  - `has:nouserlabels`
- source pool:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_pool_generic_1000_20260324.json`
- count:
  - `200`

## dominant patterns
- Generic residual slice with mixed notification, newsletter, shipping, and privacy-alert mail.
- Sampled sender families include:
  - `learn@email1.asana.com`
  - `no-reply@everytime.kr`
  - `transaction@notice.aliexpress.com`
  - `daisomall_official@daiso.co.kr`
  - `sciencedaily@substack.com`
  - `glasp@substack.com`
- Most sampled items are single-message threads, so the main dedupe rule is sender-family + subject-theme, not self-thread collapse.

## recommended triage
### `@GTD/Reference`
- `transaction@notice.aliexpress.com`
  - shipping / order-status notices
- `daisomall_official@daiso.co.kr`
  - privacy / data-use notices
- `learn@email1.asana.com`
  - invite / workspace record
- `sciencedaily@substack.com`
  - newsletter / issue archive
- `glasp@substack.com`
  - creator/newsletter archive

### `@GTD/Action`
- `learn@email1.asana.com`
  - only when invite acceptance or task ownership is still pending
- `no-reply@everytime.kr`
  - only when login/device alert needs account review

### `@GTD/Waiting`
- invite threads awaiting response
- service/security threads awaiting follow-up after a user action

### `@GTD/Read`
- editorial/newsletter items with low archive value
- use when the content is informational but not worth retaining as reference

## dedupe notes
- Collapse repeated sender-family + subject-theme into one thread-level triage decision.
- Do not split shipping-status series into multiple actions.
- For newsletter families, keep one `Reference` or `Read` decision per issue family.
- This batch does not show self-thread behavior; do not apply self-thread dedupe rules.

## application notes
- Process this batch `Reference` first.
- Use `Action` only for explicit invite-acceptance or security-review cases.
- Use `Read` for low-value newsletter issues when archival search value is low.
