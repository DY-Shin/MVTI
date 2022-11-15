<template>
  <div>
    <h1>Movie Page</h1>
    <hr>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
  computed:{
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies(){
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>

</style>
