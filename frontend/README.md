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
* `--host 0.0.0.0` 을 추가함으로서 외부 IP 바인딩을 허용하였다.
* --host는 개발 환경에서만 적용하고, 상용 환경의 경우 적용해선 안된다.

```json
  "scripts": {
    "dev": "vite --host 0.0.0.0",
    "build": "vue-tsc -b && vite build",
    "preview": "vite preview"
  },
```


## 📄 License

This project is licensed under the [Creative Commons BY-NC-ND 4.0 License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

