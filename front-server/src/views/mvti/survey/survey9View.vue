<template>
  <div>
    <div>
      <p>밸런스 게임!</p>
    </div>
    <div class="d-flex justify-content-center">
      <div>
        <p @click="toGroup5">손톱 옆 거스름 뜯다가 찢김</p>
      </div>
      <div>
        <p>vs</p>
      </div>
      <div>
        <p @click="toGroup6">음식 먹다가 혀 깨물음</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup5() {
      this.$store.commit('TOGROUP5')
      this.$store.dispatch('get_result')
      this.$router.push({name: 'MvtiResult'})
    },
    toGroup6() {
      this.$store.commit('TOGROUP6')
      this.$store.dispatch('get_result')
      this.$router.push({name: 'MvtiResult'})
    }
  }
}
</script>

<style>

</style>