# Phase 10 Notes 02: bulk targeting, false positive, 예외 규칙

## 현재까지 확인된 사실
- 최근 30일 기준:
  - 저위험 snapshot 50 결과는 `17건` 적용
  - 분포는 `TrashCandidate 12`, `Social 2`, `Notification 2`, `Newsletter 1`
- `31~180일` targeted bulk snapshot은 `200건`까지 채워진다.
- backlog 분포는 `LinkedIn/Social` 비중이 매우 높다.

## TrashCandidate 운영 원칙
- 초기 sender registry는 반복 확인된 commercial bulk sender만 포함한다.
- 새 발신자는 바로 TrashCandidate로 올리지 않는다.
- 처음에는 `Promo` 또는 기존 분류로 받고, 샘플 리뷰 후 sender registry에 승격한다.

## 현재 예외로 막은 항목
- 금융/카드/대출 계열:
  - `hanacard`
  - `하나카드`
  - `kbcard`
  - `국민카드`
  - `카드`
  - `loan`
  - `대출`
- 보안/계정/영수증/예약/학교 메일은 기존 exclude 패턴으로 차단

## 오탐/경계 사례
- `(광고)[하나카드] 내게 맞는 최저금리 대출`
  - 초기에는 TrashCandidate로 잡혔음
  - 이후 금융 예외 패턴 추가로 완화
- LinkedIn 일부 메일
  - `rule_social_from`와 `rule_newsletter_subject_guard`가 동시에 잡히는 케이스가 있음
  - 운영상 우선 판단은 `Social`
  - 후속 개선 시 LinkedIn 발신자에 대해 newsletter subject guard 예외를 추가하는 것이 바람직함

## targeted snapshot 전략
- 전체 snapshot 200보다 `bulk 규칙군 전용 snapshot 200`이 더 실용적이다.
- 운영 queue 고정:
  - `bulk_low_value`: `rule_trash_candidate_sender`, `rule_trash_candidate_subject_guard`, `rule_promo`
  - `social_newsletter`: `rule_social_from`, `rule_social_subject_guard`, `rule_newsletter_from`, `rule_newsletter_subject_guard`
  - `context_ops`: `rule_google_notification`, `rule_receipt`, `rule_travel`
  - `critical_review`: `rule_sys_security`, `rule_cnu_student`, `rule_cnu_notice`, `rule_cnu_otp`
  - `manual_residual`: rule-family queue 소진 후 수동 조사

## 배치 확대 기준
- 최근 구간:
  - `25`: 실행 경로 검증
  - `50`: queue 단위 샘플 적용
  - `200`: 최근 메일 일상 운영
- 중기/장기 구간:
  - `50`: queue 시동
  - `200`: backlog drain 시작
  - `500`: 두 번 연속 정상 종료 후 허용

## 후속 개선 후보
- LinkedIn -> Newsletter 오탐 예외 추가
- TrashCandidate sender registry 주기적 정리
- `31~180d`, `181d+`용 snapshot 템플릿 명령을 runbook으로 분리
