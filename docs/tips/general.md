
## 기획/설계
### Versioning
1. SemVer (Semantic Versioning, 의미적 버저닝) – 가장 널리 쓰임  

> MAJOR.MINOR.PATCH  
> 깨짐 -  추가  - 수정  

    예: 2.4.1  

        2 → MAJOR: 하위 호환성 없는 변경  

        4 → MINOR: 기능 추가, 하위 호환 유지  

        1 → PATCH: 버그 수정 등 사소한 변화  

    예: 3.0.0-alpha.1, 1.2.3-beta, 1.2.3+build45  


## Git
### Git commit 예시

| 타입       | 설명                                     |
| -------- | -------------------------------------- |
| feat     | 새로운 기능 추가                              |
| fix      | 버그 수정                                  |
| docs     | 문서 수정                                  |
| style    | 코드 포맷팅, 세미콜론 누락 등 스타일 관련 변경 (로직 변경 없음) |
| refactor | 코드 리팩토링 (기능 변경 없음)                     |
| perf     | 성능 개선                                  |
| test     | 테스트 추가/수정                              |
| chore    | 빌드 업무 수정, 패키지 매니저 설정 변경 등 기타 잡일        |
| revert   | 이전 커밋 되돌리기                             |


### Git Branch 예시

| 타입          | 예시                                   | 설명             |
| ----------- | ------------------------------------ | -------------- |
| main/master | `main`                               | 프로덕션 배포 코드     |
| develop     | `develop`                            | 통합 개발 브랜치      |
| feature     | `feature/login`, `feature/ui-update` | 기능 개발 브랜치      |
| release     | `release/1.0.0`, `release/1.1.0`     | 배포 준비 브랜치      |
| hotfix      | `hotfix/fix-login-bug`               | 긴급 버그 수정 브랜치   |
| chore       | `chore/update-deps`                  | 환경설정, 의존성 업데이트 |

