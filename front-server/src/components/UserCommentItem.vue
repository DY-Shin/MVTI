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
      // isEditing: false,
      // commentContent: this.comment.content,
      
      // movieScore1: this.comment.score,
      // commentUser: this.comment.username,
    }
  },
  computed: {
    username() {
      // console.log(this.$store.state.username)
      return this.$store.state.username
    },
  },
    
  methods:{
    // getArticles(){
    //     this.$store.state.comments.forEach(comment => {
    //       if (this.currentUser === this.commentUser){
    //         // console.log(article)
    //         this.comments.push(comment)
    //       }
    //     })
    //   },

  //   getComments(){
  //     const commentUser = this.comment.username
  //     this.$store.state.comments.forEach(comment => {
  //     if (this.username === commentUser){
  //       this.$store.commit('GET_USER_COMMENTS', comment)
  //     }
  //   })
  // },
  // created(){
  //   this.getComments()
  // }
  
  }
}

</script>

<style>

</style>