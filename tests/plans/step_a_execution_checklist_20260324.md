# step A execution checklist 2026-03-24

## goal
- reduce `has:nouserlabels` from `4015` to `3515`
- reduce `in:inbox has:nouserlabels` from `3641` to `3141`

## workstreams
### auto-safe residual
- [ ] check for newly discovered safe senders
- [ ] add sender only after subject sample review
- [ ] run `plan-only`
- [ ] build targeted snapshot
- [ ] apply snapshot with approval text
- [ ] record journal path
- [ ] recalculate baseline

### manual-review queue
- [ ] maintain `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_pool_400_20260324.json`
- [ ] maintain `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch_50_20260324.json`
- [ ] produce batch recommendation docs
- [ ] triage by thread, not by individual duplicate messages
- [ ] assign one of `@GTD/Action|Waiting|Reference|Read`

## safety
- [ ] do not auto-label manual-review senders as `@AUTO/*`
- [ ] keep self sender threads as `Reference` by default
- [ ] treat direct CNU threads conservatively
- [ ] remove risky sender rules if business/personal context is discovered

## milestone check
- [ ] batch recommendation docs accumulated
- [ ] safe sender residual reviewed
- [ ] baseline moved toward `3515`
