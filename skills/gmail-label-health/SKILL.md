# Skill: gmail-label-health

## 목적
라벨 트리의 일관성 및 상태 분포를 점검한다.

## 입력
- `config/labels.v3.json`
- Gmail 샘플 메타데이터(운영시)

## 출력
- 라벨 건강 리포트
  - `status`: `pass | warn | fail`
  - `label_count`
  - `dead_labels`
  - `unused_labels`
  - `dup_path_count`
  - `cleanup_recommendations`

## 체크 항목
- 라벨 총수 <= 15
- 라벨 경로 중복/포맷 오류 없음 (`@카테고리/하위`)
- `@GTD` 계열 수동 운영 적합성(과도한 세분화 여부)
- `source_rule_ref` 누락 라벨 탐지

## 실행 인터페이스(정의)
- `drift_check(snapshot, policy)`
- `label_usage_summary(snapshot, window_days=30)`
- `recommend_cleanup(top_n=5)`

## 운영 제약
- `dead_labels`는 비활성 라벨 + 참조 누락 라벨만 포함
- `status: fail`일 때는 Phase 2 라벨 사양 조정 우선 제안
- 추천 목록에는 `id`, `reason`, `impact` 포함

## 반환 예시
```json
{
  "status": "pass",
  "label_count": 14,
  "dead_labels": [],
  "unused_labels": [],
  "dup_path_count": 0,
  "cleanup_recommendations": []
}
```
