<template>
  <div>
    <p>{{ username }}님, 평점을 남겨보세요!</p>
    <div>
      <input 
        type="text" 
        id="comment"
        v-model.trim="commentContent"
        @keyup.enter="createComment">
      <!-- <button type="submit" class="btn btn-primary">Submit</button> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'CommentForm',
  data() {
    return {
      commentContent: null,
    }
  },
  computed: {
    username() {
      return this.$store.state.username
    },
  },
  methods: {
    createComment() {
      const content = this.commentContent
      if (!content) {
        alert('내용을 입력해주세요')
        // return
        // console.log()
      } else {
        axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/comments/`,
        data: {
          content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // console.log(res)
        const commentItem = {
          content
        }
        this.$store.commit('CREATE_COMMENT', commentItem)
      })
      .catch((err) => {
        console.log(err)
      })
        
      }
      this.commentContent = null
      // console.log(this.$route.params)

      
    }
  }
}
</script>

<style>

</style>