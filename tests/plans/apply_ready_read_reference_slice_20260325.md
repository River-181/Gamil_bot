# apply ready read/reference slice 2026-03-25

## scope
- `Read-first 5 + Reference-first 10`만 묶은 최소 apply-ready note.
- 새 `@AUTO/*` sender rule 추가 없음.
- thread-level GTD decision만 기록한다.

## bulk-safe 15-item slice

### Read-first `5`
| family / sender | recommended GTD state | reason |
| --- | --- | --- |
| `ScienceDaily` | `@GTD/Read` | newsletter / digest / article content |
| `Glasp` | `@GTD/Read` | content / update digest |
| `Freedom` | `@GTD/Read` | low-risk informational content |
| `Linking Your Thinking` | `@GTD/Read` | recurring informational content |
| pure newsletter / digest family | `@GTD/Read` | 읽고 종료 가능한 콘텐츠성 메일 |

### Reference-first `10`
| family / sender | recommended GTD state | reason |
| --- | --- | --- |
| `Notion` | `@GTD/Reference` | service / collaboration / record keeping |
| `GitHub` | `@GTD/Reference` | platform / notification / record keeping |
| `OpenAI` | `@GTD/Reference` | product update / service notice |
| `n8n` | `@GTD/Reference` | platform / system update |
| `Figma` | `@GTD/Reference` | collaboration / platform notice |
| `Stripe` | `@GTD/Reference` | receipt / statement / billing record |
| `Trip.com` | `@GTD/Reference` | booking / travel record |
| `KB Card` | `@GTD/Reference` | receipt / statement / finance record |
| `AliExpress` | `@GTD/Reference` | shipping / order / fulfillment record |
| `Daiso` | `@GTD/Reference` | commerce / service notice |

## decision rule
- sender-family와 subject-theme를 먼저 묶는다.
- 읽고 끝나면 `@GTD/Read`.
- 보존 가치가 더 크면 `@GTD/Reference`.
- 실행 필요성이 보이면 `@GTD/Action` 또는 `@GTD/Waiting`으로 보류한다.

## exclusions
- `manual/work residual`
- `self-thread / self-reference`
- login / verification / password reset
- 직접 계약 / 제출 / 행정 회신
- 새 sender rule 추가

## next step
1. 이 15개는 thread-level confirmation 후 bulk apply 후보로 유지한다.
2. `Security-first`는 별도 lane에서 확인한다.
3. `manual/work`와 `self-thread`는 bulk apply 대상에서 제외한다.
