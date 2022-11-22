<template>
  <div>
    <div>
      <p>여행을 간다면?</p>
    </div>
    <div class="d-flex justify-content-center">
      <div>
        <p @click="toGroup1">깊은 숲 속 오두막 혼자가기</p>
      </div>
      <div>
        <p>vs</p>
      </div>
      <div>
        <p @click="toGroup2">내가 주최한 30명 단체여행</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup1() {
      this.$store.commit('TOGROUP1')
      this.$router.push({name: 'survey4'})
    },
    toGroup2() {
      this.$store.commit('TOGROUP2')
      this.$router.push({name: 'survey4'})
    }
  }
}
</script>

<style>

</style>