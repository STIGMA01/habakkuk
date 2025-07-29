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


## 파일 구조
- src/views 디렉토리에는 애플리케이션의 특정 "페이지" 또는 "뷰"를 나타내는 최상위 컴포넌트들을 배치합니다.
- src/components 디렉토리에는 애플리케이션 전반에서 재사용될 수 있는 작은 단위의 UI 컴포넌트들을 배치합니다. 이들은 독립적인 기능을 가지며, 다양한 페이지나 다른 컴포넌트 내에서 활용될 수 있습니다.
>   **특징:**
>
>    - 단일 책임 원칙을 따르는 경향이 있습니다. (예: 버튼, 카드, 입력 필드, 헤더 등)  
>    - 명확한 props를 통해 데이터를 받고, emits를 통해 이벤트를 발생시킵니다.  
>    - 대개 자체적인 데이터 페칭 로직을 직접 수행하기보다는, 부모 컴포넌트(주로 뷰 컴포넌트)로부터 데이터를 받아서 표시하는 **표현 컴포넌트**의 역할을 합니다.  
>    - 다른 페이지나 뷰에서 범용적으로 사용될 수 있도록 일반화되어 있습니다.  
>
>   **예시:**
>
>    * src/components/common/Button.vue  
>    * src/components/ui/Modal.vue  
>    * src/components/layout/AppHeader.vue  
>    * src/components/product/ProductCard.vue  
>    * src/components/user/UserAvatar.vue  
 