<template>
  <div>
    <h1>Sign Up</h1>
    <form @submit.prevent="signup">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <div>

        <label for="email">email : </label>
        <input type="text" id="email" v-model="email"><br>
        <p class="validation-text">
              <!-- 이메일 형식 및 입력란 공백 확인 -->
          <span class="warning" v-if="!isUsernameValid && username">
            Please enter an email address
          </span>
        </p>
      </div>
      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
import router from '@/router'
// import axios from 'axios'

export default {
  name: 'SingupView',
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signup() {
      const username = this.username
      const email = this.email
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username,
        email,
        password1,
        password2
      }
      this.$store.dispatch('signUp', payload)
      router.push({name: 'LoginView' })
    }
  }
}
</script>