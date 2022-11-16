<template>
  <div class="justify-content-center mt-2">
    <h1>Detail</h1>
    <div class="card mt-3" style="width: 30rem; margin: 0 auto;">
      <img :src="movieImgUrl" alt="movie_img">
      <div class="card-body">
        <p class="card-title">제목 : {{ movie?.title }}</p>
        <p>평점 : {{ movie?.vote_avg }}</p>
        <p>개봉일 : {{ movie?.released_date }}</p>
        <p>내용 : {{ movie?.overview }}</p>
      </div>
    </div> 
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"
// const body = document.querySelector("body")

export default {
  name: 'DetailView',
  data() {
    return{
      movie: null,
      movieImgUrl: null,
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
  /* body {
    background-image: url('@/assets/logo.png');
  } */
</style>