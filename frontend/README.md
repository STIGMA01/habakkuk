# Vue3.js + Vite + TypeScript + Naive-UI


## 설치
- axios
- vue-router
- pinia
- naive-ui

```bash
npm install axios vue-router pinia naive-ui
```

> **Eslint, Prettier 설치**
> ```
>   # ESLint 관련
> npm install -D eslint eslint-plugin-vue eslint-plugin-import eslint-plugin-unused-imports
> npm install -D prettier eslint-config-prettier eslint-plugin-prettier
> npm install -D @typescript-eslint/parser @typescript-eslint/eslint-plugin
> ```
> 
>

## 실행
```bash
# 기본 개발 모드
npm run dev

# production 모드 빌드
npm run build
```

## 환경 설정
### package.json

**[ 변경사항 ]**  
```json
// --host 0.0.0.0 을 추가함으로서 외부 IP 바인딩을 허용하였다.
...
  "scripts": {
    "dev": "vite --host 0.0.0.0",
    "build": "vue-tsc -b && vite build",
    "preview": "vite preview"
  },
...
```
