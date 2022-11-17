<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
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


    // logIn() {
    //   const username = this.username
    //   const password = this.password

    //   const payload = {
    //     username,
    //     password
    //   }
    //   .then(() => {
    //   this.$store.dispatch('logIn', payload)
    //   router.push({name: 'MovieView' })
    //   })
    //   .catch(err =>
    //     this.error = err.response.data.error)
    //     alert('다시 시도해보세요.')
    // },

    // async logIn() {
    //   try {
    //     const userData = {
    //       username: this.username,
    //       password: this.password,
    //     }
    //     this.$store.dispatch('logIn', userData)
    //     router.push({name: 'MovieView' })
    //   } catch (err) {
    //     console.log(err.response.data)
    //     alert ('다시 시도해주세요') }
      // } finally {
      //   this.initForm()
      // }
    // },
    // initForm() {
    //   this.username = '',
    //   this.password = '',
    // },
  }
}
</script>
