# Hook 계약 (Phase 4)

## 목적
Skill/Persona/운영 체크리스트 실행을 자동화하기 위해 컨텍스트 공유와 감사를 표준화한다.

## 현재 단계
- 실행 단계: 학습/준비(비파괴)
- 기본 모드: `pre/post` 상태 수집 + drift 경고
- 민감정보 마스킹 필수

## 지원 이벤트
- `SessionStart`
- `UserPromptSubmit`
- `PostToolUse`
- `Stop`
- `ErrorBoundary`(권장)

## 훅 실행 정책
- 기본 동작: `log_only=true`
- 실패해도 파이프라인 중단하지 않음(`fail_open=true`)
- 출력은 JSON 요약으로 제한
- 토큰/비밀 키/개인식별 패턴 마스킹

## 필수 산출
- Hook 실행 시 `status`, `warnings`, `missing` 또는 `audits`가 있는 JSON 요약 저장
- 경고 등급은 `warning|error` 구분

## 운영 훅 매핑
- `SessionStart` → `hooks/session_start.sh`
  - policy/config 존재성, 버전/레퍼런스 점검
- `UserPromptSubmit` → `hooks/user_prompt.sh`
  - Phase 전이, 금지 키워드, 대규모 변경 제안 감지
- `PostToolUse` → `hooks/post_tool_use.sh`
  - 스키마 영향도와 승인 대상 체크
- `Stop` → `hooks/stop_handoff.sh`
  - 다음 세션 요약 및 이행 항목 생성
- `ErrorBoundary` → `hooks/error_boundary.sh`
  - 민감정보 유출 패턴 경고 및 긴급 중단 플래그

## 실행 설정 파일
- `hooks/hooks.v3.json` (실행 레지스트리)
- `hooks/pre_context.md` (샘플 동작)
- `hooks/post_audit.sh` (샘플 감사 출력)

