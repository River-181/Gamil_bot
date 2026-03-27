# apply_ready_merged_batch_100_20260325

## scope
- merge/validation for current 100-message candidate sets
- sources:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/apply_ready_execute_batch_100_20260325.md` (safe closeout 21)
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_triage_batch_a_100_20260325.md` (manual triage 100)
- no new rules

## overlap check (manual)
- inspected message_id lists from both sources
- no overlap detected in the visible IDs
- note: this is a manual check based on the provided outputs, not a programmatic diff

## recommended selection for an exact 100
- keep all 21 safe closeout items
- take the first 79 items from manual triage batch A
- total = 100

## safe closeout (21)
### Security-first (9)
- 19575623ab05084c | workspace-noreply@google.com | Label_18
- 1955ba26d31760cf | workspace-noreply@google.com | Label_18
- 195326e9e1dd6e95 | workspace-noreply@google.com | Label_18
- 19522fb8eac04dfd | workspace-noreply@google.com | Label_18
- 19518aed92322d36 | workspace-noreply@google.com | Label_18
- 19513ad1bca11ab6 | workspace-noreply@google.com | Label_18
- 1917bc160459e147 | workspace-noreply@google.com | Label_18
- 18e68d0d9c54718a | workspace-noreply@google.com | Label_18
- 18ae048b0b6a8665 | workspace-noreply@google.com | Label_18

### Reference-first (9)
- 1971e9b057dbc794 | cyberman@bill.kbcard.com | Label_21, Label_23
- 196b2e596ad339f2 | cyberman@bill.kbcard.com | Label_21, Label_23
- 19618c84d48feff4 | cyberman@bill.kbcard.com | Label_21, Label_23
- 195eea0d501b5f04 | cyberman@bill.kbcard.com | Label_21, Label_23
- 19583505160c9aac | cyberman@bill.kbcard.com | Label_21, Label_23
- 19564c02f51ebed5 | cyberman@bill.kbcard.com | Label_21, Label_23
- 1944927b3a76d146 | cyberman@bill.kbcard.com | Label_21, Label_23
- 193aec9b7609200e | cyberman@bill.kbcard.com | Label_21, Label_23
- 18590cad879baf33 | openbanking@nonghyup.com | Label_18, Label_23

### Read-first (3)
- 19687abb53327512 | announcements@figma.com | Label_20
- 1955c4f84120a82d | announcements@figma.com | Label_20
- 1900a6006b286108 | announcements@figma.com | Label_20, Label_22

## manual triage batch A (use first 79 for the 100 target)
- source: `/Users/river/tools/gmail-agent-sys/tests/plans/manual_triage_batch_a_100_20260325.md`
- recommended selection: rows 1–79
- each row has message_id, thread_id, sender, subject, and recommended_state

## notes
- if you want the full 121-item apply set, take all 100 manual triage items + 21 safe closeout items.
- if you need strict 100, use safe 21 + first 79 of manual triage batch A.
