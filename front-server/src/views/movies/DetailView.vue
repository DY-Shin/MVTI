<template>
  <div 
    :style="{ backgroundImage : `url(${backImgUrl})`}"
    style="background-size: cover; height: 100vh; width: 99.1vw; overflow: auto;"
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
            <h5 class="card-header"><b>{{ movie?.title }}</b></h5>
            <p>평점 : {{ movie?.vote_avg }}</p>
            <p>개봉일 : {{ movie?.released_date }}</p>
            <p>내용 : {{ movie?.overview }}</p>
            <iframe :src="videoUrl" frameborder="0" width="500" height="300"></iframe>
          </div>
        </div>
        <div id="actors" class="d-flex justify-content-start">
          <ActorsList
            v-for="(actor, idx) in actorsData"
            :key="idx"
            :actor="actor"
          />
          <!-- <p>{{ actorsData }}</p> -->
        </div>
      </div>
    </div>
    <template v-if="isLogin">
      <div id="comment" style="width: 30rem; margin: auto;" class="mt-5">
        <CommentList/>
      </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '@/components/CommentList.vue'
import ActorsList from '@/components/ActorsList.vue'

const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'DetailView',
  components: {
    CommentList,
    ActorsList,
  },
  data() {
    return{
      movie: null,
      movieImgUrl: null,
      backImgUrl: null,
      videoUrl: null,
      actorsData: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getMovieDetail()
    this.getComments()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/`,
      })
      .then((res) => {
        // console.log(res)
        this.movie = res.data
        this.movieImgUrl = `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.movie?.poster_path}`
        this.backImgUrl = `https://image.tmdb.org/t/p/original${this.movie?.backdrop_path}`\
        this.videoUrl = `https://www.youtube.com/embed/${this.movie?.youtube_url}`
        this.actorsData = this.movie?.actors_data
        // console.log(this.actorsData)
      })
      .catch(err => console.log(err))
    },

    // 영화에 달린 코멘트 가져오기
    getComments(){
      const movieId = this.$route.params.id

      this.$store.dispatch('get_comments', movieId)
    }
  }
}
</script>

<style>
  #body {
    background-color: rgba( 255, 255, 255, 0.7 );
    color: black;
    background-size: cover;
  }
  #comment {
    background-color: white;
  }
  #actors{
    background-color: white;
  }
</style>
