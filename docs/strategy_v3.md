# Gmail 운영 전략 v3 (GTD 통합 버전)

## 핵심 공식
- 이메일은 `Context + State`로 해석한다.
- `Context`: 라벨의 축 (`@GTD`, `@CNU`, `@CTX`, `@AUTO`, `@SYS`)
- `State`: 수동 처리 상태 (`Action/Waiting/Reference/Read`)

## Phase 2 정규화 요약
- 기준 정책: `docs/policy_normalization_v3.md`
- 라벨: v3 14개 라벨 고정
- 필터: 13개 규칙 고정
- 충돌: `@SYS` 우선, 이후 `CNU` 우선, 이후 `AUTO` 묶음의 우선순위 고정

## 라벨 구조

### @GTD
- `@GTD/Action`
- `@GTD/Waiting`
- `@GTD/Reference`
- `@GTD/Read`

### @CNU
- `@CNU/학생`
- `@CNU/뉴스알림`

### @CTX
- `@CTX/Travel`
- `@CTX/Finance`

### @AUTO
- `@AUTO/Newsletter`
- `@AUTO/Receipt`
- `@AUTO/Notification`
- `@AUTO/Social`
- `@AUTO/Promo`

### @SYS
- `@SYS/Security`

## 라벨/필터 상위 정책
- 총 라벨 수 상한: 15
- 라벨 규칙: 새 라벨 추가 시 기존 라벨 1개 정리
- 라벨은 사람이 직접 판단할 여지를 유지하는 최소 단위로 구성
- 상태 라벨(`@GTD/*`)은 자동 분류의 최종 결과가 아니라 수동 운영 상태 라벨로만 사용

## 우선순위 체인
1. `@SYS/Security` (보안)
2. `@CNU/학생`
3. `@CNU/뉴스알림`
4. `@AUTO/Receipt`
5. `@CTX/Travel`
6. `@AUTO/Social`
7. `@AUTO/Promo`
8. `@AUTO/Newsletter`
9. `@AUTO/Notification`

## 수동 프로세스(핵심)
- 인박스 진입 후 `@GTD/Action/Waiting/Reference/Read` 중 1개만 선택
- 사람 응답 필요/답변 대기/보존/읽기 종료를 분리

## 운영 가드
- 보안 메일 누락 제로를 최우선으로 감시
- 라벨 상한 초과 방지
- 주간 리뷰에서 `@AUTO/Notification`, `@AUTO/Newsletter`, `@AUTO/Promo` 질적 점검
