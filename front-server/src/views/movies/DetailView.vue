<template>
  <div 
    :style="{ backgroundImage : `url(${backImgUrl})`}"
    style="background-size: cover; overflow: auto; background-attachment: fixed;"
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
        <div id="actorCard" class="text-align-center mt-3">
          <br>
          <h5><b>출연진</b></h5>
          <hr>
          <swiper 
            ref="filterSwiper" 
            :options="swiperOption" 
            role="tablist"
          >
            <ActorsList
              v-for="(actor, idx) in actorsData"
              :key="idx"
              :actor="actor"
            />
            <div class="swiper-button-prev" slot="button-prev"></div>
            <div class="swiper-button-next" slot="button-next"></div>
          </swiper>
        </div>
      </div>
    </div>
    <template v-if="isLogin">
      <div id="comment" style="width: 30rem; margin: 0 auto; background-color: black; color: white; justify-content-center" class="mt-5">
        <CommentList/>
      </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '@/components/CommentList.vue'
import ActorsList from '@/components/ActorsList.vue'
import { swiper } from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.min.css'

const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'DetailView',
  components: {
    CommentList,
    ActorsList,
    swiper,
  },
  data() {
    return{
      movie: null,
      movieImgUrl: null,
      backImgUrl: null,
      videoUrl: null,
      actorsData: null,
      swiperOption: {
        slidesPerView: 7,
        slidesPerGroup: 3,
        spaceBetween: 6, // swiper-slide 사이의 간격 지정
        slidesOffsetBefore: 0, // slidesOffsetBefore는 첫번째 슬라이드의 시작점에 대한 변경할 때 사용
        slidesOffsetAfter: 0, // slidesOffsetAfter는 마지막 슬라이드 시작점 + 마지막 슬라이드 너비에 해당하는 위치의 변경이 필요할 때 사용
        freeMode: true, // freeMode를 사용시 스크롤하는 느낌으로 구현 가능
        centerInsufficientSlides: true, // 컨텐츠의 수량에 따라 중앙정렬 여부를 결정함
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      },
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
        this.backImgUrl = `https://image.tmdb.org/t/p/original${this.movie?.backdrop_path}`
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
  #actorCard{
    background-color: rgba( 255, 255, 255, 0.7 );
    color: black;
  }
</style>

<style lang="scss" scoped>
  .swiper-container {
    .swiper-wrapper {
      .swiper-slide {
        width: 'auto'; // auto 값을 지정해야 슬라이드의 width값이 텍스트 길이 기준으로 바뀜
        min-width: 56px; // min-width를 지정하지 않을 경우 텍스트가 1개 내지는 2개가 들어갈 때 탭 모양이 상이할 수 있으므로 넣어준다.
        padding: 0px;
        font-size: 14px;
        line-height: 36px;
        text-align: center;
        color: #84868c;
        border: 0;
        border-radius: 18px;
        // background: #f3f4f7;
        appearance: none;
        // cursor: pointer;
      }
    }
  }
</style>
