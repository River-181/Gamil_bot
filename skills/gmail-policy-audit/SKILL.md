# Skill: gmail-policy-audit

## 목적
v3 정책 문서와 실행 정책(JSON) 간 일치성 및 위험도를 평가한다.

## 입력
- `docs/policy_normalization_v3.md`
- `docs/strategy_v3.md`
- `config/labels.v3.json`
- `config/filters.v3.json`

## 출력
- JSON (필수 필드):
  - `policy_sha`: 문자열
  - `labels_found`: 정규 라벨 개수
  - `filters_found`: 정규 필터 개수
  - `violations`: 배열
  - `risks`: `[{severity, id, message}]`
  - `drift`: `{labels:[], filters:[], conflict_rules:[]}`
  - `recommendations`: 우선순위 정렬 문자열 배열
  - `status`: `pass | warn | fail`

## 핵심 규칙
- 보안 라벨(`@SYS/Security`)은 존재해야 함
- 라벨 수는 15개 이하
- 필터 `priority`는 정수이며 작을수록 선행
- 동일 조건의 중복 규칙은 `mutual_exclusive_group` 또는 `conflict_with`로 설명

## 실행 동작
1. 스키마 검증: `labels.schema.json`, `filters.schema.json` 통과
2. `labels.v3.json`와 `filters.v3.json`을 정책(`policy_normalization_v3.md`)와 매핑
3. 우선순위 체인/충돌 규칙 평가
4. `drift_check(snapshot, policy)` 결과 반환

## 계약 인터페이스(정의)
- `run(policy_path, labels_path, filters_path, options={})`
- `run` 반환:
  - `{status, checks:[{name, result}], score, risks}`
- 실행 제약:
  - `dry_run_only` 모드 기본값 true
  - 실패 시 `status: fail` 및 `error_context` 포함

## 출력 예시
```json
{
  "status": "pass",
  "policy_sha": "sha256:...",
  "labels_found": 14,
  "filters_found": 12,
  "violations": [],
  "risks": [],
  "drift": {"labels":[], "filters":[], "conflict_rules":[]},
  "recommendations": ["none"],
  "score": 100
}
```
