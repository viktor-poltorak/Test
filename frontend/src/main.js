import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000"
const header = "Authorization: Basic " + btoa("admin:pass")
axios.defaults.headers["Authorization"] = header


const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
