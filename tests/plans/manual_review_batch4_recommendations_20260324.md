# manual review batch4 recommendations 2026-03-24

## source
- batch:
  - `/Users/river/tools/gmail-agent-sys/.tokens/manual_review_batch_50_20260324.json`
- sample slice:
  - items 31-40

## recommended triage
1. `194ea252b71a422b`
- sender: `aa01053208720@gmail.com`
- subject: `오사카 여행계획`
- recommended state: `@GTD/Action`
- reason: 실제 여행 준비/일정 정리 가능성 높음

2. `194e4f7499dd046f`
- sender: `aa01053208720@gmail.com`
- subject: `오사카 여행계획`
- recommended state: `@GTD/Action`
- reason: 동일 스레드

3. `18c21cf7b55aba0e`
- sender: `kang.songyi785@gmail.com`
- subject: `Re: 안녕하세요!`
- recommended state: `@GTD/Read`
- reason: 개인 인사/대화 시작 스레드, 맥락 확인 후 종료 가능성

4. `18b308f80b91b73d`
- sender: `kang.songyi785@gmail.com`
- subject: `안녕하세요!`
- recommended state: `@GTD/Read`
- reason: 동일 성격

5. `18a58d101c74b80a`
- sender: `chany010713@gmail.com`
- subject: `안녕하세요`
- recommended state: `@GTD/Reference`
- reason: self thread, 자동 처리보다 보존이 안전

6. `18a58d101c5196e9`
- sender: `chany010713@gmail.com`
- subject: `안녕하세요`
- recommended state: `@GTD/Reference`
- reason: 동일 스레드

7. `18a58d1018f8baba`
- sender: `chany010713@gmail.com`
- subject: `안녕하세요`
- recommended state: `@GTD/Reference`
- reason: 동일 스레드

8. `18a58d101803484b`
- sender: `chany010713@gmail.com`
- subject: `안녕하세요`
- recommended state: `@GTD/Reference`
- reason: 동일 스레드

9. `18a58d10177dc432`
- sender: `chany010713@gmail.com`
- subject: `안녕하세요`
- recommended state: `@GTD/Reference`
- reason: 동일 스레드

10. `18a58d101751f115`
- sender: `chany010713@gmail.com`
- subject: `안녕하세요`
- recommended state: `@GTD/Reference`
- reason: 동일 스레드

## application notes
- 여행 계획 메일은 `Action`으로 두는 편이 실용적이다.
- 짧은 인사성 개인 메일은 `Read`로 두고 직접 열어 확인 후 정리한다.
- self sender 반복 메일은 thread 기준으로 `Reference` 한 번만 잡아도 충분하다.
