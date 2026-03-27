# steady state ops transition 2026-03-24

## objective
- 대량 backlog triage 단계에서 steady-state 운영 단계로 전환한다.

## transition reason
- 새 `1000`을 여러 번 생성했지만 실제 고유 잔여는
  - `849`
  - `506`
  - `342`
로 줄었다.
- 이는 backlog가 실제로 고갈 단계에 들어갔다는 뜻이다.
- 현재 live residual은 `201`이다.
- `Security` / `Read` / `Reference` / `Manual-Work` lane snapshot은 3650d 창 기준 `0`건이라 coverage refresh가 필요하다.

## operating mode change
### before
- large backlog discovery
- repeated `100 x 5` and `200 x 5`
- new sender family exploration

### after
- lane-based steady state
- final residual coverage refresh
- new inbound / residual only
- apply-ready 압축 중심

## steady-state lanes
### security-first
- login
- verification
- password reset
- account alert
- action:
  - 먼저 `@SYS/Security`
  - 확인 후 `Read` 또는 `Reference`

### read-first
- newsletter
- content digest
- low-value informational content
- action:
  - 기본 `@GTD/Read`

### reference-first
- service notices
- receipts / statements
- travel / shipping / booking
- platform updates
- action:
  - 기본 `@GTD/Reference`

### manual/work
- direct reply
- academic / admin live thread
- project / contract / submission
- action:
  - `@GTD/Action`
  - `@GTD/Waiting`
  - `@GTD/Reference`

## daily workflow
1. 신규 `has:nouserlabels`만 뽑는다.
2. sender-family / subject-theme 기준으로 4개 lane에 배치한다.
3. `Security` 먼저 확인한다.
4. `Read/Reference` bulk 압축한다.
5. live thread만 `Action/Waiting`으로 남긴다.

## stop doing
- 무분별한 새 auto rule 추가
- message 단위 triage
- self-thread를 개별 메일로 계속 세는 방식

## success condition
- 신규 유입은 small queue로 충분히 소화된다.
- 잔여 long-tail은 lane 구조 안에서 설명 가능하다.
- `1000` 단위 대량 탐색 없이도 운영이 유지된다.
