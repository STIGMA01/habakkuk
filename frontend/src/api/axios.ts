import axios from 'axios'

const base = import.meta.env.VITE_API_URL || 'http://localhost:8000'
const baseURL = base.endsWith('/api') ? base : `${base}/api`

const api = axios.create({
  baseURL,
  timeout: 5000
})

export default api
