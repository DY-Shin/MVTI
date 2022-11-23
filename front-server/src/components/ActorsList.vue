<template>
  <swiper-slide role="tab" id="card">
    <img :src="actorImg" alt="img" style="width: 50px;" class="mt-3">
    <p>{{ actor.actor }}</p>
  </swiper-slide>
</template>

<script>
import { swiperSlide } from 'vue-awesome-swiper'

export default {
  name: 'ActorsList',
  props: {
    actor: Object,
  },
  components: {
    swiperSlide,
  },
  data() {
    return {
      actorImg: `https://image.tmdb.org/t/p/w500/${this.actor.actor_path}`, 
    }
  }
}
</script>

<style>
  /* #actor{
    border: 1px solid black;
    margin: 0 auto
  } */
  #card {
    /* background-color: rgba( 255, 255, 255, 0.7 ); */
    color: black;
  }
</style>