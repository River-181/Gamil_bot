# thread manual triage ops v1

## 목적
- `manual-review` 대상 메일을 `message`가 아니라 `thread` 단위로 처리한다.
- 같은 thread의 반복 메시지는 중복 분류하지 않고, 하나의 `GTD` 상태만 유지한다.

## 기본 원칙
- `1 thread = 1 GTD state`
- 반복 회신, 전달, 답장, 자동 알림이 섞여도 최종 상태는 하나만 둔다.
- 상태 부여는 최신 메시지 1개만 보지 말고 thread 전체 의도를 본다.
- thread 내 중복 메시지는 `label`이 아니라 `history note`로만 기록한다.

## 상태 우선순위
1. `@GTD/Action`
- 바로 처리해야 하는 요청
- 계약, 견적, 제출, 신청, 일정 조율, 즉시 답장 필요

2. `@GTD/Waiting`
- 상대 답변 대기
- 회신 스레드가 계속 진행 중이고 아직 종료되지 않음

3. `@GTD/Reference`
- 파일 전달, 증빙, 기록 보존
- 나중에 검색만 하면 되는 메일

4. `@GTD/Read`
- 읽고 종료 가능
- 보존은 필요하지만 후속 행동은 없음

## thread dedupe rule
- 같은 `threadId`의 메시지가 여러 개면 가장 먼저 다음 순서로 정리한다.
1. thread의 목적을 한 줄로 적는다.
2. 가장 강한 상태를 하나만 고른다.
3. 나머지 메시지는 중복으로 본다.
- 중복 메시지 처리 예:
  - 같은 답장 스레드 5건은 `Waiting` 1개로 묶는다.
  - 같은 파일 전달 스레드 3건은 `Reference` 1개로 묶는다.
  - 같은 요청 스레드가 아직 미완료면 `Action`이 우선한다.
  - 같은 self thread가 반복되면 `Reference` 1개로 묶는다.

## self-thread special case
- sender가 사용자 본인이고 subject도 반복되면 thread 하나로 본다.
- 기본 상태는 `@GTD/Reference`
- 예:
  - `chany010713@gmail.com`
  - subject: `안녕하세요`
- 추가 예:
  - `chany010713@gmail.com`
  - subject: `삼겹살 600g`
- 이 경우 message 수가 많아도 triage 1건으로 계산한다.

## 상태 선택 규칙
- `Action` 우선 조건
  - 아직 답해야 함
  - 제출/신청/계약/견적/미팅 조율이 남아 있음
- `Waiting` 우선 조건
  - 내가 이미 보냈고 상대 회신을 기다림
  - thread가 진행 중이라 종료하면 안 됨
- `Reference` 우선 조건
  - 문서, 증빙, 파일, 안내문, 백업 목적
- `Read` 우선 조건
  - 내용 확인만 필요하고 후속 행동이 없음

## 수동 triage 작업 방식
1. thread 대표 메시지 1개를 고른다.
2. subject와 sender를 보고 상태를 고른다.
3. 같은 thread의 나머지 메시지는 중복으로 표시한다.
4. 상태가 바뀌면 thread 전체 상태를 갱신한다.

## 예시
- `djglocal25@naver.com`
  - `Re: [2026 장인학교 해커톤] 망상궤도 팀, 비교견적 및 계약 문의`
  - `Action`
- `doogie233@naver.com`
  - `Re: [환급신청]충남대 데이터베이스 수업 SQLD 자격증 수수료 환급 신청`
  - `Waiting`
- `oneulst1@naver.com`
  - `김주용님 사진 파일 보내드립니다 ^^`
  - `Reference`
- `kang.songyi785@gmail.com`
  - `안녕하세요!`
  - `Read`

## 운영 금지
- 같은 thread에 `Action`과 `Waiting`을 동시에 남기지 않는다.
- 같은 sender라고 해서 무조건 같은 상태로 묶지 않는다.
- auto-label 규칙으로 thread manual triage를 대체하지 않는다.

## batch 연동
- `manual_review_batch_50_20260324.json` 같은 배치는 thread triage의 입력이다.
- 배치별 추천안은 `message` 기준이 아니라 `thread state` 기준으로 최종 정리한다.

## 완료 기준
- thread별 상태가 1개로 정리된다.
- 중복 메시지는 더 이상 별도 라벨링 대상이 아니다.
- `Action / Waiting / Reference / Read`의 기준이 흔들리지 않는다.
