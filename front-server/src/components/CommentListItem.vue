<template>
  <div>
    <li>
      <!-- 댓글 수정 중 -->
      <div v-if="isEditing">
        <input 
        type="text" 
        id="comment"
        v-model.trim="commentContent">
        <button type="submit" class="btn btn-primary" @click="updateComment">수정</button>
      </div>
      <div v-else>

        <span>{{ comment.username }} - {{ comment.content }}</span>
        <button type="submit" class="btn btn-primary" @click="deleteComment">X</button>
        <button type="submit" class="btn btn-primary" @click="SwitchIsEditing">수정</button>
      </div>
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
  data() {
    return {
      isEditing: false,
      commentContent: this.comment.content,
      commentUser: this.comment.username,
      currentUser: this.$store.state.username
    }
  },
  methods: {
    SwitchIsEditing() {
      if (this.currentUser === this.commentUser) {
        this.isEditing = !this.isEditing
      } else {
        alert('본인만 수정 가능합니다!')
      }
      // this.isEditing = !this.isEditing
    },
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
        alert('본인만 삭제 가능합니다!')
      })
    },
    updateComment() {
      const movie_id = this.$route.params.id
      const comment_id = this.comment.id
      const content = this.commentContent

      axios({
        method: 'put',
        url: `${API_URL}/api/v1/movies/comments/${comment_id}/`,
        data: {
          content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.isEditing = !this.isEditing
        this.$store.commit('GET_COMMENTS', movie_id)
      })
      .catch((err) => {
        console.log(err)
        // alert('본인만 수정가능합니다!')
      })
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