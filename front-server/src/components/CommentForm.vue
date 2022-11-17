<template>
  <div>
    <p>{{ username }}님, 평점을 남겨보세요!</p>
    <form @submit.prevent="createComment">
      <input type="text" id="comment">
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'CommentForm',
  computed: {
    username() {
      return this.$store.state.username
    },
  },
  methods: {
    createComment() {
      this.$store.dispatch('createComment')
    }
  }
}
</script>

<style>

</style>