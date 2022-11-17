<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-dark">
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{ name: 'MovieView' }">
          <img src="@/assets/MVTI.png" alt="#" width="100px">
        </router-link>
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link :to="{ name: 'MovieView' }">Movies</router-link>
          </li>
          <template v-if="isUserLogin">
            <li class="nav-item">
              <span class="username">Hello, </span>
                <router-link :to="{ name: 'ProfileView', params: { username: username } }">
                  {{ $store.state.username }}
              </router-link>
            </li>
              <br>
              <button class="btn btn-dark" @click="logoutUser">LogOut</button>
          </template>
          <template v-else>
            <li class="nav-item">
              <router-link :to="{ name: 'LoginView' }">LoginPage</router-link>
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'SignupView' }">SignUpPage</router-link>
            </li>
          </template>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  data() {
    return {
    }
  },
  computed: {
    username() {
      return this.$store.state.username
    },
    isUserLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logoutUser() {
      this.$store.commit('LOGOUT')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.nav-item {
  margin: 7px;
}
</style>
