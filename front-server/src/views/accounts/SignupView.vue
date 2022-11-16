<template>
  <div>
    <h1>Sign Up</h1>
    <form @submit.prevent="signup">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'SingupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signup() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username,
        password1,
        password2
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>