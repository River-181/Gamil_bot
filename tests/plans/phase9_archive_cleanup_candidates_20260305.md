# Phase 9 Legacy 삭제 후보 정리 계획 (2026-03-05)

## 전제
- run_id: `20260305T171000Z`
- 마이그레이션 상태: `done`
- 처리 메시지: `messages_scanned=1392`, `run_messages=745`, `applied=576`
- 보존 정책: 원본 라벨 보존(keep) + 14일 후 삭제 승인

## 14일 보존 운영
- 보존 대상 라벨: legacy-user로 추출된 라벨 전체
- legacy 라벨 수: `42`
- 보존 종료일: 마이그레이션 완료 시점 기준 +14일
- 보존 종료 전 점검:
  - 최근 24시간 오분류 피드백 수집
  - 시스템 검색/필터 영향 점검(중요: `SYS`, `CNU`, `INBOX` 관련 흐름)

## 삭제 후보
- `#Archive/20241124-26. 후쿠오카 여행`
- `#Archive/20241230-20250206. 산티아고 순례길`
- `#Archive/경상대`
- `#Archive/경상대/경상대`
- `#Archive/경상대/과기철`
- `#Archive/경상대/대학영어`
- `#Archive/경상대/행복심리학`
- `#Archive/고등학교 과제`
- `#Archive/기타/설문`
- `#Archive/뉴스레터`
- `#Archive/뉴스레터/디스콰이엇`
- `#Archive/뉴스레터/외신`
- `#Archive/뉴스레터/출판`
- `#Archive/라이나생명_무배당THE건강한치아보험`
- `#Archive/쇼핑`
- `#Archive/영수증`
- `#Archive/영수증/기타`
- `#Archive/영수증/애플`
- `#Archive/영수증/에픽게임즈`
- `#Archive/영수증/주거통신`
- `#Archive/은행`
- `@To me`
- `AI`
- `Active Project/ABC PM`
- `Active Project/Apple Developer Academy`
- `Active Project/[SanS] 시안`
- `Active Project/로컬해커톤`
- `Akiflow`
- `Cold outreach`
- `[Notion]`
- `n8n/n8n/Notion Account`

## 삭제 실행 기준(수동 승인)
1. `phase9_archive_post_apply_review_20260305.md` 샘플 검토 통과
2. 오분류 건수: 수용 기준 초과 없음(현재 0건 샘플 기반 추정)
3. `--archive-rollback`으로 전체 역적용 리허설이 필요할 경우 별도 승인 수행
4. `Gmail 삭제 승인`: 각 legacy 라벨 단위로 dry-run 확인 후 삭제 적용

## 실행 방법(권장)
1. 삭제 전 `.tokens/archive_migration_checkpoint_20260305T171000Z.json` 스냅샷 보관
2. 1차 승인(소량) → 2차 승인(전체)
3. 삭제 후 24시간 이슈 모니터링
