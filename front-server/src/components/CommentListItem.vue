<template>
  <div>{{ comments.content }}</div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comments: Object,
  }
}
</script>

<style>

</style>