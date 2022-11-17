<template>
  <div>
    <h3>Comment List</h3>
    <CommentForm/>

  </div>
</template>

<script>
import CommentForm from '@/components/CommentForm.vue'

export default {
  name: 'CommentList',
  components: {
    CommentForm
  },
}
</script>

<style>

</style>