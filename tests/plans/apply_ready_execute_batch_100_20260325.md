# Apply-ready batch (Read/Reference/Security only) — 2026-03-25

## Summary
- Goal: build the smallest safe apply-ready batch from existing `Read-first`, `Reference-first`, `Security-first` lanes.
- Result: `21` candidates available (less than 100). Lanes with `0` are marked exhausted and not expanded.

## Exhausted lanes
- Read-first: `0` candidates in `/Users/river/tools/gmail-agent-sys/.tokens/closeout_read_reference_50.json`.
- Security-tail: `0` candidates in `/Users/river/tools/gmail-agent-sys/.tokens/closeout_security_tail_50_20260325.json`.
- Manual/work and school lanes are out of scope for this batch and remain manual.

## Apply-ready candidates (total 21)

### Security-first (9)
Source: `/Users/river/tools/gmail-agent-sys/.tokens/closeout_security_senders_50.json`

- message_id: `19575623ab05084c` | sender: `workspace-noreply@google.com` | subject: `cnu-psy-stu.notion.site의 Google Workspace Business Standard 평가판 사용 기간이 종료됨` | recommended: `Label_18` | rule: `rule_google_notification`
- message_id: `1955ba26d31760cf` | sender: `workspace-noreply@google.com` | subject: `cnu-psy-stu.notion.site의 Google Workspace Business Standard 평가판 사용 기간이 종료됨` | recommended: `Label_18` | rule: `rule_google_notification`
- message_id: `195326e9e1dd6e95` | sender: `workspace-noreply@google.com` | subject: `3일 내에 cnu-psy-stu.notion.site의 Google Workspace 설정을 완료해야 함` | recommended: `Label_18` | rule: `rule_google_notification`
- message_id: `19522fb8eac04dfd` | sender: `workspace-noreply@google.com` | subject: `cnu-psy-stu.notion.site의 Google Workspace 설정에 대한 도움 받기` | recommended: `Label_18` | rule: `rule_google_notification`
- message_id: `19518aed92322d36` | sender: `workspace-noreply@google.com` | subject: `cnu-psy-stu.notion.site의 Google Workspace 설정하기` | recommended: `Label_18` | rule: `rule_google_notification`
- message_id: `19513ad1bca11ab6` | sender: `workspace-noreply@google.com` | subject: `Welcome to Google Workspace. See what you can do.` | recommended: `Label_18` | rule: `rule_google_notification`
- message_id: `1917bc160459e147` | sender: `workspace-noreply@google.com` | subject: `[Reminder] Jamboard application wind down` | recommended: `Label_18` | rule: `rule_google_notification`
- message_id: `18e68d0d9c54718a` | sender: `workspace-noreply@google.com` | subject: `[Reminder] Jamboard application wind down` | recommended: `Label_18` | rule: `rule_google_notification`
- message_id: `18ae048b0b6a8665` | sender: `workspace-noreply@google.com` | subject: `[조치 권장] Jamboard 애플리케이션 지원 중단` | recommended: `Label_18` | rule: `rule_google_notification`

### Reference-first (finance/commerce) (9)
Source: `/Users/river/tools/gmail-agent-sys/.tokens/closeout_finance_50_20260325.json`

- message_id: `1971e9b057dbc794` | sender: `cyberman@bill.kbcard.com` | subject: `(KB국민카드) 김*용님 2025년06월 명세서` | recommended: `Label_21, Label_23` | rule: `rule_receipt`
- message_id: `196b2e596ad339f2` | sender: `cyberman@bill.kbcard.com` | subject: `(KB국민카드) 김주용님 2025년04월 KB국민체크카드 내역서` | recommended: `Label_21, Label_23` | rule: `rule_receipt`
- message_id: `19618c84d48feff4` | sender: `cyberman@bill.kbcard.com` | subject: `(KB국민카드) 김주용님 2025년03월 KB국민체크카드 내역서` | recommended: `Label_21, Label_23` | rule: `rule_receipt`
- message_id: `195eea0d501b5f04` | sender: `cyberman@bill.kbcard.com` | subject: `(KB국민카드) 김*용님 2025년04월 명세서` | recommended: `Label_21, Label_23` | rule: `rule_receipt`
- message_id: `19583505160c9aac` | sender: `cyberman@bill.kbcard.com` | subject: `(KB국민카드) 김주용님 2025년02월 KB국민체크카드 내역서` | recommended: `Label_21, Label_23` | rule: `rule_receipt`
- message_id: `19564c02f51ebed5` | sender: `cyberman@bill.kbcard.com` | subject: `(KB국민카드) 김*용님 2025년03월 명세서` | recommended: `Label_21, Label_23` | rule: `rule_receipt`
- message_id: `1944927b3a76d146` | sender: `cyberman@bill.kbcard.com` | subject: `(KB국민카드) 김주용님 2024년12월 KB국민체크카드 내역서` | recommended: `Label_21, Label_23` | rule: `rule_receipt`
- message_id: `193aec9b7609200e` | sender: `cyberman@bill.kbcard.com` | subject: `(KB국민카드) 김주용님 2024년11월 KB국민체크카드 내역서` | recommended: `Label_21, Label_23` | rule: `rule_receipt`
- message_id: `18590cad879baf33` | sender: `openbanking@nonghyup.com` | subject: `2023년 4분기 오픈뱅킹 금융거래정보 제공사실 안내(농·축협)` | recommended: `Label_18, Label_23` | rule: `rule_finance_notice`

### Read-first (newsletter/platform) (3)
Source: `/Users/river/tools/gmail-agent-sys/.tokens/closeout_platform_50_20260325.json`

- message_id: `19687abb53327512` | sender: `announcements@figma.com` | subject: `One week until Config 👀` | recommended: `Label_20` | rule: `rule_newsletter_from`
- message_id: `1955c4f84120a82d` | sender: `announcements@figma.com` | subject: `Ready to level up?` | recommended: `Label_20` | rule: `rule_newsletter_from`
- message_id: `1900a6006b286108` | sender: `announcements@figma.com` | subject: `Config 2024 초대장을 메일에서 확인하세요` | recommended: `Label_20, Label_22` | rule: `rule_social_subject_guard, rule_newsletter_from`

## Notes
- Total candidates available: `21`.
- No expansion beyond these lanes was performed.
- If any of the above snapshots were already applied, treat that lane as exhausted and do not reapply.
