# Backlog Scoreboard 2026-03-09

## Baseline
- `all_mail`: `11,227`
- `inbox`: `9,575`
- `has:nouserlabels`: `7,027`
- `has:userlabels`: `4,200`
- `trash_candidate`: `8`
- `trash_candidate_older_than_14d`: `0`

## Queue Status
| Queue | Rules | Window | Snapshot | Apply | Failures | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `bulk_low_value` | `rule_trash_candidate_sender`, `rule_trash_candidate_subject_guard`, `rule_promo` | `0~30d` | pending | pending | `0` | `TrashCandidate`는 `14일 보존` |
| `social_newsletter` | `rule_social_from`, `rule_social_subject_guard`, `rule_newsletter_from`, `rule_newsletter_subject_guard` | `0~180d` | complete (`25`) | complete (`25`) | `0` | `phase10-social-newsletter-25-20260309` 적용 완료 |
| `context_ops` | `rule_google_notification`, `rule_receipt`, `rule_travel` | `0~30d`, `31~180d` | blocked | pending | `0` | `snapshot-min-hours` 추가 후에도 metadata fetch 병목 남음 |
| `critical_review` | `rule_sys_security`, `rule_cnu_student`, `rule_cnu_notice`, `rule_cnu_otp` | all | review only | n/a | `0` | `--allow-critical` 필요 |
| `manual_residual` | residual unlabeled | all | pending | pending | n/a | rule-family queue 소진 후 진입 |

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
- `M9 / Zero-Unlabeled`: `7,120 -> 0`
- `M10 / Zero-Other steady state`: 최근 `0~7d` 일일 운영 고정
