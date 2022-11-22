<template>
  <div>
    {{ comment.moviename }} | {{ comment.movie }} | {{ comment.score }} {{ comment.content }} - {{ comment.username }}
    <!-- <button @click="getUserComment"></button> -->
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'UserCommentItem',
  props: {
    comment: Object,
  },
  data() {
    return {
    }
  },
  computed: {
    username() {
      // console.log(this.$store.state.username)
      return this.$store.state.username
    },
  },
    
  methods:{
    getComments(){
      this.$state.dispatch('get_user_comments')
    },
  },
  created(){
    this.getComments()
  }
}

</script>

<style>

</style>