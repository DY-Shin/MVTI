<template>
  <div>
    <div>
      <p>밸런스 게임!</p>
    </div>
    <div class="d-flex justify-content-center">
      <div>
        <p @click="toGroup3">평생 여름</p>
      </div>
      <div>
        <p>vs</p>
      </div>
      <div>
        <p @click="toGroup4">평생 겨울</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup3() {
      this.$store.commit('TOGROUP3')
      this.$router.push({name: 'survey7'})
    }
    ,
    toGroup4() {
      this.$store.commit('TOGROUP4')
      this.$router.push({name: 'survey7'})
    }
  }
}
</script>

<style>

</style>