<template>
  <div>
    <div>
      <p>밸런스 게임!</p>
    </div>
    <div class="d-flex justify-content-center">
      <div>
        <p @click="toGroup1">털 엄청 많기</p>
      </div>
      <div>
        <p>vs</p>
      </div>
      <div>
        <p @click="toGroup2">털 하나도 없기</p>
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
      this.$router.push({name: 'survey2'})
    },
    toGroup2() {
      this.$store.commit('TOGROUP2')
      this.$router.push({name: 'survey2'})
    }
  }
}
</script>

<style>

</style>