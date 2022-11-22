<template>
  <div class="carousel-item active">
    <img :src="imgUrl" class="d-block w-100" alt="...">
    <div class="carousel-caption d-none d-md-block">
      <h5>{{this.movie.title}}</h5>
      <p>내용</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'CarouselItem',
  props: {
    movie: Object,
  },
  data() {
    return{
      imgUrl: null,
    }
  },
  created() {
    this.getMovieUrl()
  },
  methods: {
    getMovieUrl() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.movie.id}/`,
      })
        .then((res) => {
          this.imgUrl = `https://image.tmdb.org/t/p/original${res.data.backdrop_path}`
          // console.log(this.imgUrl)
        })
        .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>