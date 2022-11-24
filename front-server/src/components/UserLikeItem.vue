<template>
  <div>
    <router-link :to="{
                    name: 'DetailView',
                    params: { id: movie.id }
                  }">
      <div id="card">
          <img :src="imgUrl" alt="img">
          <div id="card-body">
            <!-- <h5>{{ movie.id }}</h5> -->
            <h4>{{ movie.title }}</h4>
          </div>
      </div>
    </router-link>
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'UserLikeItem',
  props: {
    movie: Object
  },
  data() {
    return{
      imgUrl: `https://themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`,
    }
  },
  methods: {
    getLike() {
      this.$store.dispatch('getlike')
    }
  },
  created() {
    this.getLike()
  }
}
</script>

<style>
#card {
  color: white;
  text-decoration: none !important;
}
</style>