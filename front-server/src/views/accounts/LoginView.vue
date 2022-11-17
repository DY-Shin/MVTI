<template>
  <div>
    <h1>Log In</h1>
    <form @submit.prevent="logIn">
      <div class="col-4">

        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input type="text" class="form-control" id="username" v-model="username" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input type="password" class="form-control" id="password" v-model="password">
        </div>
        <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div>
        <button type="submit" class="btn btn-primary">LogIn</button>
      </div>
    </form>
  </div>
</template>

<script>
// import router from '@/router'
// import validateEmail from ''

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
      error: null,
    }
  },
  methods: {

    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username,
        password
      }
      this.$store.dispatch('logIn', payload)
      // router.push({name: 'MovieView' })
    },
  }
}
</script>

<style>
form {
  /* width: 500px; */
  display: flex;
  justify-content: center;
  text-align: start;
}
</style>