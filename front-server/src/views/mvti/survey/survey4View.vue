<template>
  <div>
    <div>
      <p>콧구멍에 치아가 나면?</p>
    </div>
    <div class="d-flex justify-content-center">
      <div>
        <p @click="toGroup3">치과가기</p>
      </div>
      <div>
        <p>vs</p>
      </div>
      <div>
        <p @click="toGroup4">이비인후과 가기</p>
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
      this.$router.push({name: 'survey5'})
    }
    ,
    toGroup4() {
      this.$store.commit('TOGROUP4')
      this.$router.push({name: 'survey5'})
    }
  }
}
</script>

<style>

</style>