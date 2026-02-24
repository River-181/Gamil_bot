# Gmail Mail Flow

```mermaid
graph TD
    A[새 메일 수신] --> B{필터 엔진}
    B -->|매칭 없음| C[인박스 유지]
    B -->|@SYS/Security 우선| D[@SYS/Security 적용]
    B -->|@CNU/학생| E[@CNU/학생 적용]
    B -->|@CNU/뉴스알림| F[@CNU/뉴스알림 적용]
    B -->|@AUTO/Receipt| G[@AUTO/Receipt + @CTX/Finance]
    B -->|@CTX/Travel| H[@CTX/Travel]
    B -->|@AUTO/Social| I[@AUTO/Social]
    B -->|@AUTO/Promo| J[@AUTO/Promo]
    B -->|@AUTO/Newsletter| K[@AUTO/Newsletter]
    B -->|@AUTO/Notification| L[@AUTO/Notification]

    D --> M1[인박스 유지, 중요표시]
    E --> M2[인박스 유지, Star]
    F --> M3[Skip Inbox + Read]
    G --> M4[Skip Inbox + Read]
    H --> M5[Skip Inbox]
    I --> M6[Skip Inbox + Read]
    J --> M7[Skip Inbox + Read]
    K --> M8[Skip Inbox + Read]
    L --> M9[Skip Inbox + Read]

    C --> N1[사용자 수동 @GTD 적용]
    M1 --> N1
    M2 --> N1
    N1 --> O{State 라벨링}
    O -->|오늘 처리| P[@GTD/Action]
    O -->|응답 대기| Q[@GTD/Waiting]
    O -->|참고용 저장| R[@GTD/Reference]
    O -->|읽고 아카이브| S[@GTD/Read]

    P --> T[운영 체크포인트: 주간/월간 점검]
    Q --> T
    R --> T
    S --> T
```
