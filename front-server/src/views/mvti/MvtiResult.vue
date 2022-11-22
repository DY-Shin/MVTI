<template>
  <div>
    <h3>축하드립니다! {{ name }} 유형이시군요!</h3>
    <span>{{ username }}님, 이런 영화는 어떠세요?</span>
    <!-- 영화 목록 좌르륵 -->

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'MvtiResult',
  data() {
    return {
      name: null,
      genre1: null,
      genre2: null,
      genre3: null,
      genre4: null,
      genre5: null
    }
  },
  computed: {
    username() {
      return this.$store.state.username
    },
    mvti_pk() {
      return this.$store.state.resultmvti
    }
  },
  methods: {
    get_mvti() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/mvti/${this.mvti_pk}`
      })
      .then((res) => {
        this.name = res.data.name
        this.genre1 = res.data.genre1
        this.genre2 = res.data.genre2
        this.genre3 = res.data.genre3
        this.genre4 = res.data.genre4
        this.genre5 = res.data.genre5
      })
      .catch((err) => console.log(err))
    },
  },
  created() {
    this.get_mvti()
  }
  
}
</script>

<style>

</style>