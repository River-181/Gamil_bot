# Gmail-Agent-SYS v3 정책 정규화(동결본)

> 기준 골조: `/Users/river/tools/gmail-agent-sys/20260224_김주용_이메일시스템_마스터설계서_v3.md`

## 1) 적용 원칙
- 이 문서는 Phase 2 종료 시점을 위한 정규화 기준이자 변경 불가 동결본이다.
- 실행은 다음 phase에서 plan-only 검증 후에만 허용한다.
- 라벨 수는 `14개`, 상한은 `15개`(변경 불가).
- 필터 수는 `13개`로 고정한다(구현본 기준).
- OpenClaw/외부 자동화 실행은 Phase 3+로 이동한다.
- 정합성 검증은 스키마 + 결정 규칙 + 충돌 정책이 모두 통과한 경우만 통과로 본다.

## 2) 라벨 정합본 (`config/labels.v3.json`)

### 2-1. 라벨 집합
| 카테고리 | 라벨 | id | kind | source_rule_ref |
|---|---|---|---|---|
| GTD | `@GTD/Action` | `state_action` | STATE | `manual_state` |
| GTD | `@GTD/Waiting` | `state_waiting` | STATE | `manual_state` |
| GTD | `@GTD/Reference` | `state_reference` | STATE | `manual_state` |
| GTD | `@GTD/Read` | `state_read` | STATE | `manual_state` |
| CNU | `@CNU/학생` | `cnu_student` | CTX | `rule_cnu_student` |
| CNU | `@CNU/뉴스알림` | `cnu_news` | CTX | `rule_cnu_notice` |
| CTX | `@CTX/Travel` | `ctx_travel` | CTX | `rule_travel` |
| CTX | `@CTX/Finance` | `ctx_finance` | CTX | `rule_receipt` |
| AUTO | `@AUTO/Newsletter` | `auto_newsletter` | AUTO | `rule_newsletter_from`, `rule_newsletter_subject_guard` |
| AUTO | `@AUTO/Receipt` | `auto_receipt` | AUTO | `rule_receipt` |
| AUTO | `@AUTO/Notification` | `auto_notification` | AUTO | `rule_notification`, `rule_google_notification` |
| AUTO | `@AUTO/Social` | `auto_social` | AUTO | `rule_social_from`, `rule_social_subject_guard` |
| AUTO | `@AUTO/Promo` | `auto_promo` | AUTO | `rule_promo` |
| SYS | `@SYS/Security` | `sys_security` | SYS | `rule_sys_security`, `rule_cnu_otp` |

### 2-2. 스키마 제약(필수)
- `version`: `v3.0.0`
- `path` 정합성: depth 2~3 허용 (`@GROUP/Label` 형식)
- `source_rule_ref` 존재: 필수
  - STATE 라벨: 오직 `manual_state` 단일 참조만 허용
  - 그 외 라벨: `manual_state` 직접 참조 불가
- `caps`:
  - `inbox_priority`, `requires_review` 필수
  - `max_depth`는 1~3 범위
  - `is_system` / `state_tag`는 의미론적 정합점검 대상
- 라벨 총수는 15개 초과 불가

## 3) 필터 정합본 (`config/filters.v3.json`)

### 3-1. ID, 우선순위
1. `rule_sys_security` (priority 10)
2. `rule_cnu_otp` (20)
3. `rule_cnu_student` (30)
4. `rule_cnu_notice` (40)
5. `rule_receipt` (50)
6. `rule_travel` (60)
7. `rule_social_from` (70)
8. `rule_social_subject_guard` (71)
9. `rule_promo` (80)
10. `rule_newsletter_from` (90)
11. `rule_newsletter_subject_guard` (91)
12. `rule_google_notification` (95)
13. `rule_notification` (99)

### 3-2. 필수 형식
- `from_patterns` 또는 `subject_patterns`는 최소 1개 이상.
- `actions.apply_labels`는 최소 1개.
- `skip_inbox`/`apply_labels`는 공존 가능.
- `priority` 작을수록 먼저 적용.

### 3-3. 충돌 후보 정합
- `cnu_scope`: `rule_cnu_student`, `rule_cnu_notice`, `rule_cnu_otp`
- `social_group`: `rule_social_from`, `rule_social_subject_guard`
- `news_group`: `rule_newsletter_from`, `rule_newsletter_subject_guard`
- `notification_group`: `rule_google_notification`, `rule_notification`

## 4) 고정 충돌/우선순위 비교기
동일 메일이 다중 매칭할 때 최종 라벨링은 아래 comparator로 고정한다.
1. `priority` 오름차순
2. `mutual_exclusive_group` 존재 시 해당 그룹 규칙 우선 적용
3. `kind` 우선순위:
   - SYS > CTX > AUTO > STATE
4. 동일 우선순위 교집합 충돌 시:
   - `source_rule_ref` 사전순
   - 최종 tie: rule id 사전순

동일 priority에서 동일 규칙군이 다중 충돌하면 즉시 P1 블로커.

## 5) 고정 운영 규칙
1. `@SYS/Security`은 상시 보존 라벨로 취급.
2. 수동 상태 라벨(`@GTD/*`)은 시스템 자동규칙이 오버라이트하지 않는다.
3. `skip_inbox=true` + `star=true` 조합은 허용한다.
4. Phase2 산출물 외 임시 라벨/필터 규칙(`rule_gtd_state_apply` 등) 추가 금지.
5. 라벨/필터 변경은 plan-only + 리뷰 승인 없이는 반영하지 않는다.

## 6) 변경금지 체크리스트
- 14개 라벨/12개 필터 고정
- priority 체인 및 그룹 충돌 규칙 고정
- source_rule_ref 정합성 고정
- 스키마/문서 일치 상태에서만 상위 phase 진입

## 7) 시나리오 샘플(문서 기준)
- SYS vs CNU: `rule_sys_security`와 모든 CNU 후보는 SYS 우선.
- CNU 중복: `rule_cnu_student`/`rule_cnu_notice`는 그룹 내 우선순위로 1개만 적용.
- 뉴스레터 중복: `rule_newsletter_from`(90) > `rule_newsletter_subject_guard`(91)로 고정.
- 소셜 중복: `rule_social_from`(70) > `rule_social_subject_guard`(71)로 고정.
