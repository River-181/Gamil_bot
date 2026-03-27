# self-thread bulk reference rule v1

## purpose
- `manual-review`에 남은 self-sent mail을 낮은 비용으로 정리한다.
- 대상은 주로 `chany010713@gmail.com` 발신의 반복 self-thread다.

## target pattern
- sender:
  - `chany010713@gmail.com`
- dominant subject family examples:
  - `안녕하세요`
  - `삼겹살 600g`
  - `삼겹살`
  - `21 학기 기말고사 정리`
  - `실험 전 필독 사항 CAR`

## default state
- 기본 상태:
  - `@GTD/Reference`

## apply conditions
- 아래 조건을 모두 만족하면 bulk `@GTD/Reference` 후보로 본다.
1. self-sent thread다.
2. 회신 상대가 사실상 자기 자신이거나 self archive 성격이다.
3. 반복 제목 또는 메모성 제목이다.
4. 명시적 계약/일정/신청/후속 액션이 없다.

## exclusion conditions
- 아래 중 하나라도 있으면 bulk 처리하지 않는다.
1. 실제 외부인과 주고받는 대화가 섞여 있다.
2. 일정 조율, 제출, 계약, 환급, 행정 요청처럼 살아 있는 action이 있다.
3. thread 내용상 `Waiting` 또는 `Action` 의미가 더 강하다.

## dedupe rule
- 같은 subject family가 다수여도 triage는 thread family 단위로 압축한다.
- `message count`가 아니라 `decision unit`을 기준으로 본다.
- 예:
  - `삼겹살 600g` 99건 -> `Reference` family 1건
  - `안녕하세요` 반복 -> `Reference` family 1건

## execution note
- 이 규칙은 `batch100_08~10`에 우선 적용한다.
- 적용 순서:
1. self-thread 여부 확인
2. exclusion 조건 확인
3. bulk `@GTD/Reference`로 묶음 처리
4. 예외 thread만 별도 `Action/Waiting/Read`로 분리

## risk note
- self-sent라고 해서 모두 `Reference`는 아니다.
- 자기 자신에게 보낸 reminder, 일정, 제출 메모는 `Action`일 수 있다.
- 따라서 subject family와 thread 목적을 함께 봐야 한다.
