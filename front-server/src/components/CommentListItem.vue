<template>
  <div>
    <li>
      <span>{{ comment.username }} - {{ comment.content }}</span>
      <button type="submit" class="btn btn-primary" @click="deleteComment">삭제</button>
      <button type="submit" class="btn btn-primary" @click="updateComment">수정</button>
      
    </li>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  },
  methods: {
    deleteComment() {
      const movie_id = this.$route.params.id
      const comment_id = this.comment.id

      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/movies/comments/${comment_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.$store.commit('GET_COMMENTS', movie_id)
      })
      .catch((err) => {
        console.log(err)
        // alert('본인만 삭제가능합니다!')
      })
    },
    updateComment() {
      
    }
  }
  // computed: {
  //   comment() {
  //     return this.$store.state.comments
  //   }
  // }
}
</script>

<style>

</style>