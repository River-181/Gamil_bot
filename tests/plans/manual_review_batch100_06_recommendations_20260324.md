# manual review batch100_06 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_06_20260324.json`
- sample basis:
  - `/Users/river/tools/gmail-agent-sys/tests/plans/manual_review_queue_20260324.md`
  - `/Users/river/tools/gmail-agent-sys/docs/manual_work_residual_policy_v1.md`
  - `/Users/river/tools/gmail-agent-sys/docs/thread_manual_triage_ops_v1.md`

## dominant patterns

### 1) Naver security/login cluster
- sender:
  - `help@help.naver.com`
- volume:
  - `27 messages`
  - `21 threads`
- common subjects:
  - `새로운 환경에서 로그인 되었습니다.`
  - `비밀번호가 변경되었습니다.`
  - `요청하신 인증번호를 알려드립니다.`
- recommended state:
  - `@GTD/Action`
- reason:
  - account/security follow-up is the dominant intent
  - if the account is already verified, the thread can be downgraded to `@GTD/Reference` after one review pass

### 2) R&D mentoring / submission cluster
- sender:
  - `euclidsoft.edu@gmail.com`
- volume:
  - `10 messages`
  - `4 threads`
- common subjects:
  - `Re: [제출] R&D 프로젝트 멘토링_결과보고서 제출, 17-망상궤도-김주용`
  - `Re: [제출] R&D 프로젝트 멘토링_지출품의서 (망상궤도 김주용)`
  - `Re: [제출] R&D 프로젝트 멘토링_발표자료 제출, 17-망상궤도-김주용`
  - `Re: [제출] R&D 프로젝트 멘토링_수행계획서, 17-망상궤도-김주용`
- recommended state:
  - `@GTD/Waiting`
  - `@GTD/Reference` for already-submitted artifacts
- reason:
  - same project family repeats across multiple threads
  - one thread should hold one state only

### 3) Chargeback / refund follow-up cluster
- sender:
  - `doogie233@naver.com`
- volume:
  - `4 messages`
  - `1 thread`
- common subject:
  - `Re: [환급신청]충남대 데이터베이스 수업 SQLD 자격증 수수료 환급 신청`
- recommended state:
  - `@GTD/Waiting`
- reason:
  - administrative follow-up with external response pending
  - dedupe as one thread, not four messages

### 4) Contract / project coordination cluster
- sender:
  - `djglocal25@naver.com`
- volume:
  - `3 messages`
  - `2 threads`
- common subjects:
  - `Re: [2026 장인학교 해커톤] 망상궤도 팀, 비교견적 및 계약 문의`
  - `RE: [2026 장인학교 해커톤] 망상궤도 팀, 비교견적 및 계약 문의`
  - `Re: 장인학교 해커톤 대체과제 안내`
- recommended state:
  - `@GTD/Action` for contract / quote thread
  - `@GTD/Waiting` for the alternate-task follow-up thread
- reason:
  - one thread is active action, the other is a pending response path

## secondary patterns

- `minjugim655@gmail.com`
  - mentoring submission / project paperwork
  - recommend `@GTD/Waiting` or `@GTD/Reference` depending on whether the thread is still open

- `aa01053208720@gmail.com`
  - `오사카 여행계획`
  - recommend `@GTD/Action`

- `bigkinds571@gmail.com`
  - privacy reconfirmation / account notice
  - recommend `@GTD/Action` if reconsent is still needed, otherwise `@GTD/Reference`

- `dptmf702@gmail.com`
  - grade / reply thread
  - recommend `@GTD/Waiting`

- `ade26594@gmail.com`
  - experiment participation / documents
  - recommend `@GTD/Waiting`

- `gusdn6245@naver.com`
  - document/file-like subject
  - recommend `@GTD/Reference`

- `oneulst1@naver.com`
  - photo attachment delivery
  - recommend `@GTD/Reference`

- `outlook_7A89390CA06E025E@outlook.com`
  - offline meeting
  - recommend `@GTD/Action`

- `kang.songyi785@gmail.com`
  - simple greeting thread
  - recommend `@GTD/Read` or `@GTD/Reference`

- `hoam518@gmail.com`
  - university course / backup discussion
  - recommend `@GTD/Waiting` for active reply threads, `@GTD/Reference` for archived backup material

## dedupe notes

- Same thread should be treated as one GTD item.
- Security/login bursts from `help@help.naver.com` repeat across many messages, but they collapse into a smaller thread set. Keep one state per thread.
- `euclidsoft.edu@gmail.com` appears across several mentoring/document threads; split by thread, not by sender alone.
- `doogie233@naver.com` is a single refund thread repeated across multiple messages; dedupe aggressively.
- `djglocal25@naver.com` has at least two separate threads and should not be flattened into one state.
- Self-like or simple repeated personal threads should default to `@GTD/Reference` once the content is captured.

## practical triage guidance

1. Prioritize `@GTD/Action` on the `help@help.naver.com` security/login thread family.
2. Keep the mentoring/document family under `@GTD/Waiting` until the thread is resolved, then downgrade to `@GTD/Reference`.
3. Keep refund and grade reply threads under `@GTD/Waiting`.
4. Use `@GTD/Reference` for delivered files, templates, or already-captured personal notes.
5. Do not create new auto-label rules from this batch; the useful boundary here is manual triage, not sender automation.
