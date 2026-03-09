# Backlog Scoreboard 2026-03-09

## Baseline
- `all_mail`: `11,410`
- `inbox`: `9,172`
- `has:nouserlabels`: `6,624`
- `has:userlabels`: `4,603`
- `trash_candidate`: `0`
- `trash_candidate_older_than_14d`: `0`

## Queue Status
| Queue | Rules | Window | Snapshot | Apply | Failures | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `bulk_low_value` | `rule_trash_candidate_sender`, `rule_trash_candidate_subject_guard`, `rule_promo` | `0~30d`, `31~180d` | complete (`0`, `0`) | n/a | `0` | 최근/중기 구간에서 추가 처리 후보 없음, `CNU` 공지 2건 보호됨 |
| `social_newsletter` | `rule_social_from`, `rule_social_subject_guard`, `rule_newsletter_from`, `rule_newsletter_subject_guard` | `0~365d`, `181~365d`, `366d+` | complete (`25`, `50`, `83`, `40`, `17`, `71`) | complete (`25`, `50`, `83`, `40`, `17`, `71`) | `0` | `phase10-social-newsletter-25-20260309`, `phase10-social-newsletter-50-20260310`, `phase10-social-newsletter-83-20260310`, `phase10-social-newsletter-residual-40-20260310`, `phase10-social-newsletter-17-181-365d-20260310`, `phase10-social-newsletter-71-366d-plus-20260310` 적용 완료 |
| `context_ops` | `rule_google_notification`, `rule_receipt`, `rule_travel` | `0~30d`, `31~180d`, `181~365d` | complete (`1`, `4`, `31`) | complete (`1`, `4`, `31`) | `0` | `snapshot-min-hours` + targeted fallback 차단 후 정상화, `이메일 확인 코드`는 `Security`로 보호됨, `181~365d` 네이버페이/영수증 31건 적용 완료 |
| `critical_review` | `rule_sys_security`, `rule_cnu_student`, `rule_cnu_notice`, `rule_cnu_otp` | all | partial (`10`) | partial (`10`) | `0` | `rule_cnu_notice` small batch 10건 적용 완료, `allow-critical` 검증 경로 확인 |
| `manual_residual` | residual unlabeled | all | sample `100` analyzed, focused snapshots `10`, `10`, `13`, `5`, `9`, `19` | partial (`10`, `10`, `13`, `5`, `9`, `19`) | `0` | 상위 도메인: `mail.notion.so`, `google.com`, `ted.com`, `cnu.ac.kr`; `Notion` support/marketplace 10건, `Apple` 가족공유 10건, `Notion newsletter` 13건, `Notion notify/team` 5건, `Apple storage` 9건, `finance-context` 19건 적용 완료 |

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
