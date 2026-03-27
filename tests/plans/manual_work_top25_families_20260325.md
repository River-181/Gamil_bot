# manual/work top 25 remaining thread families 2026-03-25

## purpose
- 남은 `manual/work residual`와 `self-thread`를 thread-family 단위로 압축한다.
- 이 목록은 **새 auto-safe sender rule 후보가 아니라**, 반대로 **auto-safe가 아닌 가족**을 고정하는 용도다.

## rule
- 아래 25개 가족은 전부 `not auto-safe = YES`다.
- 이유:
  - sender만으로 안전하게 분류되지 않는다.
  - thread 목적, 상대방, subject 문맥이 필요하다.
  - 일부는 self-thread, 일부는 프로젝트/계약/행정/환급/면담/과제 회신이 섞인다.

## top 25 remaining manual/work thread families
| # | family | example sender / subject | not auto-safe |
|---|---|---|---|
| 1 | project / contract / hackathon | `djglocal25@naver.com` / `Re: [2026 장인학교 해커톤] 망상궤도 팀, 비교견적 및 계약 문의` | YES |
| 2 | project / contract / hackathon | `outlook_7a89390ca06e025e@outlook.com` / `오프라인 미팅` | YES |
| 3 | project / contract / hackathon | `aa01053208720@gmail.com` / `오사카 여행계획` | YES |
| 4 | refund / admin follow-up | `doogie233@naver.com` / `Re: [환급신청] ... 수수료 환급 신청` | YES |
| 5 | refund / admin follow-up | `hoam518@gmail.com` / `Re: 데이터 활용과 문제해결 수강생 김주용` | YES |
| 6 | direct mentor / paper / submission | `minjugim655@gmail.com` / `R&D 프로젝트 멘토링_결과보고서 제출` | YES |
| 7 | direct mentor / paper / submission | `euclidsoft.edu@gmail.com` / `R&D 프로젝트 멘토링_지출품의서` | YES |
| 8 | direct university correspondence | `suk.w.han@cnu.ac.kr` / `RE: 노화심리학 수업 자료` | YES |
| 9 | direct university correspondence | `pdkim@cnu.ac.kr` / `논문 목록 PDF` | YES |
| 10 | direct university correspondence | `munhyunsu@cs-cnu.org` / `ChatGPT 대화내용 백업` | YES |
| 11 | personal / reference-only direct mail | `oneulst1@naver.com` / `김주용님 사진 파일 보내드립니다 ^^` | YES |
| 12 | personal / reference-only direct mail | `hihippo@lh.or.kr` / `...` | YES |
| 13 | personal / reference-only direct mail | `olepensen@gmail.com` / `Hello Mr Kim & Mr Kim` | YES |
| 14 | self-thread / self-reference | `chany010713@gmail.com` / `안녕하세요` | YES |
| 15 | self-thread / self-reference | `chany010713@gmail.com` / `삼겹살 600g` | YES |
| 16 | self-thread / self-reference | `chany010713@gmail.com` / `21 학기 기말고사 정리` | YES |
| 17 | self-thread / self-reference | `chany010713@gmail.com` / `실험 전 필독 사항 CAR` | YES |
| 18 | self-thread / self-reference | `chany010713@gmail.com` / `안녕하세요!` | YES |
| 19 | self-thread / self-reference | `chany010713@gmail.com` / `삼겹살` | YES |
| 20 | self-thread / self-reference | `chany010713@gmail.com` / `안녕하세요` thread repeat | YES |
| 21 | self-thread / self-reference | `chany010713@gmail.com` / `각종 메모성 반복 thread` | YES |
| 22 | direct mentor / paper / submission | `yhkwon67@gmail.com` / `장학재단 사회리더16기 권영혁멘토의 면접 설문` | YES |
| 23 | direct mentor / paper / submission | `hoowny@naver.com` / `상속포기각서` | YES |
| 24 | direct mentor / paper / submission | `kang.songyi785@gmail.com` / `안녕하세요!` / `Re: 안녕하세요!` | YES |
| 25 | direct university correspondence | `raros23@o.cnu.ac.kr` / `인지심리학 연습문제 번역본` | YES |

## operational note
- 위 25개는 `sender-only` 자동화 후보가 아니다.
- thread-level triage에서만 `@GTD/Action`, `@GTD/Waiting`, `@GTD/Reference`, `@GTD/Read`를 결정한다.
- self-thread는 기본 `@GTD/Reference`, 예외만 `Action/Waiting`.

## next step
- 이 25개를 실제 apply 후보로 보려면 thread 대표 메시지 기준으로만 다시 확인한다.
- 그 전까지는 새 sender rule을 추가하지 않는다.
