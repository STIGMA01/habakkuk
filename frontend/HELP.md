# HELP

## What is 'tsconfig'?

| 파일명                  | 역할                  | 주요 포인트                                   |
| -------------------- | ------------------- | ---------------------------------------- |
| `tsconfig.json`      | 루트 설정 파일            | 하위 `app`, `node` 구성 파일을 `references`로 연결 |
| `tsconfig.app.json`  | Vue + Vite 앱 코드용    | 실제 `.vue`, `.ts` 앱에 적용                   |
| `tsconfig.node.json` | Vite config 등 Node용 | Vite config용 고급 타입 설정                    |


## vite.config.ts
Vite의 설정 파일을 통해 빠르게 웹페이지를 구축할 수 있습니다.  
https://vite.dev/config/


## What is pinia?
전역 상태 관리 (Global State Management)

📌 예시 상황  
* 사용자 로그인 상태 (isLoggedIn)  
* 로그인한 유저 정보 (user)  
* 장바구니에 담은 상품 리스트 (cartItems)  
* 자막 편집 프로젝트에서 현재 선택된 문장, 편집 상태 등  



