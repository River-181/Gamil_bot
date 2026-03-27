# minimal safe bulk slice 2026-03-25

## conclusion
- 지금 남은 residual에서 **가장 작고 안전하게 bulk apply 할 수 있는 slice는 `Read-first`**이다.
- 그 다음은 `Reference-first`이며, `Security-first`는 bulk slice보다는 별도 high-priority lane으로 다루는 편이 안전하다.
- `manual/work residual`은 bulk apply 대상이 아니다.

## evidence
- `manual_review_batches_21_30_summary_20260324.md`에서 `21~23` 구간은 이미 lane 구조가 수렴했다.
  - `Read-first`
  - `Reference-first`
  - `Security-first`
  - minor `Waiting/Action`
- `read_first_bulk_rule_v1.md`
  - newsletter / digest / content성 메일은 `@GTD/Read`가 기본값이다.
- `reference_first_bulk_rule_v1.md`
  - 서비스 알림 / 영수증 / 예약 / 플랫폼 업데이트는 `@GTD/Reference`가 기본값이다.
- `security_first_bulk_rule_v1.md`
  - login / verification / password reset / account notice는 `@SYS/Security`가 기본값이다.

## smallest safe bulk apply slice
### 1. Read-first
- 대상:
  - newsletter
  - article digest
  - launch/update content
  - recurring informational content
- 이유:
  - 운영 리스크가 가장 낮고, `Read`로의 압축 규칙이 가장 안정적이다.

### 2. Reference-first
- 대상:
  - service notice
  - product update
  - receipt / statement
  - booking / shipping / fulfillment
  - collaboration notice
- 이유:
  - bulk apply는 가능하지만, `Action/Waiting` 예외를 한 번 더 확인하는 게 좋다.

### 3. Security-first
- 대상:
  - login alert
  - verification
  - password reset
  - account notice
- 이유:
  - 우선순위는 가장 높지만 bulk-size 관점에서는 별도 lane이 더 안전하다.

## exclusion
- `manual/work residual`
- `self-thread / self-reference`
- 직접 계약 / 제출 / 행정 회신
- 새 sender rule 추가

## next action
- `Read-first`를 먼저 bulk apply
- 그 다음 `Reference-first`
- `Security-first`는 별도 확인 후 적용

## apply-ready 50-item slice
- bulk-safe core:
  - `Read-first` `5`
  - `Reference-first` `10`
  - `Security-first` `5`
- non-bulk remainder:
  - `manual/work` `20`
  - `self-thread` `10`
- decision:
  - 이 50개 묶음에서 실제 bulk apply 우선순위는 `Read-first -> Reference-first -> Security-first`다.
  - `manual/work`와 `self-thread`는 bulk apply가 아니라 thread-level triage로 남긴다.
