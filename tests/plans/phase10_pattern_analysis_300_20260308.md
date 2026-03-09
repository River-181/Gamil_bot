# Phase 10 패턴 분석 보고서 (300건 샘플)

## 기준
- 샘플 쿼리: `in:all`
- 샘플 수: `300`
- 목적: 현재 v3 14라벨 체계가 최근 메일 패턴을 충분히 수용하는지 검토하고, 라벨 추가 여부보다 우선적으로 필터 보강 포인트를 확정한다.

## 요약 결과
- 현재 필터 포착 건수: `90`
- 현재 필터 미포착 건수: `210`
- 현재 포착률: `30%`
- 결론:
  - 라벨 체계 자체는 유지 가능하다.
  - 문제는 라벨 수 부족이 아니라 `from_patterns`/`subject_patterns` 커버리지 부족이다.
  - 따라서 이번 단계에서는 라벨을 늘리지 않고, 기존 14개 체계를 유지한 채 필터 패턴을 확장한다.

## 1차 보강 후 재측정
- 샘플 수: `300`
- 포착 건수: `179`
- 미포착 건수: `121`
- 포착률: `59.67%`
- 변화:
  - `30% -> 59.67%`
  - 단일 패턴 보강만으로도 최근 메일 절반 이상이 기존 14개 체계에 자연스럽게 편입됨을 확인

## 1차 보강 후 남은 미포착 상위
- `email.apple.com`: 10
- `gmail.com`: 8
- `github.com`: 7
- `tm1.openai.com`: 6
- `oracleapex.com`: 5
- `email.claude.com`: 5

## 남은 미포착 해석
- `gmail.com`
  - 자기 자신이 보낸 메일과 수동 커뮤니케이션 비중이 높다.
  - 이는 자동 라벨보다 `@GTD/*` 수동 상태 라벨 또는 향후 `Project` 맥락 검토 대상이다.
- `github.com`
  - 보안 알림(`two-factor`, `passkey`)과 일반 개발 알림이 섞여 있다.
  - 2차 보강 시 `@SYS/Security`와 개발 알림 처리 기준을 분리할 가치가 있다.
- `tm1.openai.com`, `email.claude.com`
  - 데이터 내보내기/제품 알림/워크스페이스 알림 성격이다.
  - 새 라벨보다는 `@AUTO/Notification` 패턴 세분화가 우선이다.
- `email.apple.com`
  - 보안/계정/서비스 알림이 섞여 있다.
  - 2차 샘플에서 제목 패턴을 더 수집한 뒤 `@SYS/Security` 또는 `@AUTO/Notification`으로 분기하는 것이 안전하다.

## 최근 300건 상위 도메인
- `linkedin.com`: 39
- `nytimes.com`: 23
- `google.com`: 17
- `mail.notion.so`: 15
- `ted.com`: 13
- `linkingyourthinking.com`: 11
- `email.apple.com`: 10
- `accounts.google.com`: 9
- `gmail.com`: 8
- `github.com`: 7

## 미포착 상위 도메인
- `linkedin.com`: 27
- `ted.com`: 13
- `mail.notion.so`: 13
- `linkingyourthinking.com`: 11
- `email.apple.com`: 10
- `accounts.google.com`: 9
- `gmail.com`: 8
- `github.com`: 7
- `navercorp.com`: 7
- `daiso.co.kr`: 6

## 해석
- `linkedin.com`
  - 기존 `rule_social_from`이 `notifications-noreply@linkedin.com`만 포착하고 있었다.
  - 실제 최근 메일은 `messages-noreply@linkedin.com`, `updates-noreply@linkedin.com` 비중이 높다.
  - 이는 새 라벨이 아니라 `@AUTO/Social` 패턴 보강 문제다.
- `ted.com`, `linkingyourthinking.com`, `medium.com`
  - 반복적인 콘텐츠/큐레이션형 메일이다.
  - 새 라벨 없이 `@AUTO/Newsletter`로 흡수 가능하다.
- `accounts.google.com`, `email.apple.com`, `verify@x.com`
  - 보안/인증 성격이 강하다.
  - `@SYS/Security` 보강이 맞다.
- `mail.notion.so`, `tm.openai.com`, `tm1.openai.com`, `email.claude.com`
  - 제품/워크스페이스/내보내기/정책 변경성 알림이 많다.
  - 신규 라벨 없이 `@AUTO/Notification`으로 수용 가능하다.
- `navercorp.com`
  - `네이버페이`는 금융/영수증 계열이므로 `@AUTO/Receipt` + `@CTX/Finance`가 맞다.
- `daiso.co.kr`, `perplexity.ai`, `akool2025.com`
  - 프로모션 성격이 강해 `@AUTO/Promo`로 수용 가능하다.

## 라벨 결정
- 유지:
  - `@GTD/*` 4개
  - `@CNU/*` 2개
  - `@CTX/*` 2개
  - `@AUTO/*` 5개
  - `@SYS/Security` 1개
- 이번 샘플 기준 추가 보류:
  - `@CTX/Project`
  - `@AUTO/Survey`
  - `@AUTO/Shopping`
- 판단 이유:
  - 위 분기들은 별도 라벨로 쪼갤 수는 있으나, 최근 300건 기준으로는 기존 `CTX/AUTO` 범주로 충분히 수용 가능하다.
  - 먼저 필터 적중률을 올린 뒤, 2차 샘플(추가 300건)에서 반복적으로 넘치는 범주가 확인되면 그때 라벨 확장을 검토한다.

## 이번 단계 필터 보강 결정
- `rule_sys_security`
  - `no-reply@accounts.google.com`
  - `verify@x.com`
  - `authentication`, `verification`, `new login`
- `rule_receipt`
  - `naverpayadmin_noreply@navercorp.com`
- `rule_social_from`
  - `messages-noreply@linkedin.com`
  - `updates-noreply@linkedin.com`
- `rule_social_subject_guard`
  - `멘션`, `게시물`, `게시함`, `다음 단계를 확인`
- `rule_promo`
  - `daisomall_official@daiso.co.kr`
  - `team@mail.perplexity.ai`
  - `admin@akool2025.com`
  - `unlock`, `offer`
- `rule_newsletter_from`
  - `recommends@ted.com`
  - `hello@linkingyourthinking.com`
  - `hello@medium.com`
  - `subscriptions@medium.com`
  - `info@admin.manus.im`
- `rule_notification`
  - `notify@mail.notion.so`
  - `noreply@email.openai.com`
  - `noreply@tm.openai.com`
  - `noreply@tm1.openai.com`
  - `no-reply@email.claude.com`
  - `update`, `product update`, `privacy`, `introducing`, `export`, `ready`, `notification`, `mention`, `comment`, `준비를 마쳤습니다`

## 2차 보강(상위 미포착 50건 기반)
- `GitHub` 보안 vs 일반 알림 분리
  - `rule_sys_security`
    - sender 추가: `noreply@github.com`
    - subject 추가: `two-factor`, `passkey`, `recovery code`, `personal access token`
  - `rule_notification`
    - sender 추가: `noreply@github.com`, `dbtools-apexext-noreply@oracleapex.com`
    - subject 추가: `updated permissions`, `permissions`, `workspace`, `purged`
- `OpenAI` / `Claude` 제품 알림 보강
  - `rule_notification`
    - sender 유지/보강: `noreply@email.openai.com`, `noreply@tm.openai.com`, `noreply@tm1.openai.com`, `no-reply@email.claude.com`
    - subject 추가: `데이터 내보내기`, `준비를 마쳤습니다`
- 기타 반복 발신자 보강
  - `rule_promo`
    - `tour@nol-universe.com`, `mail@ifttt.com`, `chelsea.c@ifttt.com`, `hello@freedom.to`, `marriottbonvoy@email-marriott.com`
  - `rule_newsletter_from`
    - `developer@insideapple.apple.com`, `githubeducation@github.com`, `platon@jigwan.org`, `datalabnews@knto.or.kr`, `kird@kird.re.kr`, `no-reply@goodwillstore.org`
  - `rule_notification`
    - `team@mail.notion.so`, `no-reply@gov.kr`, `no.reply@mail.tossbank.com`, `doumi@hi.co.kr`

## 500건 dry-run 검증
- 샘플 쿼리: `in:all`
- 샘플 수: `500`
- 포착 건수: `334`
- 미포착 건수: `166`
- 포착률: `66.8%`

### 500건 기준 상위 규칙
- `rule_newsletter_from`: 110
- `rule_social_from`: 57
- `rule_social_subject_guard`: 32
- `rule_notification`: 28
- `rule_google_notification`: 26
- `rule_sys_security`: 25
- `rule_promo`: 23
- `rule_newsletter_subject_guard`: 19
- `rule_receipt`: 11
- `rule_travel`: 11

### 500건 기준 상위 적용 라벨
- `@AUTO/Newsletter`: 129
- `@AUTO/Social`: 89
- `@AUTO/Notification`: 54
- `@SYS/Security`: 29
- `@AUTO/Promo`: 23
- `@AUTO/Receipt`: 11
- `@CTX/Finance`: 11
- `@CTX/Travel`: 11

### 500건 기준 남은 미포착 상위
- `email.apple.com`: 13
- `gmail.com`: 12
- `naver.com`: 8
- `tm1.openai.com`: 7
- `github.com`: 6
- `email.claude.com`: 6
- `megazone.com`: 6
- `mail.notion.so`: 4
- `creators.gumroad.com`: 4
- `raindrop.io`: 4

## 해석 업데이트
- 현재 14개 라벨 체계는 유지 가능하다.
- 500건 기준으로 `66.8%` 자동 포착이면 전수 적용 전 검증 단계로는 충분히 의미 있는 수준이다.
- 다만 남은 미포착은 다음 세 축으로 남아 있다.
  - 자기 자신/직접 소통 메일 (`gmail.com`)
  - 제품/커뮤니티 알림의 경계 사례 (`OpenAI`, `Claude`, `Notion`, `GitHub`)
  - 쇼핑/프로모션/커뮤니티성 발신자 롱테일

## 현재 결론
- 라벨 추가는 보류한다.
- 다음 우선순위는 새 라벨 설계가 아니라 `미포착 롱테일 sender registry`를 운영하는 것이다.
- 전수 적용 전에 추가로 필요한 것은:
  - 미포착 166건 중 반복 도메인만 다시 묶어 3차 sender 추가
  - 자기 자신이 보낸 메일에 대한 운영 규칙 결정
  - 실제 apply 전 `500 -> 1000 -> 전체` 배치 게이트 유지

## 3차 sender 보강
- `rule_sys_security`
  - `noreply@tm1.openai.com`
  - `pops@megazone.com`
  - `sa.noreply@samsung-mail.com`
  - `authentication code`, `비밀번호가 변경`, `비밀번호 재설정`, `휴면 해제`
- `rule_receipt`
  - `cyberman@bill.kbcard.com`
  - `invoice+statements@mail.anthropic.com`
  - `no_reply@email.apple.com`
  - `billing_info@kepco.co.kr`
  - `청구서`, `invoice`, `환불 요청 접수 확인`
- `rule_promo`
  - `support@gpters.org`
  - `trip.com@newsletter.trip.com`
  - `letter@panelpower.net`
  - `noreply@kyobobook.com`
  - `웨비나`, `소비자 조사에 참여`, `무료 AI 웨비나`
- `rule_newsletter_from`
  - `hello@tavus.io`
  - `no-reply@m.mail.coursera.org`
  - `emails@britishmuseum.org`
  - `newsletters-noreply@linkedin.com`
- `rule_notification`
  - `notifications@github.com`
  - `info@raindrop.io`
  - `windowsinsiderprogram@e-mails.microsoft.com`
  - `no-reply@nol-universe.com`
  - `memories@facebookmail.com`
  - `export file created`, `bookmarks imported successfully`, `과거의 오늘`, `run failed`, `run cancelled`, `체험판`

## 1000건 dry-run 검증
- 샘플 쿼리: `in:all`
- 샘플 수: `1000`
- 포착 건수: `692`
- 미포착 건수: `308`
- 포착률: `69.2%`

### 1000건 기준 상위 규칙
- `rule_newsletter_from`: 253
- `rule_social_from`: 100
- `rule_promo`: 63
- `rule_sys_security`: 53
- `rule_social_subject_guard`: 51
- `rule_notification`: 49
- `rule_receipt`: 45
- `rule_newsletter_subject_guard`: 40
- `rule_google_notification`: 34

### 1000건 기준 상위 적용 라벨
- `@AUTO/Newsletter`: 293
- `@AUTO/Social`: 151
- `@AUTO/Notification`: 83
- `@AUTO/Promo`: 63
- `@SYS/Security`: 63
- `@AUTO/Receipt`: 45
- `@CTX/Finance`: 45
- `@CTX/Travel`: 17

### 1000건 기준 남은 미포착 상위
- `gmail.com`: 38
- `cnu.ac.kr`: 16
- `email.apple.com`: 14
- `naver.com`: 13
- `makenotion.com`: 12
- `mail.perplexity.ai`: 12
- `mymind.com`: 11
- `creators.gumroad.com`: 6
- `mail.notion.so`: 6
- `email.claude.com`: 6

## 최종 해석
- 현재 상태로도 전수 분류 전 검증 기준은 통과 가능한 수준이다.
- 남은 미포착은 이제 큰 범주 미설계 문제가 아니라, `개별 서비스 롱테일`과 `자기 자신이 보낸 메일`, `수동 검토가 필요한 업무 메일` 문제다.
- 즉 다음 단계의 핵심은 라벨 구조 재설계가 아니라:
  - `self-sent` 처리 정책 확정
  - `CNU 직접 소통`과 일반 공지의 추가 분리
  - 롱테일 sender를 운영 중 계속 누적 등록하는 방식

## 다음 기준
- 2차 샘플 300건에서 포착률이 유의미하게 올라가는지 확인
- 여전히 `Project`, `Survey`, `Shopping` 계열이 반복적으로 기존 라벨 범주를 넘친다면 그때 라벨 추가 검토
- 지정되지 않은 발신자는 지금처럼 패턴 분석 후 순차 추가
