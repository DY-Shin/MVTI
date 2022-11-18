<template>
  <div id="profile">
    <h3>{{ username }}님의 프로필</h3>
    <h5>{{ username }}님이 좋아한 영화</h5>
    <h5>{{ username }}님이 남긴 리뷰</h5>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'ProfileView',
  // props: {
  //   username: Object,
  // },
  computed: {
    username() {
      return this.$store.state.username
    },
  },
  data: function () {
    return {}
  },
  methods: {
    signup: function () {     
    }
  }
}
</script>

<style>
  #profile{
    color: white;
  }
</style>