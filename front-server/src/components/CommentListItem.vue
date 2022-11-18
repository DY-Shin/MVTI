<template>
  <div>
    <li>
      {{ comment }}
    </li>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: String,
  }
  // computed: {
  //   comment() {
  //     return this.$store.state.comments
  //   }
  // }
}
</script>

<style>

</style>