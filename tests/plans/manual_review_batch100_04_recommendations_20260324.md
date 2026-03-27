# manual review batch100_04 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_04_20260324.json`
- selection rule:
  - `has:nouserlabels (from:@naver.com OR from:@gmail.com OR from:@outlook.com)`

## batch-level summary
- total messages: `100`
- dominant sender: `chany010713@gmail.com` (`77/100`)
- second sender: `help@help.naver.com` (`18/100`)
- other senders are small residuals and should be triaged individually only if they repeat later.

## recommended triage by dominant pattern
### 1) `chany010713@gmail.com` self-thread / university admin cluster
- recommended default state: `@GTD/Reference`
- use `@GTD/Action` only when the message is an active submission, request, or immediate reply target.
- use `@GTD/Waiting` only when it is clearly a reply chain waiting on another party.

#### dominant subject patterns
- `empty subject`
- `김주용`
- `대학원서`
- `경상대 심리학과 20 김주용, 학업과 진로에 관해 고민이 있습니다.`
- `심리학과 김주용 관생회비 반환 신청서`
- `20학번 김주용입니다. 감사합니다!`
- `경상대 기호학의 이해 수강생, 20학번 김주용 과제 제출합니다.`
- `심리학개론 수강생 20학번 김주용입니다(수업관련)`
- `경상대 글쓰기기초 수강생, 김주용 2020010455`
- `어깨동무 성장지원 프로그램 특강 결과보고서 - 김주용`
- `최근 사진 보기`
- `근로 장학 서류`
- `기초글쓰기 김주용 3조 제안서 최종 선정 이유`

#### practical guidance
- Treat repeated `chany010713@gmail.com` messages as thread-level items, not message-level items.
- If the thread is clearly a personal/self note, result, upload confirmation, or attachment delivery, collapse it to `@GTD/Reference`.
- If the thread is a live university request or submission, collapse it to one `@GTD/Action` item.
- If the thread is a back-and-forth waiting on the other side, collapse it to `@GTD/Waiting`.

### 2) `help@help.naver.com` login/security alerts
- recommended state: `@SYS/Security`
- this batch contains repeated login alerts such as `새로운 환경에서 로그인 되었습니다.`
- treat repeated alerts from the same security sender as security-notification clusters, not separate work items.

#### practical guidance
- Collapse repeated `help@help.naver.com` alerts into one security thread per event.
- Do not move these into `@GTD/Action` unless there is an explicit account recovery step.
- If the account event is informational only, `@SYS/Security` is the right default.

### 3) small residual document/file senders
- `ngodaejeon@gmail.com`
  - recommended state: `@GTD/Reference`
  - reason: report resend / record keeping pattern
- `gusdn6245@naver.com`
  - recommended state: `@GTD/Reference`
  - reason: PPT/document attachment exchange pattern
- `ballinnino@naver.com`
  - recommended state: manual review first
  - reason: singleton residual, no stable bulk rule yet

## dedupe notes
- Thread-level dedupe is mandatory for `chany010713@gmail.com`.
- Message count overstates workload here; many messages collapse into a small number of self-thread clusters.
- For `help@help.naver.com`, repeated login alerts should also be deduped at thread/event level.
- Small residual senders should not become new automatic rules unless they repeat in a later batch.

## operational recommendation
- Apply `@SYS/Security` to the Naver login cluster.
- Apply `@GTD/Reference` to the bulk of `chany010713@gmail.com` self-thread messages.
- Escalate only the active submission/request threads to `@GTD/Action` or `@GTD/Waiting`.
- Do not add new auto rules for singleton residuals in this batch.
