# Phase 9 레거시 라벨 베이스라인 (2026-03-05)

## 목적
- 현재 Gmail 라벨 집합을 v3 정책 기준으로 분류해, Legacy 라벨만 선별한다.
- 이후 아카이브 마이그레이션의 기준 집합으로 고정한다.

## 기준
- v3 정책 경로: `config/labels.v3.json`
- v3 라벨 수: `14`
- 마이그레이션 범위: `legacy-user`
- 아카이브 루트: `#Archive/Legacy-20260305`
- 제외 라벨:
  - `@AUTO/*`, `@CTX/*`, `@CNU/*`, `@SYS/*`, `@GTD/*` (v3 라벨)
  - Gmail 시스템 라벨 (`INBOX`, `SENT`, `STARRED`, `CATEGORY_*`, `UNREAD` 등)
  - 기존 Shadow Archive 라벨(`#Archive/Legacy-20260305/*`)

## 산출 항목
- Legacy user label 이름 목록
- legacy 라벨 개수
- 각 legacy 라벨에 대한 아카이브 라벨 경로 매핑 준비 상태
- 충돌 점검 결과

## 작성 규칙
- 라벨별 분류 기준은 `legacy-user` 스코프로 고정
- 매핑은 `tests/plans/phase9_archive_mapping_20260305.json`에 저장
- 충돌 없을 때만 다음 단계(Stage 200) 진행

## 다음 단계
- `docs/runbooks/legacy_label_archive_migration_v1.md`의 Stage A 실행 승인
- 실행 전 `--dry-run --archive-migrate`로 결과 dry run 기록

