import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  state: {
    movies: [],
    token: null,
    username: null,
  },
  plugins: [
    createPersistedState
  ],
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies){
      state.movies = movies
    },

    SAVE_TOKEN(state, payload1) {
      state.token = payload1.token
      state.username = payload1.username
      // router.push({name: 'MovieView' })
      // console.log(payload1.username)
    },


    LOGOUT(state){
      state.token = !state.token
      router.push({name: 'LoginView'})
    }

    // SAVE_USERNAME(state, payload) {
    //   // state.token = token
    //   state.username = payload.username
    //   router.push({name: 'MovieView' })
    // },

  },
  actions: {
    getMovies(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
        .then(res=> {
          console.log(res, context)
          context.commit('GET_MOVIES', res.data)
        })
        .catch(err => console.log(err))
    },


    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          email: payload.email,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          // const payload1 = {
          //   token : res.data.key,
          //   username : payload.username
          // }
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => console.log(err))
      },

    logIn(context, payload) {
      // if (!payload) {
      //   alert('다시 시도해주세요!')
      // }
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
      .then((res) => {
        // console.log(res)
        const payload1 = {
          token : res.data.key,
          username : payload.username
        }
        context.commit('SAVE_TOKEN', payload1)
      })
      .catch((err) => {
        console.log(err)
        // alert('다시 시도해주세요!')
      })
    },
  },
  modules: {
  }
})
