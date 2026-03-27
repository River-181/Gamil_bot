# Gmail-Agent-SYS Milestones v3.2

## 목적
- `has:nouserlabels -> 0`을 주축으로 backlog를 단계적으로 제거한다.
- Gmail 메인 `기타` 체감량은 위 목표의 결과로 함께 감소시키고, 신규 유입은 일일 운영으로 `0` 유지 상태에 수렴시킨다.

## 기준선
- `all_mail`: `11,402`
- `inbox`: `9,664`
- `has:nouserlabels`: `7,120`
- `has:userlabels`: `4,158`
- 정책 기준:
  - `15 labels`
  - `15 filters`
  - `@AUTO/TrashCandidate` `14일 보존`

## Queue 모델
- `bulk_low_value`
  - `rule_trash_candidate_sender`
  - `rule_trash_candidate_subject_guard`
  - `rule_promo`
- `social_newsletter`
  - `rule_social_from`
  - `rule_social_subject_guard`
  - `rule_newsletter_from`
  - `rule_newsletter_subject_guard`
- `context_ops`
  - `rule_google_notification`
  - `rule_receipt`
  - `rule_travel`
- `critical_review`
  - `rule_sys_security`
  - `rule_cnu_student`
  - `rule_cnu_notice`
  - `rule_cnu_otp`
- `manual_residual`
  - rule-family queue 소진 후 남는 수동 조사 대상

## 마일스톤
### M8-A. Targeted Snapshot 안정화
- 각 queue에서 `25/50` snapshot 생성 2회 연속 성공
- 기록 항목:
  - `selected_candidates`
  - `protected_skips`
  - `self_sent_skips`
  - 생성 시간

### M8-B. Apply Throughput 확보
- `bulk_low_value`, `social_newsletter`, `context_ops` 각 queue에서 `50 -> 200` apply 성공
- 통과 기준:
  - 실패율 `<= 2%`
  - self-sent 변경 `0`
  - critical 오분류 `0`

### M8-C. Mid/Old backlog drain
- `31~180d`, `181~365d`, `366d+` 구간에 대해 `200 -> 500` 반복 적용
- queue별 journal 누락 `0`
- rollback 가능 상태 유지

### M9. Zero-Unlabeled
- rule-family queue를 모두 소진한 뒤 `manual_residual`만 남게 만든다.
- 최종 목표:
  - `has:nouserlabels = 0`

### M10. Zero-Other steady state
- 최근 `0~7d` queue를 일일 운영 루틴으로 고정
- 신규 유입 메일은 일일 batch 후 `기타 0` 유지

### M11. Residual Rule Expansion
- 현재 live residual `201`은 기존 lane rule set으로는 `0`건이므로 coverage refresh가 필요하다.
- 작업:
  1. `Security-first` / `Read-first` / `Reference-first` / `Manual-Work` rule coverage 재점검
  2. 남은 residual을 설명할 새 sender / subject family만 추가
  3. lane별 snapshot을 다시 만든다
- 통과 기준:
  - lane snapshot에서 최소 1개 이상 residual hit 확인
  - residual 201에 대한 커버리지 설명 완료

### M12. Final Residual Closeout
- coverage refresh 이후 남은 residual을 전부 apply한다.
- 통과 기준:
  - `has:nouserlabels = 0`
  - apply-ready 묶음 전체 회수 완료
  - security lane 누락 0

### M13. Steady-State Handoff
- unlabeled closeout 이후 신규 유입만 다루는 daily lane 운영으로 전환한다.
- 통과 기준:
  - 신규 메일이 small queue로만 처리됨
  - 새 auto rule 추가 없음
  - manual/work는 thread 기반으로만 review

## 운영 가드
- 운영 기본경로는 `build-snapshot -> apply-snapshot -> trash-commit`
- direct `--apply-batch`는 유지되더라도 표준 경로로 쓰지 않는다.
- `@AUTO/TrashCandidate`는 `older_than:14d` 전에는 `TRASH`로 보내지 않는다.
- `manual_residual`은 자동 queue가 아니라 수동 분류/규칙 보강 대상으로만 취급한다.

## 연결 문서
- `/Users/river/tools/gmail-agent-sys/docs/phase10_notes_01_snapshot_apply_trash.md`
- `/Users/river/tools/gmail-agent-sys/docs/phase10_notes_02_bulk_targeting_and_false_positive.md`
- `/Users/river/tools/gmail-agent-sys/docs/runbooks/rule_family_snapshot_runbook.md`
- `/Users/river/tools/gmail-agent-sys/tests/plans/final_residual_closeout_201_20260324.md`
