import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about', 
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/r',
    name: 'reg',
    component: () => import('../views/RegistraciaView.vue')
  },
  {
    path: '/s',
    name: 'sravn',
    component: () => import('../views/SravnView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
