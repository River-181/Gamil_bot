# closeout platform/product lane 2026-03-25

## scope
- platform/service/product/update/notification families only
- no new @AUTO rules
- snapshot built via sender-targeted query

## snapshot
- file: /Users/river/tools/gmail-agent-sys/.tokens/closeout_platform_50_20260325.json
- selected_candidates: 3
- lane status: near-exhausted (very low hit rate)

## sender families used
- notion.so
- mail.notion.so
- github.com
- notifications@github.com
- openai.com
- figma.com
- n8n.io
- slack.com
- atlassian.net
- atlassian.com
- trello.com
- supabase.com
- canva.com
- dropbox.com
- workspace-noreply@google.com

## candidates found (sample)
- Figma announcements (newsletter)
  - matched_rules: rule_newsletter_from (and rule_social_subject_guard for 1)
  - planned labels: @AUTO/Newsletter (+@AUTO/Social for the social-guard hit)

## conclusion
- Lane is effectively exhausted; only 3 candidates were found in the full sender set.
- Apply snapshot if you want these 3 labeled now; otherwise consider lane closed.
