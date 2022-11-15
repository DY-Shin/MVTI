<template>
  <div class="movie-list text-center">
    <h3>Movie List</h3>
    <hr>
    <MovieListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'
export default {
  name: 'movieList',
  components: {
    MovieListItem,
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  }
}
</script>

<style>
.movie-list {
  text-align: start;
}
</style>
