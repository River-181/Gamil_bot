# manual review queue baseline 2026-03-24

## 목적
- `has:nouserlabels` 잔여 중 자동 분류가 위험한 메일을 `manual-review queue`로 분리한다.
- 이 문서는 자동 `promo/newsletter` 금지 sender와 우선 검토 주제를 고정한다.

## 자동 분류 금지 sender
- `djglocal25@naver.com`
- `oneulst1@naver.com`
- `doogie233@naver.com`
- `outlook_7a89390ca06e025e@outlook.com`
- `chany010713@gmail.com`

## 샘플 근거
- `djglocal25@naver.com`
  - `Re: [2026 장인학교 해커톤] 망상궤도 팀, 비교견적 및 계약 문의`
  - `Re: 장인학교 해커톤 대체과제 안내`
- `oneulst1@naver.com`
  - `김주용님 사진 파일 보내드립니다 ^^`
- `outlook_7a89390ca06e025e@outlook.com`
  - `오프라인 미팅`
- `doogie233@naver.com`
  - `Re: [환급신청]충남대 데이터베이스 수업 SQLD 자격증 수수료 환급 신청`

## 수동 triage 분류 기준
### `@GTD/Action`
- 바로 답장 또는 처리 필요
- 계약/견적/신청/제출/수정 요청

### `@GTD/Waiting`
- 상대 답변 대기
- 회신 스레드가 진행 중이고 즉시 종료할 수 없는 메일

### `@GTD/Reference`
- 기록 보존만 필요
- 증빙/전달 자료/행정 기록

### `@GTD/Read`
- 읽고 종료 가능
- 공지성에 가깝지만 자동 분류하기엔 발신자 맥락이 애매한 메일

## 운영 원칙
- 위 sender는 새 자동 rule 추가 금지
- 위 sender는 `@AUTO/*`로 보내지 않음
- 필요 시 subject 패턴이 반복되는 스레드만 별도 검토 후 수동 상태 라벨 부여

## 다음 작업
1. 위 sender들의 최근 20건 subject를 추가 수집
2. `Action/Waiting/Reference/Read`로 수동 분류 템플릿 작성
3. 필요하면 `manual-review snapshot` 산출물 생성

## first batch
- batch artifact:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch_50_20260324.json`
- source:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_pool_400_20260324.json`
- selection rule:
  - `manual_like_primary` pool의 앞 50개
- intended use:
  - 수동 triage 파일럿
  - `@GTD/Action|Waiting|Reference|Read` 기준 실험

## first 10 sample
- `oneulst1@naver.com`
  - `김주용님 사진 파일 보내드립니다 ^^`
  - suggested state: `@GTD/Reference`
- `djglocal25@naver.com`
  - `Re: [2026 장인학교 해커톤] 망상궤도 팀, 비교견적 및 계약 문의`
  - `RE: [2026 장인학교 해커톤] 망상궤도 팀, 비교견적 및 계약 문의`
  - `Re: 장인학교 해커톤 대체과제 안내`
  - suggested state: `@GTD/Action` 또는 `@GTD/Waiting`
- `outlook_7a89390ca06e025e@outlook.com`
  - `오프라인 미팅`
  - suggested state: `@GTD/Action`
- `chany010713@gmail.com`
  - `[말머리] 핵심용건 (30자 내외, 소속/날짜/프로젝트 포함) (현재 날짜)`
  - suggested state: `@GTD/Reference`
- `doogie233@naver.com`
  - `Re: [환급신청]충남대 데이터베이스 수업 SQLD 자격증 수수료 환급 신청`
  - suggested state: `@GTD/Waiting` 또는 `@GTD/Reference`

## triage template
- `@GTD/Action`
  - 계약/견적/대면 일정/즉시 답장 필요
- `@GTD/Waiting`
  - 신청/회신 스레드로, 상대방 반응 대기 성격
- `@GTD/Reference`
  - 파일 전달/기록 보존/나중 검색용
- `@GTD/Read`
  - 읽고 종료 가능하지만 자동 분류하기엔 애매한 직접 메일
