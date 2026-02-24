# hooks/pre_context.md

## 사용 시점
`SessionStart` 전/후에 컨텍스트 준비를 위한 참조 문서 목록을 로드한다.

## 동작(샘플)
1. `CLAUDE.md`, `AGENTS.md` 존재 여부 확인
2. `config/labels.v3.json`, `config/filters.v3.json`, `config/mcp.server.json` 존재 여부 확인
3. 없으면 사용자에게 다음 항목 보완을 요청
4. 마스킹 규칙(토큰/비밀키 문자열 패턴) 적용

## 산출 포맷
```json
{
  "status": "ready|blocked",
  "missing": ["path1", "path2"],
  "warnings": ["hint1"]
}
```

