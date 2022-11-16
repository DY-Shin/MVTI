<template>
  <div id="app">
    <nav>
      <div>

        <router-link :to="{ name: 'MovieView' }">Movies</router-link>
      </div>
      <div class="navigations">
        <template v-if="isUserLogin">
          <span class="username">Hello, {{ $store.state.username }}</span>
          <router-link :to="{ name: 'ProfileView' }"> [Profile]</router-link>
          <br>
          <button @click="logoutUser">LogOut</button>
        </template>
        <template v-else>
          <router-link :to="{ name: 'SignupView' }">SignUpPage</router-link> |
          <router-link :to="{ name: 'LoginView' }">LoginPage</router-link> |
        </template>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  computed: {
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
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
