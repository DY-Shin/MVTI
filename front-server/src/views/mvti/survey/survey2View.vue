<template>
  <div>
    <div>
      <p>밸런스 게임!</p>
    </div>
    <div class="d-flex justify-content-center">
      <div>
        <p @click="toGroup1">추성훈에게 맞고 이국종 교수에게 수술 받기</p>
      </div>
      <div>
        <p>vs</p>
      </div>
      <div>
        <p @click="toGroup2">이국종 교수에게 맞고 추성훈에게 수술받기</p>
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
      this.$router.push({name: 'survey3'})
    },
    toGroup2() {
      this.$store.commit('TOGROUP2')
      this.$router.push({name: 'survey3'})
    }
  }
}
</script>

<style>

</style>