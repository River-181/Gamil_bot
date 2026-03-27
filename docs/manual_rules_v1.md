Manual rules (v1)

Purpose
Manual GTD rules for high-confidence senders only. These are intended to be used by the self-sent exception path and should not expand beyond confirmed families without review.

Rules added (manual namespace)
- rule_manual_self_reference -> @GTD/Reference
  - sender: chany010713@gmail.com
  - subjects: "안녕하세요", "삼겹살 600g", "21 학기 기말고사 정리", "실험 전 필독 사항 CAR", "[재무로그"
- rule_manual_action_djglocal25 -> @GTD/Action
  - sender: djglocal25@naver.com
  - subjects: 견적, 계약, 해커톤, 대체과제
- rule_manual_waiting_doogie233 -> @GTD/Waiting
  - sender: doogie233@naver.com
  - subject: 환급신청
- rule_manual_waiting_euclidsoft -> @GTD/Waiting
  - sender: euclidsoft.edu@gmail.com
  - subjects: 멘토링, 지출품의서, 결과보고서, 발표자료
- rule_manual_action_outlook_meeting -> @GTD/Action
  - sender: outlook_7a89390ca06e025e@outlook.com
  - subject: 오프라인 미팅
- rule_manual_action_aa01053208720 -> @GTD/Action
  - sender: aa01053208720@gmail.com
  - subject: 오사카 여행계획

Notes
- These rules are intentionally narrow and rely on sender + subject patterns.
- Any expansion should be justified by manual review batches and kept minimal.
