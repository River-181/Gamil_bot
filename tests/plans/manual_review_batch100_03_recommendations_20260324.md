# manual review batch100_03 recommendations 2026-03-24

## source
- batch file:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch100_03_20260324.json`
- query:
  - `has:nouserlabels (from:@naver.com OR from:@gmail.com OR from:@outlook.com)`
- count:
  - `100`

## dominant patterns

### pattern A. self-thread / personal study notes
- dominant sender:
  - `chany010713@gmail.com`
- volume:
  - `68 / 100`
- common subjects:
  - blank subject
  - `Re: 21 학기 기말고사 정리`
  - `Re: 실험 전 필독 사항 CAR`
  - `Re: 심리학과`
  - `Re: 실험참가 메뉴얼과 서류`
  - `1-2 고전사회학 강의 필기`
  - long Google URL subject
- recommended state:
  - `@GTD/Reference`
- reason:
  - repeated self thread
  - notes, drafts, study fragments, and forwarded references

### pattern B. academic admin / lab / class coordination
- recurring senders:
  - `bigkinds571@gmail.com`
  - `ade26594@gmail.com`
  - `dptmf702@gmail.com`
  - `powerjjh95@naver.com`
  - `0720jenny@gmail.com`
  - `cnu.global.study.abroad@gmail.com`
  - `cheol.hwan.kim2391@gmail.com`
  - `junokorea66@naver.com`
  - `neuroscience.han@gmail.com`
  - `suk.w.han@gmail.com`
  - `zkfp4334@naver.com`
  - `euisoljeong@gmail.com`
  - `doodle.fac@gmail.com`
  - `rlaendhks123@naver.com`
  - `apply758@gmail.com`
  - `1102jtw@naver.com`
- common subjects:
  - `빅카인즈에서 개인정보 취급 재동의 관련 안내드립니다.`
  - `Re: 심리통계 1 성적 문의 답변드립니다.`
  - `Re: 실험참가 메뉴얼과 서류`
  - `RE: CNU_운영체제_과제3_김주용(202100739)`
  - `RE: 충남대학교 2022_취업과 창업 과제4_김주용(202100739)`
  - `취업과 창업 교육조교 장준호입니다.`
  - `긴급휴강 공지`
  - `실험 심리 실험한거여!!`
- recommended states:
  - `@GTD/Waiting` for reply-needed administrative threads
  - `@GTD/Action` for pending task/assignment/response requests
  - `@GTD/Reference` for notices, receipts, and materials-only threads
- reason:
  - these are mostly academic coordination threads rather than promo/newsletter
  - thread state should be decided at thread level, not message level

### pattern C. notices / recurring info mail
- examples:
  - `bigkinds571@gmail.com`
  - `cnu.global.study.abroad@gmail.com`
  - `suk.w.han@gmail.com`
- recommended state:
  - `@GTD/Reference`
  - sometimes `@GTD/Read` if no follow-up is needed
- reason:
  - informational, usually not actionable

## practical triage guidance
1. Treat `chany010713@gmail.com` as one self-thread family and dedupe aggressively.
2. For academic/admin senders, classify by thread intent:
   - request or deadline -> `@GTD/Action`
   - awaiting reply or confirmation -> `@GTD/Waiting`
   - attachment/material/notice -> `@GTD/Reference`
3. Do not force these senders into `@AUTO/*` unless the thread is clearly repetitive notice traffic.
4. For repeated subjects with the same sender, prefer one thread-level decision over per-message labeling.

## dedupe notes
- `chany010713@gmail.com` accounts for most of the batch. Multiple messages with the same blank or near-identical subject should collapse to one `Reference` thread.
- `Re: 실험참가 메뉴얼과 서류` appears across multiple senders and should be handled as a single coordination thread family where possible.
- `빅카인즈 개인정보 재동의` is a recurring notice pattern. Keep as `Reference`, not `Action`.
- Long subject variants that are clearly the same study note or forwarded reference should not be split into separate triage items.

## recommended default states by sender family
- `chany010713@gmail.com` -> `@GTD/Reference`
- academic admin / lab coordination -> `@GTD/Waiting` or `@GTD/Action`
- notice-only senders -> `@GTD/Reference` or `@GTD/Read`

