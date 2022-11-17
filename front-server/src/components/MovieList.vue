<template>
  <div class="movie-list text-center">
    <h3>Movie List</h3>
    <hr>
    <swiper 
      ref="filterSwiper" 
      :options="swiperOption" 
      role="tablist"
    >
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'
import { swiper } from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.min.css'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    swiper,
  },
  data () {
    return {
      swiperOption: {
        slidesPerView: 'auto',
        slidesPerGroup: 4,
        spaceBetween: 6, // swiper-slide 사이의 간격 지정
        slidesOffsetBefore: 0, // slidesOffsetBefore는 첫번째 슬라이드의 시작점에 대한 변경할 때 사용
        slidesOffsetAfter: 0, // slidesOffsetAfter는 마지막 슬라이드 시작점 + 마지막 슬라이드 너비에 해당하는 위치의 변경이 필요할 때 사용
        freeMode: true, // freeMode를 사용시 스크롤하는 느낌으로 구현 가능
        centerInsufficientSlides: true, // 컨텐츠의 수량에 따라 중앙정렬 여부를 결정함
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      }
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  }
}
</script>

<style lang="scss" scoped>
.movie-list {
  text-align: start;
}
.swiper-container {
  padding: 0 20px; // 여백값을 지정할 경우 슬라이드의 시작점과 종점이 이에 영향을 받아 변경됨
  &:before,
  &:after { // 가상선택자를 활용하여 그라데이션 값 추가
    display: block;
    position: absolute;
    top: 0;
    width: 20px; // container에 준 여백값보다 크지 않게 사이즈 지정하기 (swiper-slide의 클릭 이벤트에 영향을 주지 않고, 이렇게 지정해야 그라데이션이 영역 내부에 있는 탭이 스크롤 하기 전엔 영향을 주지 않음)
    height: 100%;
    z-index: 10;
    content: "";
  }
  &:before {
    left: 0;
    background: linear-gradient(90deg, #fff -20.19%, rgba(255, 255, 255, 0.8) 18.31%, rgba(255, 255, 255, 0) 75%);
  }
  &:after {
    right: 0;
    background: linear-gradient(270deg, #fff -20.19%, rgba(255, 255, 255, 0.8) 18.31%, rgba(255, 255, 255, 0) 75%);
  }
  //...중략
  .swiper-wrapper {
    .swiper-slide {
      width: 350px; // auto 값을 지정해야 슬라이드의 width값이 텍스트 길이 기준으로 바뀜
      min-width: 56px; // min-width를 지정하지 않을 경우 텍스트가 1개 내지는 2개가 들어갈 때 탭 모양이 상이할 수 있으므로 넣어준다.
      padding: 0px 14px;
      font-size: 14px;
      line-height: 36px;
      text-align: center;
      color: #84868c;
      border: 0;
      border-radius: 18px;
      background: #f3f4f7;
      appearance: none;
      cursor: pointer;
    }
  }
}
</style>
