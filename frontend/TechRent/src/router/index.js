import { createRouter, createWebHistory } from 'vue-router'
import LoginUser from '../components/LoginUser.vue'
import RegisterUser from '../components/RegisterUser.vue'
import ForgotPassword from '../components/ForgotPassword.vue'
import Dashboard from '../components/Dashboard.vue'
import BrowseItems from '../Views/BrowseItems.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/login',
      name: 'LoginUser',
      component: LoginUser
    },
    {
      path: '/register',
      name: 'RegisterUser',
      component: RegisterUser
    },
    {
      path: '/forgotpassword',
      name: 'ForgotPassword',
      component: ForgotPassword
    },
    {
      path: '/browse',
      name: 'BrowseItems',
      component: BrowseItems
    }
  ]
})

export default router
