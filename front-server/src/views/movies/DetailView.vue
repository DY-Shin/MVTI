<template>
  <div 
    :style="{ backgroundImage : `url(https://image.tmdb.org/t/p/original${this.movie?.backdrop_path})`}"
    style="background-size: cover; height: 100vh; width: 99.1vw;"
  >
    <div class="d-flex flex-row justify-content-evenly">
      <!-- <h1>Detail</h1> -->
      <div class="col-3">
        <div class="card mt-5" style="width: 20rem; margin: 0 auto;">
          <img :src="movieImgUrl" alt="movie_img">
        </div>
      </div>
      <div class="col-7">
        <div class="card mt-5" id="body">
          <div class="card-body">
            <h5 class="card-header">{{ movie?.title }}</h5>
            <p>평점 : {{ movie?.vote_avg }}</p>
            <p>개봉일 : {{ movie?.released_date }}</p>
            <p>내용 : {{ movie?.overview }}</p>
          </div>
        </div>
      </div>
    </div>
    <template v-if="isLogin">
      <div id="comment" style="width: 30rem; margin: auto;">
        <CommentList/>
      </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
// import CommentForm from '@/components/CommentForm.vue'
import CommentList from '@/components/CommentList.vue'
const API_URL = "http://127.0.0.1:8000"
// const body = document.querySelector("body")

export default {
  name: 'DetailView',
  components: {
    CommentList
  },
  data() {
    return{
      movie: null,
      movieImgUrl: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getMovieDetail()
    // const backImgUrl = `https://image.tmdb.org/t/p/original${this.movie?.backdrop_path}`

  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/`,
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
        this.movieImgUrl = `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.movie?.poster_path}`
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>
  #body {
    background-color: rgba( 255, 255, 255, 0.7 );
    color: black;
  }
  #comment {
    background-color: white;
  }
</style>