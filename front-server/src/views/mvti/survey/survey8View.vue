<template>
  <div>
    <div>
      <p>밸런스 게임!</p>
    </div>
    <div class="d-flex justify-content-center">
      <div>
        <p @click="toGroup5">50%확률로 10억받기</p>
      </div>
      <div>
        <p>vs</p>
      </div>
      <div>
        <p @click="toGroup6">그냥 500만원 받기</p>
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
      this.$router.push({name: 'survey9'})
    }
    ,
    toGroup6() {
      this.$store.commit('TOGROUP6')
      this.$router.push({name: 'survey9'})
    }
  }
}
</script>

<style>

</style>