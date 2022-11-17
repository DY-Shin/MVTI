Skip to content
GitLab

메뉴
 
도움말
박정은
P
pjt
프로젝트 정보
저장소
이슈0
머지 리퀘스트(MR)0
CI/CD
보안 및 준수 사항
Deployments
패키지 & 레지스트리
Infrastructure
Monitor
분석
위키
스니펫
설정
박정은
pjt

Auto DevOps
애플리케이션의 빌드, 테스트, 배포가 사전에 정의된 CI/CD 설정에 따라 자동으로 수행됩니다.

더 알아보기 Auto DevOps 문서


master
pjt
front-server
src
components
MovieList.vue
 
 
 
사용자 아바타
background
Dongyoon Shin authored 1분 전
0bd6a81a
MovieList.vue
3.08 KiB
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
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