<template>
  <div>
    <img :src="actorImg" alt="img" style="width: 50px;">
    <p>{{ actor.actor }}</p>
    <!-- <p>{{ actorImg }}</p> -->
  </div>
</template>

<script>


export default {
  name: 'ActorsList',
  props: {
    actor: Object,
  },
  data() {
    return {
      actorImg: `https://image.tmdb.org/t/p/w500/${this.actor.actor_path}`, 
    }
  }
}
</script>

<style>

</style>