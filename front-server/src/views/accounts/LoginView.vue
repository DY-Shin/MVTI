<template>
  <div>
    <h1>Login</h1>
    <form>
      <label for="username">username : </label>
      <input type="text" id="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data: function() {
    return {

    }
  },
  methods: {
    login: function () {

    }
  }
}
</script>

<style>

</style>