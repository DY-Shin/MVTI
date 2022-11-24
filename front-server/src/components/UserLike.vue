<template>
  <div class="d-flex justify-content-center">
    <UserLikeItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
    <!-- <UserLikeItem/> -->
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = "http://127.0.0.1:8000"
import UserLikeItem from '@/components/UserLikeItem.vue'

export default {
  name: 'UserLike',
  components: {
    UserLikeItem
  },
  computed: {
    movies() {
      return this.$store.state.likemovie
    }
  },
  methods: {
    // getlike() {
    //   const movie_id = this.$route.params.id

    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/movies/${this.$route.params.id}/like/${this.$store.state.userpk}/`,
    //     data: {
    //       movie_id
    //     },
    //     headers: {
    //       Authorization: `Token ${this.$store.state.token}`
    //     }
    //   })
    //     .then((res) => {
    //       this.isLike = res.data
    //       console.log(this.isLike);
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
      
    // }
  }
}
</script>

<style>

</style>