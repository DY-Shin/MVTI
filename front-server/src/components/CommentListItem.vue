<template>
  <div>
    <li>
      <span>{{ comment.username }} - {{ comment.content }}</span>
        
    </li>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
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