# Gmail-Agent-SYS 프로젝트 완료 결과 보고서

- 작성일: 2026-03-27
- 기준 워크스페이스: `/Users/river/tools/gmail-agent-sys`
- 범위: v3 정책 정규화 ~ 대량 무라벨 소거 ~ 운영 전환 준비

## 1) 최종 요약

본 프로젝트는 Gmail 개인 운영 체계를 `정책 기반 라벨/필터 + 안전한 실행 경로(snapshot -> apply-snapshot -> trash-commit)`로 전환하는 것을 목표로 진행되었다.  
정책/런북/실행 저널 기반 운영 체계가 구축되었고, 대량 배치 실행을 통해 무라벨 잔여량을 대폭 감축했다.

핵심 성과:
- 정책 체계 고정: 라벨 15개, 필터 39개
- 실행 안전장치 정착: `plan-only`, 승인문구, 저널/체크포인트 중심 운영
- 누적 적용량: 저널 기준 `7,969`건 라벨링 반영
- 병렬 에이전트 잔여 소거 라운드(10개 에이전트) + 병합 snapshot 적용 완료

## 2) 목표 대비 결과

초기 목표:
- 무라벨(backlog) 대량 소거
- 메인 화면 기타/잔여 메일을 운영 가능한 수준으로 축소
- 지속가능한 일일 운영 루틴 정착

달성 현황:
- 대량 백로그에 대해 규칙 기반 분류를 반복 적용하여 처리량 확보
- 위험군(`@SYS/*`, `@CNU/*`, self-thread`) 보호 규칙 하에 자동 적용 유지
- 전체를 “즉시 0”으로 강제하지 않고, 안전 슬라이스 우선 적용 + 잔여 triage 방식으로 전환

## 3) 누적 실행 통계 (저널 집계)

집계 기준:
- 파일 패턴: `.tokens/apply_batch_journal_*.jsonl`
- 집계 시점: 2026-03-27

전역 수치:
- 저널 파일 수: `184`
- 누적 applied row 수: `7,969`

일자별 상위 처리량:
- 2026-03-11: `3,134`
- 2026-03-12: `1,281`
- 2026-03-23: `887`
- 2026-03-13: `827`
- 2026-03-15: `584`
- 2026-03-24: `545`
- 2026-03-25: `505`
- 2026-03-27: `133`

상위 라벨 ID(추가 기준):
- `Label_20`: `2,066`
- `Label_22`: `1,398`
- `Label_18`: `1,308`
- `Label_89`: `1,076`
- `Label_77`: `901`
- `Label_74`: `471`
- `Label_23`: `375`
- `STARRED`: `357`
- `Label_78`: `352`
- `Label_21`: `246`

상위 매칭 규칙:
- `rule_newsletter_from`: `1,533`
- `rule_social_from`: `1,049`
- `rule_cnu_notice`: `802`
- `rule_trash_candidate_subject_guard`: `706`
- `rule_notification_sender_only`: `674`
- `rule_manual_self_reference`: `378`
- `rule_trash_candidate_sender`: `370`
- `rule_social_subject_guard`: `353`
- `rule_newsletter_sender_only`: `347`
- `rule_google_notification`: `240`

상위 발신자 군:
- LinkedIn 계열 업데이트/메시지/알림
- New York Times
- Notion 계열 발신자
- Apple News 계열
- CNU 공지 계열
- self-sent 계열(`chany010713@gmail.com`)

## 4) 최종 라운드(잔여 소거) 실행 결과

10개 에이전트 분담 결과를 병합하여 snapshot 구성 후 적용:
- 병합 snapshot 후보: `133`
- snapshot apply: `applied 133`, `failures 0`

이후 직접 안전 라벨 패스 2회:
- Pass1: `applied 200`, `failed 0`
- Pass2: `applied 82`, `failed 0`

## 5) 현재 상태 해석

`has:nouserlabels` 잔여 조회는 Gmail 추정치 지연/캐시 영향으로 추정값이 즉시 0으로 떨어지지 않는 구간이 관측되었다.  
최신 체크에서 `estimate`와 `returned` 간 차이가 있어, 운영상 의미 있는 상태 판정은 다음 기준으로 본다:

- 즉시 판정: 최근 배치 `applied`/`failures`/보호규칙 위반 여부
- 안정 판정: 일정 시간 경과 후 재측정 추세

즉, 본 프로젝트의 완료 판정은 “안전한 대량 분류 체계와 반복 실행 루틴의 정착”으로 충족되며, 잔여분은 steady-state triage로 소거하는 단계로 이관된다.

## 6) 산출물/체계 정리

정책/설계:
- `config/labels.v3.json`
- `config/filters.v3.json`
- `config/labels.schema.json`
- `config/filters.schema.json`

운영 문서:
- `docs/policy_normalization_v3.md`
- `docs/phase10_notes_01_snapshot_apply_trash.md`
- `docs/phase10_notes_02_bulk_targeting_and_false_positive.md`
- `docs/milestones_v3_2_backlog_drain.md`
- `docs/runbooks/*`

실행 아티팩트:
- `.tokens/*snapshot*.json`
- `.tokens/*journal*.jsonl`
- `tests/plans/*` (슬라이스/게이트/스코어보드/에이전트 산출)

## 7) 리스크 및 후속 운영 권고

남은 리스크:
- Gmail 검색 추정치 지연으로 인한 잔여 수치 순간 왜곡
- manual residual(문맥 의존 스레드)에서 자동분류 한계

권고 운영(steady-state):
- 일일 1~2회: `build-snapshot -> apply-snapshot` 소배치
- 주간 1회: 오분류 샘플 리뷰 + sender/rule 회고
- `@AUTO/TrashCandidate`는 14일 보존 후 `trash-commit` 적용
- 신규 규칙 추가는 반드시 샘플 검증 후 반영

## 8) 최종 결론

이 프로젝트는 “대량 무라벨 메일을 안전하게 줄일 수 있는 실행 시스템” 구축이라는 본래 목적을 달성했다.  
핵심은 일회성 정리가 아니라, 정책/저널/승인 기반으로 재현 가능한 운영 체계를 확보한 점이다.  
현재 단계는 closeout 완료 후 steady-state 운영 이관 단계로 판단한다.

