<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">
          {{ waterplant.name }}
        </h2>
      </div>
      <div class="col-md-6 mb-4">
        <img
          :src="waterplant.picture"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          alt
        >
      </div>
      <div class="col-md-6">
        <div class="waterplant-details">
          <h4>植える位置</h4>
          <p>{{ waterplant.position }}</p>
          <h4>育成難易度</h4>
          <p>{{ waterplant.difficulty }}</p>
          <h4>二酸化炭素添加量</h4>
          <p>{{ waterplant.addition_amount }}</p>
          <h4>葉長</h4>
          <p>{{ waterplant.leaf_length }} mm</p>
          <h4>水質</h4>
          <p>{{ waterplant.water_quality }}</p>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head () {
    return {
      title: '水草詳細ページ'
    }
  },
  data () {
    return {
      waterplant: {
        name: '',
        position: '',
        picture: '',
        difficulty: '',
        addition_amount: '',
        leaf_length: '',
        water_quality: ''
      }
    }
  },
  async asyncData ({ $axios, params }) {
    try {
      const waterplant = await $axios.$get(`/waterplants/${params.id}`)
      return { waterplant }
    } catch (e) {
      return { waterplant: [] }
    }
  }
}
</script>
<style scoped>
</style>
