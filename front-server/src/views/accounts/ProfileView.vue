<template>
  <div id="profile">
    <h3>{{ username }}님의 프로필</h3>
    <div class="fw-bold text-end text-white">
        <!-- <h4>코멘트 {{ profile.comments.length }}개</h4> -->
        <!-- <h4>찜한 영화 {{ profile.pick_movies.length }}개</h4> -->
        <!-- <h4>좋아요한 영화 {{ profile.like_movies.length }}개</h4> -->
    </div>
    <h5>{{ username }}님이 좋아한 영화</h5>
    <div>
      <h5>{{ username }}님이 남긴 리뷰</h5>
      <UserComment/>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import UserComment from '@/components/UserComment'
// const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'ProfileView',
  components: {
    UserComment
  },
  computed: {
    username() {
      return this.$store.state.username
    },
  },
  data: function () {
    return {
      comment: null,
    }
  },
  methods: {
    // getUserComments(){
    //     axios({
    //       method: 'get',
    //       url: `${API_URL}/api/v1/comments/`,
    //     })
    //     .then((res) => {
    //       console.log(res)
    //       this.comment = res.data
    //     })
    //     .catch(err => console.log(err))
    //   },

    // GoActions() {
    //   this.$store.dispatch('get_user_comments')

    // }
  },
  
  // created() {
  //   axios({
  //     method: 'get',
  //     url: `${API_URL}/accounts/user/${this.username}`
  //   })
  //     .then(res => {
  //       this.profile = res.data
  //     })
  //     .catch(err => console.error(err))
  // },
}
</script>

<style>
  #profile{
    color: white;
  }
</style>