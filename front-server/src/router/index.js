import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/movies/MovieView'
import DetailView from '@/views/movies/DetailView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
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
