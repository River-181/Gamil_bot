# apply ready security-first 5 slice 2026-03-25

## scope
- `security-first` lane에서 thread-level로 바로 적용 가능한 최소 5개 슬라이스.
- 새 `@AUTO/*` sender rule 추가 없음.
- thread 단위로만 판단한다.

## thread-level security slice

| thread / sender family | recommended GTD state | reason |
| --- | --- | --- |
| `account_noreply@navercorp.com` | `@SYS/Security` | account notice / login confirmation |
| `help@help.naver.com` | `@SYS/Security` | login alert / verification |
| `no-reply@everytime.kr` | `@SYS/Security` | login / password reset family |
| `no-reply@dropbox.com` | `@SYS/Security` | account notice / security confirmation |
| `workspace-noreply@google.com` | `@SYS/Security` | workspace access / account notice |

## demotion rule
- 이미 확인된 오래된 notice만 `@GTD/Read` 또는 `@GTD/Reference`로 내린다.
- 위 5개는 현재 기준에서 우선 `@SYS/Security`로 둔다.

## decision rule
- login alert, verification, password reset, account recovery, suspicious access는 모두 security-first다.
- product update, receipt, booking, newsletter는 이 slice에서 제외한다.
- sender-only 자동화는 더 추가하지 않는다.

## next step
1. 위 5개만 thread-level confirmation 후 적용 후보로 본다.
2. 오래된 acknowledged notice는 별도 demotion 검토를 한다.
3. 나머지는 manual triage 또는 다른 lane으로 유지한다.
