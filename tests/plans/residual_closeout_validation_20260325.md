# residual_closeout_validation_20260325

## Scope
- validate which candidate families are repeatable vs fragmented tail
- no new rules, no apply

## Input (latest residual shortlist)
- `ScienceDaily` family (substack variants) was the only large repeatable block (previously reported 51)
- `Imweb` family (`noreply@imweb.me`) was the only other repeatable block (previously reported 4)

## Validation result
### Repeatable families
- ScienceDaily family: **repeatable but now exhausted** in `has:nouserlabels` live queries
- Imweb family: **repeatable but very small** (4)

### Fragmented tail
- Everything else is currently **fragmented tail** (non-repeatable or count=0 in live probes)
- This includes prior probes that returned zero (various platform/security/newsletter families)

## Conclusion
- No new repeatable family remains beyond ScienceDaily/Imweb
- Next reduction must come from manual/work triage or direct single-message residual cleanup
- Do not add new auto rules for the fragmented tail
