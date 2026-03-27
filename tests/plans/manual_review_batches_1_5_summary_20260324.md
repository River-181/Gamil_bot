# manual review batches 1-5 summary 2026-03-24

## 목적
- `manual_review_batch_50_20260324.json`의 batch 1-5를 묶어 핵심 패턴과 GTD 분류 기준을 한 번에 정리한다.
- Step A(`4015 -> 3515`) 진행에 필요한 수동 triage 기준을 고정한다.

## 전체 패턴
- 자동 분류가 남기는 잔여는 더 이상 bulk/newsletter 중심이 아니다.
- 대부분이 `direct reply`, `project/admin`, `personal thread`, `self thread`다.
- thread 단위로 묶지 않으면 message 중복이 많아져 처리 효율이 떨어진다.
- `promo/newsletter` 자동화는 거의 소진됐고, 수동 triage가 본선이다.

## batch 1 요약
- 대표 sender:
  - `djglocal25@naver.com`
  - `doogie233@naver.com`
  - `outlook_7a89390ca06e025e@outlook.com`
  - `oneulst1@naver.com`
  - `chany010713@gmail.com`
- 대표 주제:
  - 계약/견적 문의
  - 오프라인 미팅
  - 환급 신청 회신
  - 사진 파일 전달
  - 템플릿성 self 메일
- 권장 GTD:
  - `@GTD/Action`
  - `@GTD/Waiting`
  - `@GTD/Reference`

## batch 2 요약
- 대표 sender:
  - `euclidsoft.edu@gmail.com`
  - `minjugim655@gmail.com`
  - `chany010713@gmail.com`
- 대표 주제:
  - R&D 프로젝트 멘토링 제출
  - 지출품의서
  - 행정/증빙성 스레드
  - self/mail-draft
- 권장 GTD:
  - `@GTD/Waiting`
  - `@GTD/Reference`

## batch 3 요약
- 대표 sender:
  - `minjugim655@gmail.com`
  - `euclidsoft.edu@gmail.com`
  - `hoam518@gmail.com`
  - `mimo4am@gmail.com`
  - `yhkwon67@gmail.com`
  - `hoowny@naver.com`
- 대표 주제:
  - 프로젝트 품의서
  - 수강생/행정 회신
  - ChatGPT 대화 백업
  - 면접 설문
  - 상속포기각서
  - 평가 점수 발표
- 권장 GTD:
  - `@GTD/Action`
  - `@GTD/Waiting`
  - `@GTD/Reference`
  - `@GTD/Read`

## batch 4 요약
- 대표 sender:
  - `aa01053208720@gmail.com`
  - `kang.songyi785@gmail.com`
  - `chany010713@gmail.com`
- 대표 주제:
  - 오사카 여행계획
  - 안녕하세요
  - self thread 반복
- 권장 GTD:
  - `@GTD/Action`
  - `@GTD/Read`
  - `@GTD/Reference`

## batch 5 요약
- 대표 sender:
  - `chany010713@gmail.com`
- 대표 주제:
  - `안녕하세요`
- 권장 GTD:
  - `@GTD/Reference`
- 해석:
  - self thread 반복이라 message 단위보다 thread 단위로 묶는 것이 맞다.

## 대표 sender별 운영 해석
- `djglocal25@naver.com`
  - 계약/견적/대체과제/행정 회신
  - `Action` 또는 `Waiting`
- `doogie233@naver.com`
  - 환급 신청 회신
  - `Waiting`
- `euclidsoft.edu@gmail.com`
  - 멘토링 제출/증빙/회신 혼합
  - `Waiting` + `Reference`
- `hoam518@gmail.com`
  - 수강/백업/안내 회신
  - `Waiting` + `Reference`
- `chany010713@gmail.com`
  - self thread, 템플릿, 반복 인사
  - `Reference`

## Step A implications
- Step A는 더 이상 bulk sender 소거만으로 달성되지 않는다.
- `50건 x 10 batch`의 manual triage가 핵심 레버다.
- 자동화 가능한 safe sender는 opportunistic하게만 줄인다.
- thread 기준 중복 정리가 필수다.
- `Action/Waiting/Reference/Read` 규칙을 batch 단위로 일관되게 적용해야 `4015 -> 3515`가 현실적이다.

## 권장 운영 순서
1. batch 1-5를 thread 단위로 triage한다.
2. `euclidsoft.edu@gmail.com`와 같은 혼합 sender는 `Waiting/Reference`로 분리한다.
3. `chany010713@gmail.com` 반복 self thread는 `Reference` 우선으로 정리한다.
4. 이후 batch 6-10을 동일 규칙으로 처리한다.
