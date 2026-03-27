# manual review batch200-25 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch200_25_20260324.json`
- query:
  - `has:nouserlabels`
- source pool:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_pool_generic_1000_b_20260324.json`
- count:
  - `49`

## dominant patterns
- Generic residual slice with mixed promo, account/security, and product-update mail.
- Sampled sender families include:
  - `newsletter@homify.com`
  - `ae.buyer.*@mail.aliexpress.com`
  - `account_noreply@navercorp.com`
  - `account.sso@myscript.com`
  - `paypal@mail.paypal.com`
  - `nexon_noreply@nexon.co.kr`
  - `storyboard-that@storyboardthat.com`
  - `marketing@twitch.tv`
- Most items are single-message threads, so dedupe should be sender-family + subject-theme.

## recommended triage
### `@GTD/Reference`
- `account_noreply@navercorp.com`
  - login / account environment notice
- `account.sso@myscript.com`
  - account reactivation / service access notice
- `nexon_noreply@nexon.co.kr`
  - dormancy / account status notice
- `ae.buyer.*@mail.aliexpress.com`
  - order / product notice series
- `paypal@mail.paypal.com`
  - reward / payment related notice when no reply is needed

### `@GTD/Read`
- `newsletter@homify.com`
  - marketing/newsletter content
- `storyboard-that@storyboardthat.com`
  - promo-style product/news content
- `marketing@twitch.tv`
  - promotional/news content

### `@GTD/Action`
- account/security notices only when the login or reactivation state needs an immediate user response
- use sparingly; most of this batch is archive/reference or low-value read material

### `@GTD/Waiting`
- only for account/service threads where the user already acted and is waiting on completion or confirmation
- do not use for ordinary promo/newsletters

## dedupe notes
- Collapse repeated AliExpress variants into one sender-family decision.
- Treat `account_noreply@navercorp.com`, `account.sso@myscript.com`, and `nexon_noreply@nexon.co.kr` as single-thread account-status families when they repeat.
- Use one `Reference` or `Read` decision per newsletter family; do not split issue-by-issue unless a later reply is pending.
- No self-thread dedupe needed in this batch.

## application notes
- Process as `Reference` first, `Read` second.
- Reserve `Action` for explicit account-recovery or reactivation events only.
- This batch is a fast residual cleanup slice, not a workflow queue.
