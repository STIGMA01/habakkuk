



## 보안

> "클라이언트로 보내는 순간, 모든 값은 공개된 것과 다름없다"
> 클라이언트는 “보여주는 용도”, 보안은 서버가 책임지는 구조로 만드세요.

### 프록시를 통해 BE API에 연결

```javascript

// vite.config.ts
...
    server: {
      proxy: {
        '/api': {
          target: env.VITE_API_URL,
          changeOrigin: true,
          rewrite: path => path.replace(/^\/api/, '/api'),
        },
      },
    },
...

// src/api.ts
import axios from 'axios'

const api = axios.create({
  baseURL: '/api', // 프록시 통해 백엔드 연결
})

api.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api
```

