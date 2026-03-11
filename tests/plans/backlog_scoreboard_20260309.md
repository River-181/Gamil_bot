# Backlog Scoreboard 2026-03-09

## Baseline
- Historical baseline (`2026-03-09`): `all_mail`: `11,419`, `inbox`: `8,873`, `has:nouserlabels`: `6,313`, `has:userlabels`: `4,923`
- Latest checkpoint (`2026-03-11`): `all_mail`: `11,434`, `inbox`: `8,741`, `has:nouserlabels`: `6,137`, `has:userlabels`: `5,114`
- `trash_candidate`: `0`
- `trash_candidate_older_than_14d`: `0`

## Queue Status
| Queue | Rules | Window | Snapshot | Apply | Failures | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `bulk_low_value` | `rule_trash_candidate_sender`, `rule_trash_candidate_subject_guard`, `rule_promo` | `0~30d`, `31~180d` | complete (`0`, `0`) | n/a | `0` | 최근/중기 구간에서 추가 처리 후보 없음, `CNU` 공지 2건 보호됨 |
| `social_newsletter` | `rule_social_from`, `rule_social_subject_guard`, `rule_newsletter_from`, `rule_newsletter_subject_guard` | `0~365d`, `181~365d`, `366d+` | complete (`25`, `50`, `83`, `40`, `17`, `71`) | complete (`25`, `50`, `83`, `40`, `17`, `71`) | `0` | `phase10-social-newsletter-25-20260309`, `phase10-social-newsletter-50-20260310`, `phase10-social-newsletter-83-20260310`, `phase10-social-newsletter-residual-40-20260310`, `phase10-social-newsletter-17-181-365d-20260310`, `phase10-social-newsletter-71-366d-plus-20260310` 적용 완료 |
| `context_ops` | `rule_google_notification`, `rule_receipt`, `rule_travel` | `0~30d`, `31~180d`, `181~365d` | complete (`1`, `4`, `31`) | complete (`1`, `4`, `31`) | `0` | `snapshot-min-hours` + targeted fallback 차단 후 정상화, `이메일 확인 코드`는 `Security`로 보호됨, `181~365d` 네이버페이/영수증 31건 적용 완료 |
| `critical_review` | `rule_sys_security`, `rule_cnu_student`, `rule_cnu_notice`, `rule_cnu_otp` | all | partial (`10`, `20`) | partial (`10`, `20`) | `0` | `rule_cnu_notice` small batch 10건 + sender-targeted 20건 적용 완료, `allow-critical` 검증 경로 확인 |
| `manual_residual` | residual unlabeled | all | sample `100` analyzed, focused snapshots `10`, `10`, `13`, `5`, `9`, `19`, `15`, `10`, `16`, `9`, `7`, `5`, `3`, `2`, `10`, `3`, `20`, `20`, `20`, `20`, `10`, `11` | partial (`10`, `10`, `13`, `5`, `9`, `19`, `15`, `10`, `16`, `9`, `7`, `5`, `3`, `2`, `10`, `3`, `20`, `20`, `20`, `20`, `7/10`, `11`) | `1` | 최근 상위 도메인: `cnu.ac.kr`, `naver.com`, `kyobobook.com`, `google.com`, `ted.com`, `mail.instagram.com`; `Notion` support/marketplace 10건, `Apple` 가족공유 10건, `Notion newsletter` 13건, `Notion notify/team` 5건, `Apple storage` 9건, `finance-context` 19건, `Notion notify` 15건, `Medium` 10건, `GitHub residual` 16건, `Notion notify v3` 9건, `Google residual` 7건, `Facebook memories` 5건, `CNU critical review` 3건, `Stripe finance` 2건, `mymind` 10건, `OpenAI/Claude residual` 3건, residual bundle 20건 x2, sender-targeted bundle 20건 x2, sender-targeted bundle C는 `7/10` 적용 후 Gmail `FAILED_PRECONDITION` 1건 발생, longtail sender 11건 적용 완료 |
| `bulk_low_value (phase11)` | `rule_trash_candidate_sender`, `rule_trash_candidate_subject_guard`, `rule_promo` | `31~180d` | snapshot (`200`) | `0` | `0` | `2026-03-11` 기준 신규 스캔 결과 0건, `CNU` 보호 3건 |
| `social_newsletter (phase11)` | `rule_social_from`, `rule_social_subject_guard`, `rule_newsletter_from`, `rule_newsletter_subject_guard` | `31~180d` | snapshot (`50`) | `0` | `0` | `2026-03-11` 기준 0건, `2026-03-10` 이전 적용 이력 유지 |
| `bulk_low_value (phase11)` | `rule_trash_candidate_sender`, `rule_trash_candidate_subject_guard`, `rule_promo` | `181~365d` | snapshot (`50`) | `0` | `0` | `2026-03-11` 기준 0건, `CNU` 보호 1건 |
| `social_newsletter (phase11)` | `rule_social_from`, `rule_social_subject_guard`, `rule_newsletter_from`, `rule_newsletter_subject_guard` | `181~365d` | snapshot (`50`) | `0` | `0` | `2026-03-11` 기준 0건 |
| `bulk_low_value (phase11)` | `rule_trash_candidate_sender`, `rule_trash_candidate_subject_guard`, `rule_promo` | `365d+` | snapshot (`50`) | `0` | `0` | `2026-03-11` 기준 0건, `CNU` 보호 1건 |
| `social_newsletter (phase11)` | `rule_social_from`, `rule_social_subject_guard`, `rule_newsletter_from`, `rule_newsletter_subject_guard` | `365d+` | snapshot (`50`) | `0` | `0` | `2026-03-11` 기준 0건 |
| `context_ops (phase11)` | `rule_google_notification`, `rule_receipt`, `rule_travel` | `365d+` | snapshot (`50`) | `0` | `0` | `2026-03-11` 기준 0건 |
| `context_ops (phase11)` | `rule_google_notification`, `rule_receipt`, `rule_travel` | `31~365d` | snapshot (`200` + `200`) | `0` | `0` | `2026-03-11` 기준 0건, 보안 라벨 스킵 6건 |
| `manual_residual (phase11)` | `rule_sys_security`, `rule_apple_notification`, `rule_notion_notification`, `rule_notification` (critical-review union) | all | `snapshot (300)` | `39` | `0` | `2026-03-11` 기준 `allow-critical` 기반 39건 적용 완료, rollback 준비 `true` |

## Throughput Gates
- `M8-A`
  - queue 3종에서 `25/50` snapshot 2회 연속 성공
- `M8-B`
  - queue 3종에서 `50 -> 200` apply 성공
  - self-sent 변경 `0`
  - critical 오분류 `0`
- `M8-C`
  - `31~180d`, `181~365d`, `366d+` 구간에서 `200 -> 500` 반복

## Acceptance Tracking
- `M9 / Zero-Unlabeled`: `7,120 -> 6,313 -> 6,176 -> 6,137` (2026-03-11 latest checkpoint), 목표 `0`
- `M10 / Zero-Other steady state`: 최근 `0~7d` 일일 운영 고정
