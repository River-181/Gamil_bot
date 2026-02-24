# Skills & Hooks Integration Plan (v3)

## 1) 목적
Phase 4에서 Skill과 Hook을 연결해, `policy_normalization_v3.md` 기반 정책 정합성 검증을 팀·에이전트 간 공유 가능한 실행 체인으로 정착한다.

## 2) 역할 매핑

### Skill
- `gmail-policy-audit`
  - 실행 트리거: `SessionStart`, `Stop`에서 정책 무결성 점검
  - 핵심 검사: 라벨/필터 충돌, 우선순위 체인 준수
- `gmail-filter-lint`
  - 실행 트리거: 필터 변경 시(`PostToolUse`)
  - 핵심 검사: 중복 priority, 패턴 누락, 불명확 규칙
- `gmail-label-health`
  - 실행 트리거: 주간/월간 점검 루틴
  - 핵심 검사: 라벨 상한, 비활성 라벨, 중복 경로

### Hooks
- `SessionStart` → 컨텍스트 준비 + 필수 파일 존재성
- `UserPromptSubmit` → 비규정 키워드/phase 변경 감시
- `PostToolUse` → 스키마 영향 분석 + 위험 태그
- `Stop` → 다음 단계 전달사항 생성
- `ErrorBoundary` → 민감정보 유출 징후 경고

## 3) 데이터 계약
- Skill 출력은 JSON으로 통일.
- Hook 출력은 최소 요약 필드(`status`, `warnings`, `missing`) 유지.
- 모든 출력은 민감정보 마스킹 규칙 적용.

## 4) 실행 순서(학습 단계)
1. Phase 4 시작 시 `SessionStart`
2. 정책/설계 파일 변경 후 `PostToolUse`
3. `gmail-filter-lint` 결과를 `tests/plans/plan_checklist.md` 주석에 반영
4. 세션 종료 시 `Stop` 훅에서 다음 세션 handoff 생성

## 5) 승인 규칙
- `gmail-policy-audit` 또는 `gmail-filter-lint`가 `status: fail`이면 Phase 4/5 진행 보류
- `gmail-label-health`의 `status: warn`은 승인 가능(조건부)

## 6) 실행 경로 고정 (Phase 4 동결)
- Skill 계약 파일
  - `skills/gmail-policy-audit/SKILL.md`
  - `skills/gmail-filter-lint/SKILL.md`
  - `skills/gmail-label-health/SKILL.md`
- Hook 실행 레지스트리
  - `hooks/hooks.v3.json`
- Hook 스크립트
  - `hooks/session_start.sh`
  - `hooks/user_prompt.sh`
  - `hooks/post_tool_use.sh`
  - `hooks/stop_handoff.sh`
  - `hooks/error_boundary.sh`

## 7) 고정 오케스트레이션 체인
1. `SessionStart` 실행 후 `gmail-policy-audit` 기준 파일 정합성 점검
2. 사용자 요청 처리 단계에서 `UserPromptSubmit`로 위험 키워드/phase 전이 감시
3. 정책 파일(`config/*.json`, `docs/*.md`) 변경 직후 `PostToolUse` 실행
4. `PostToolUse` 이후 `gmail-filter-lint` 수행, 결과 `status`를 체크리스트에 반영
5. 세션 종료 시 `Stop` 훅으로 handoff 항목 생성
6. 예외 발생 시 `ErrorBoundary`로 민감정보 패턴 탐지 및 경고 생성

## 8) 동결 규칙
- 훅 가드 정책은 `mask_sensitive=true`, `log_only=true`, `fail_open=true`를 유지
- Skill 결과 상태값은 `pass|warn|fail` 외 확장 금지
- Phase 5 전까지 apply 성격 실행 금지(`plan-only`/`dry-run`만 허용)
