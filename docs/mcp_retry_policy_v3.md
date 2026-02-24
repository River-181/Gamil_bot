# MCP 재시도 및 오류 처리 정책 (v3)

## 1) 처리 규칙
| 상태 | 정책 |
|---|---|
| 401 (Unauthorized) | 토큰 만료/무효로 판단하고 OAuth 갱신 1회 시도 후 재요청. 반복 실패 시 운영자 승인 대기 |
| 403 (Forbidden) | 권한 부족으로 간주. scope/동의 상태 점검 필요 |
| 429 (Too Many Requests) | 지수 백오프 시작(800ms→1.6s→3.2s→6.4s), 최대 5회, jitter ±15% |
| 500/502/503/504 | 지수 백오프 + 최대 5회 재시도, 실패시 dead-letter 기록 |
| 400 (Bad Request) | 스키마/요청 형식 오류로 간주, 즉시 실패 후 규칙 검증 재실행 |

## 2) dead-letter 형식
- `timestamp`
- `request_context`(메소드, 우선순위, 필터 id)
- `error_code`
- `retry_count`
- `action`
- `operator_next_step`

## 3) apply 전 필수 단계
- plan-only pass(모의 실행)
- 충돌 점검(보안, cnu, newsletter/social/group)
- 승인자 체크리스트 통과

## 4) 적용 중단 기준
- 동일 메시지/요청에서 실패율이 3회 연속 누적되는 경우
- 401 재발 + 동일 자격증명 연속 실패 2회
- dead-letter에 보안 이벤트(토큰 노출/권한 오남용) 패턴 검출

