import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/movies/MovieView'
import DetailView from '@/views/movies/DetailView'
import SignupView from '@/views/accounts/SignupView'
import LoginView from '@/views/accounts/LoginView'
import ProfileView from '@/views/accounts/ProfileView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },

  
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

  {
    path: '/user/:username',
    name: 'ProfileView',
    component: ProfileView,
  },
  
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },

  ]
      
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router