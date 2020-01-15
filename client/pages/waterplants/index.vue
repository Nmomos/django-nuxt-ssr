<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>育てた水草一覧</h3>
          <nuxt-link to="/waterplants/add" class="btn btn-info">
            水草を追加する
          </nuxt-link>
        </div>
      </div>
      <template v-for="waterplant in waterplants">
        <div :key="waterplant.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <water-plant-card :onDelete="deleteWaterPlant" :waterplant="waterplant" />
        </div>
      </template>
    </div>
  </main>
</template>
<script>

import WaterPlantCard from '~/components/WaterPlantCard.vue'

export default {
  head () {
    return {
      title: '水草一覧'
    }
  },
  components: {
    WaterPlantCard
  },
  data () {
    return {
      waterplants: []
    }
  },
  async asyncData ({ $axios, params }) {
    try {
      const waterplants = await $axios.$get(`/waterplants/`)
      return { waterplants }
    } catch (e) {
      return { waterplants: [] }
    }
  },
  methods: {
    async deleteWaterPlant (waterplant_id) { // eslint-disable-line
      try {
        await this.$axios.$delete(`/waterplants/${waterplant_id}/`) // eslint-disable-line
        const newWaterPlants = await this.$axios.$get('/waterplants/')
        this.waterplants = newWaterPlants
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
<style scoped>
</style>
