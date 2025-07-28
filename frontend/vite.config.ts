//
//   :WARNING
// define으로 넣은 변수는 전처리 시점에 코드에 "하드코딩"된다.
// → 보안 이슈가 없게 서버 비밀정보는 절대 포함하면 안 된다!
//

import { 
  defineConfig, 
  loadEnv 
} from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd()) as unknown as ImportMetaEnv

  return {
    plugins: [vue()],
    define: {
      __APP_ENV__: JSON.stringify(env.VITE_APP_ENV),
    },
    server: {
      port: 5173,
      proxy: {
        '/api': {
          target: env.VITE_API_URL || 'http://localhost:8000',
          changeOrigin: true,
          rewrite: path => path.replace(/^\/api/, '/api'),
        }
      }
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src'),
      },
    },
    build: {
      outDir: 'dist',
    }
  }
})

