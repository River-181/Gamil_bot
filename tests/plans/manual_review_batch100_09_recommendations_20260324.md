# manual review batch100_09 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_09_20260324.json`
- selection rule:
  - `has:nouserlabels from:chany010713@gmail.com`

## batch-level summary
- total messages: `100`
- dominant sender: `chany010713@gmail.com` (`100/100`)
- this batch is a self-thread / university-admin / personal-record cluster.
- message count overstates workload here; thread-level dedupe is mandatory.

## recommended triage by dominant pattern
### 1) self-thread reference cluster
- recommended default state: `@GTD/Reference`
- use this for:
  - repeated self threads
  - study notes
  - attached files
  - draft materials
  - submission confirmations that do not need follow-up

#### dominant thread patterns
- `삼겹살 600g`
  - `22 messages`
  - recommended state: `@GTD/Reference`
- `21 학기 기말고사 정리`
  - `6 messages`
  - recommended state: `@GTD/Reference`
- `https://www.google.co.kr/url?...contents.kocw.or.kr...`
  - `5 messages`
  - recommended state: `@GTD/Reference`
- `심리학과`
  - `4 messages`
  - recommended state: `@GTD/Reference`
- `실험 전 필독 사항 CAR`
  - `3 messages`
  - recommended state: `@GTD/Reference`
- `IBR서류`
  - `2 messages`
  - recommended state: `@GTD/Reference`
- `심리학과 학생회 이름`
  - `2 messages`
  - recommended state: `@GTD/Reference`
- `ㅇ`
  - `2 messages`
  - recommended state: `@GTD/Reference`
- `실험참가 메뉴얼과 서류`
  - `2 messages`
  - recommended state: `@GTD/Reference`
- `신경과학`
  - `2 messages`
  - recommended state: `@GTD/Reference`
- `1-2 고전사회학 강의 필기`
  - `2 messages`
  - recommended state: `@GTD/Reference`
- `재적증명서`
  - singleton
  - recommended state: `@GTD/Reference`
- `김주용 사진`
  - singleton
  - recommended state: `@GTD/Reference`
- `Welcome to EpocCam`
  - singleton
  - recommended state: `@GTD/Reference`
- `김주용 발표자료`
  - singleton
  - recommended state: `@GTD/Reference`

### 2) active request / reply threads
- recommended states: `@GTD/Action` or `@GTD/Waiting`
- use `@GTD/Action` when the thread is an open request that still needs a response or submission.
- use `@GTD/Waiting` when the thread is clearly awaiting someone else’s reply.

#### dominant request patterns
- `전생애발달심리학 보고서 주제 선정 및 줌 자문 - 김주용`
  - `2 messages`
  - recommended state: `@GTD/Action`
- `안녕하세요 선생님! 주용입니다! - 인터뷰 가능 여부에 관해서`
  - singleton
  - recommended state: `@GTD/Action`
- `심리통계 1 성적 문의 답변드립니다.`
  - `2 messages`
  - recommended state: `@GTD/Waiting`
- `경상대 심리학과 20 김주용, 학업과 진로에 관해 고민이 있습니다.`
  - `2 messages`
  - recommended state: `@GTD/Waiting` or `@GTD/Action` depending on whether reply is pending or new outreach is needed
- `경상대 글쓰기기초 수강생, 김주용 2020010455`
  - singleton
  - recommended state: `@GTD/Action`
- `경상대 기호학의 이해 수강생, 20학번 김주용 과제 제출합니다.`
  - `2 messages`
  - recommended state: `@GTD/Action`
- `심리학개론 수강생 20학번 김주용입니다(수업관련)`
  - `2 messages`
  - recommended state: `@GTD/Waiting`
- `근로 장학 서류`
  - singleton
  - recommended state: `@GTD/Action`
- `어깨동무 성장지원 프로그램 특강 결과보고서 - 김주용`
  - singleton
  - recommended state: `@GTD/Reference`

## dedupe notes
- This batch should be deduped primarily by thread subject, not by message count.
- `삼겹살 600g` is one large self thread, not 22 independent tasks.
- Repeated academic notes, PDFs, and attachments are reference material unless they are explicitly awaiting action.
- `chany010713@gmail.com` should remain manual-review only; do not create new auto rules for this sender.

## operational recommendation
- Apply `@GTD/Reference` to the large majority of the batch.
- Escalate only active request/reply threads to `@GTD/Action` or `@GTD/Waiting`.
- Keep self-thread notes and file deliveries out of `@AUTO/*`.
