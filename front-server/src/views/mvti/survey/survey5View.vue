<template>
  <div>
    <div>
      <p>밸런스 게임!</p>
    </div>
    <div class="d-flex justify-content-center">
      <div>
        <p @click="toGroup3">모든 팀원이 천재 나만 자괴감</p>
      </div>
      <div>
        <p>vs</p>
      </div>
      <div>
        <p @click="toGroup4">희망은 나뿐인 팀 소처럼 일하기</p>
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
      this.$router.push({name: 'survey6'})
    }
    ,
    toGroup4() {
      this.$store.commit('TOGROUP4')
      this.$router.push({name: 'survey6'})
    }
  }
}
</script>

<style>

</style>