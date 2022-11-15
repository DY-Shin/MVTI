import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '@/views/accounts/SignupView'
import LoginView from '@/views/accounts/LoginView'


Vue.use(VueRouter)

const routes = [

  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView,
  },

  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
