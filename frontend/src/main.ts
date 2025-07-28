import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import naive from 'naive-ui'
import pinia from './store/index.ts'

import './style.css'

const app = createApp(App)

app.use(router)
app.use(pinia)
app.use(naive)

app.mount('#app')
