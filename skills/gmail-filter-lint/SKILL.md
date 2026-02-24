# Skill: gmail-filter-lint

## 목적
Gmail 필터 규칙을 실행 전에 정적 검사한다.

## 입력
- `config/filters.v3.json`

## 출력
- lint JSON
  - `status`: `pass | warn | fail`
  - `errors`: 치명 이슈 목록
  - `warnings`: 동작상 충돌 가능성 목록
  - `notices`: 권장 개선사항
  - `summary`: `{total, blocking, warning_count}`

## 규칙
- 필수 필드 검증: `id`, `name`, `priority`, `from_patterns`, `actions.apply_labels`
- 최소 패턴 보장: `from_patterns` 또는 `subject_patterns` 중 하나는 필수
- 우선순위 정렬: 중복 priority 존재 시 경고
- `from_patterns`가 와일드카드 기반(`*`)인 규칙은 `notes`로 보조 규칙 명시
- `mutual_exclusive_group` 존재 규칙과 `conflict_with` 규칙의 교차점 추적

## 실행 인터페이스(정의)
- `lint(config_path, *, allow_wildcard=false)`
- `export_diagnostics(filter_id)`
- `rank_conflicts(top_n=20)`
- `simulate_match(sample)`

## 실행 제약
- `status: pass`가 아니면 Phase 4 후속 단계(테스트 플랜)에서 승인 보류
- 치명 오류(`errors`) 1건 이상이면 즉시 중단

## 반환 예시
```json
{
  "status": "warn",
  "errors": [],
  "warnings": ["Duplicate priority among group news_group"],
  "notices": ["Consider tightening wildcard rule_newsletter_subject_guard"],
  "summary": {"total": 12, "blocking": 0, "warning_count": 2}
}
```
