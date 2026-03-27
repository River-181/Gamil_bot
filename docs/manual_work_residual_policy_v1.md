# manual/work residual policy v1

## 목적
- 남은 `has:nouserlabels` 메일 중 자동 분류가 위험한 `manual/work residual`을 별도로 다룬다.
- `sender-only` 자동화는 계속 쓰되, 개인/업무 회신성 메일은 보수적으로 분리한다.

## 현재 판단
- `@AUTO/*`, `@CTX/*`, `@SYS/*`로 안전하게 들어갈 반복 sender 군집은 상당수 소진됐다.
- 남은 잔여는 아래 비중이 높다.
  - 개인 회신
  - 업무성 메일
  - 학교 직접 소통
  - 신규 long-tail sender

## 자동화 허용 범위
- 아래는 `sender-only` 또는 명확한 제목 패턴으로 자동화 허용
  - 반복 결제/영수증 발신자
  - 반복 서비스 notification 발신자
  - 반복 newsletter 발신자
  - `@cnu.ac.kr` 중 공지성/도서관/행정성 발신자
  - 이미 수동 검토로 직접 소통이 확인된 `@cnu.ac.kr` 발신자

## 자동화 금지 범위
- 아래는 새 규칙 추가 전 반드시 샘플 검토
  - 개인 Gmail/Naver/Daum 발신자
  - 회사/프로젝트 직접 회신으로 보이는 발신자
  - 과제/피드백/지원/미팅/협업 문맥이 섞인 발신자
  - 동일 sender라도 subject가 공지와 회신을 혼합하는 경우

## manual/work residual 금지 sender 예시
- 아래 sender는 `promo/newsletter` 자동 분류 금지
  - `djglocal25@naver.com`
  - `oneulst1@naver.com`
  - `doogie233@naver.com`
  - `outlook_7a89390ca06e025e@outlook.com`
  - `chany010713@gmail.com`
- 이유:
  - 실제 회신/미팅/파일 전달/프로젝트 문의 문맥이 섞여 있다.

## 최근 샘플 관측(2026-03-24)
- `oneulst1@naver.com`
  - `김주용님 사진 파일 보내드립니다 ^^`
- `djglocal25@naver.com`
  - `Re: [2026 장인학교 해커톤] 망상궤도 팀, 비교견적 및 계약 문의`
  - `Re: 장인학교 해커톤 대체과제 안내`
- `outlook_7a89390ca06e025e@outlook.com`
  - `오프라인 미팅`
- `doogie233@naver.com`
  - `Re: [환급신청]충남대 데이터베이스 수업 SQLD 자격증 수수료 환급 신청`

## manual-review queue 초안
- 아래 성격은 자동 라벨링 대신 수동 triage
  - 프로젝트 견적/계약
  - 오프라인 미팅
  - 파일 전달
  - 환급/행정 신청 회신
- 기본 처리:
  - 사용자 검토 전까지 자동 `promo/newsletter` 금지
  - 필요 시 수동으로 `@GTD/Action`, `@GTD/Waiting`, `@GTD/Reference` 부여

## 상태 라벨 운영 원칙
- `@GTD/Action`
  - 오늘/이번 주 직접 처리 필요
- `@GTD/Waiting`
  - 답변 대기, 후속 필요
- `@GTD/Reference`
  - 보존용, 검색 참조용
- `@GTD/Read`
  - 읽고 종료 가능

## manual/work residual 분류 규칙 초안
### 1. CNU direct
- 대상:
  - 교수/조교/학생 개인 메일
  - 과제/피드백/상담/면담/행정 문의 회신
- 기본 라벨:
  - `@CNU/학생`
- 상태 라벨:
  - 자동 부여하지 않음
  - 필요 시 수동으로 `@GTD/*` 추가

### 2. project/work direct
- 대상:
  - 외부 협업, 프로젝트 문의, 채용/업무 연락
- 기본 라벨:
  - 자동 부여 보류
- 상태 라벨:
  - 수동 triage 후 `@GTD/Action|Waiting|Reference|Read`

### 3. personal direct
- 대상:
  - 가족/지인/개인 대화
- 기본 라벨:
  - 자동 부여 보류
- 상태 라벨:
  - 수동 triage

## 위험 발신자 관리
- 아래 sender는 현재 규칙 재검토 필요
  - `euclidsoft.edu@gmail.com`
- 이유:
  - 현재 `promo`로 들어가 있을 가능성이 있으나 업무성 발신자일 수 있다.
- 조치:
  - 다음 턴에 실제 subject 샘플 확인 후 `promo` 유지/제거 결정

## 다음 실행 순서
1. `@cnu.ac.kr` 무라벨 20건 샘플 재시도
2. 직접 소통이 확인된 sender만 `rule_cnu_student_sender_only`에 추가
3. `euclidsoft.edu@gmail.com` subject 샘플 확인
4. 업무성으로 확인되면 `promo`에서 제거

## 승인 원칙
- manual/work residual에는 대량 자동 apply를 바로 하지 않는다.
- 새 sender 추가 전 최소 1개 이상 실제 subject 샘플을 확인한다.
