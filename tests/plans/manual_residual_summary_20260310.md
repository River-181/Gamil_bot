# Manual Residual Summary 2026-03-10

## 목적
- `has:nouserlabels`에 남아 있지만 기존 rule-family queue에 걸리지 않는 메일 100건을 표본 분석한다.

## 결과 요약
- 표본 크기: `100`
- 원본: `/Users/river/tools/gmail-agent-sys/tests/plans/manual_residual_sample_100_20260310.json`

## 상위 도메인
- `makenotion.com`: `11`
- `email.apple.com`: `10`
- `mail.notion.so`: `5`
- `cnu.ac.kr`: `5`
- `naver.com`: `4`
- `kyobobook.com`: `4`
- `notion.com`: `3`
- `stripe.com`: `3`

## 상위 발신자
- `Apple <noreply@email.apple.com>`: `8`
- `Notion Support <templates-inbox@makenotion.com>`: `8`
- `"교보문고" <noreply@kyobobook.com>`: `3`
- `"기획재정과" <evaluation@cnu.ac.kr>`: `3`
- `"Notion Academy & Certifications" <team@notion.com>`: `3`

## 관찰
- `Notion` 계열이 가장 큰 잔여군이다.
  - `templates-inbox@makenotion.com`
  - `marketplace@mail.notion.so`
  - `notify@mail.notion.so`
  - `team@notion.com`
- `Apple/iCloud` 계열도 반복적으로 남아 있다.
- `CNU` 계열 중 일부는 현재 `subject` 패턴이 약해서 `critical_review` 또는 `CNU notice` 보강 후보로 보인다.
- `교보문고`, `티머니`, `토스증권`, `KB국민은행`, `PayPal`은 `context_ops` 또는 finance rule 보강 후보다.
- `Your authentication code`와 로그인성 Apple 메일이 residual에 남는 것은 `Security` 패턴 보강 우선순위가 높다는 뜻이다.

## 다음 보강 후보
1. `Notion` 알림/템플릿/마켓플레이스 전용 rule 또는 기존 `notification/newsletter` 보강
2. `Apple/iCloud`의 계정/가족공유/로그인 분기 보강
3. `CNU` notice/student 패턴 추가 보강
4. `교보문고`/`티머니`/`토스증권`/`KB국민은행`/`PayPal`의 finance-context 보강

## 보강 후 재스캔
- 재스캔 아티팩트: `/Users/river/tools/gmail-agent-sys/tests/plans/manual_residual_rescan_notion_apple_20260310.json`
- `Notion` sender-family residual: `293`
  - 큰 군집:
    - `notify@mail.notion.so`: `200`
    - `team@mail.notion.so`: `35`
    - `ivan@mail.notion.so`: `33`
  - 해석:
    - 기존 보강만으로는 `Notion`이 아직 backlog의 독립 큐가 될 만큼 크다.
- `Apple/iCloud` sender-family residual: `41`
  - 대부분 가족공유/공유 해제 계열
  - 로그인/인증 계열 subject도 일부 포함
  - 해석:
    - `Apple`은 `security`와 `general notification` 분리 적용이 필요하다.

## 1차 focused apply
- `Notion support/marketplace`
  - snapshot: `/Users/river/tools/gmail-agent-sys/.tokens/phase10_notion_notification_25.json`
  - apply: `10`
  - journal: `/Users/river/tools/gmail-agent-sys/.tokens/phase10_apply_journal_notion_notification_10_20260310.jsonl`
- `Apple family sharing`
  - snapshot: `/Users/river/tools/gmail-agent-sys/.tokens/phase10_apple_notification_25.json`
  - apply: `10`
  - journal: `/Users/river/tools/gmail-agent-sys/.tokens/phase10_apply_journal_apple_notification_10_20260310.jsonl`
- `Notion newsletter`
  - snapshot: `/Users/river/tools/gmail-agent-sys/.tokens/phase10_notion_newsletter_residual_25.json`
  - apply: `13`
  - journal: `/Users/river/tools/gmail-agent-sys/.tokens/phase10_apply_journal_notion_newsletter_13_20260310.jsonl`

## focused apply 후 재스캔
- 재스캔 아티팩트: `/Users/river/tools/gmail-agent-sys/tests/plans/manual_residual_rescan_notion_apple_post_apply_20260310.json`
- `Apple` residual:
  - before: `41`
  - after focused family/apply: `31`
  - after storage apply + rescan: `22`
  - 감소: `19`
- `Notion` residual:
  - 총합은 sender family 확장 재집계로 직접 비교하지 않음
  - 핵심 sender 감소:
    - `team@notion.com`: `3 -> 0`
    - `ivan@mail.notion.so`: `33 -> 23`
    - `templates-inbox@makenotion.com`: `8 -> 1`
    - `marketplace@mail.notion.so`: `10 -> 8`
  - 해석:
    - `Notion`은 여전히 `notify@mail.notion.so`, `team@mail.notion.so`가 큰 잔여군이라 별도 queue로 계속 밀어야 한다.

## Apple 2차 분기 후 상태
- 재스캔 아티팩트: `/Users/river/tools/gmail-agent-sys/tests/plans/manual_residual_rescan_apple_post_storage_20260310.json`
- 남은 `Apple` residual `22`건의 대부분은 아래 성격이다.
  - `Find My` 비활성화
  - `iCloud 로그인`
  - `앱 암호 생성`
- 판단:
  - 이 구간은 더 소거할 대상이 아니라 `@SYS/Security` 보호 구간으로 보는 것이 맞다.
  - 일반 알림으로 남는 `iCloud storage`, `iOS 이용 약관`만 `@AUTO/Notification`으로 수렴시킨다.
