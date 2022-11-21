<template>
  <div>
    <li>
      <!-- 댓글 수정 중 -->
      <div v-if="isEditing">
        <input 
        type="text" 
        id="comment"
        v-model.trim="commentContent">
        <div style="background:#000;padding-bottom:10px;">
    
          <star-rating :glow="10" :rounded-corners="true" v-model="movieScore1" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"></star-rating>
        </div>
        <button type="submit" class="btn btn-primary" @click="updateComment">수정</button>
      </div>
      <!-- 수정 X -->
      <div v-else>
        <span>{{ comment.content }}</span>
        <span>{{ comment.score }}</span>
        <b>{{ comment.username }}</b>
        <button type="submit" class="btn btn-primary" @click="deleteComment">X</button>
        <button type="submit" class="btn btn-primary" @click="SwitchIsEditing">수정</button>
      </div>
    </li>
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  },
  components: {
    StarRating
  },
  data() {
    return {
      isEditing: false,
      commentContent: this.comment.content,
      movieScore1: this.comment.score,
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
      .then(() => {
        // console.log(res)
        this.$store.commit('get_comments', movie_id)
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
      const score = this.movieScore1

      axios({
        method: 'put',
        url: `${API_URL}/api/v1/movies/comments/${comment_id}/`,
        data: {
          content,
          score
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