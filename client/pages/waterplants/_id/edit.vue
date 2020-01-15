<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">
          {{ waterplant.name }}
        </h2>
      </div>
      <div class="col-md-6 mb-4">
        <img v-if="!preview" :src="waterplant.picture" class="img-fluid" style="width: 400px border-radius: 10px box-shadow: 0 1rem 1rem rgba(0,0,0,.7)">
        <img v-else :src="preview" class="img-fluid" style="width: 400px border-radius: 10px box-shadow: 0 1rem 1rem rgba(0,0,0,.7)">
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitWaterPlant">
          <div class="form-group">
            <label for>水草の名称</label>
            <input v-model="waterplant.name" type="text" class="form-control">
          </div>
          <div class="form-group">
            <label for>植える位置</label>
            <input v-model="waterplant.position" type="text" class="form-control" name="Positions">
          </div>
          <div class="form-group">
            <label for>水草の写真</label>
            <input @change="onFileChange" type="file">
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>
                  育成難易度
                </label>
                <select v-model="waterplant.difficulty" class="form-control">
                  <option value="Easy">
                    Easy
                  </option>
                  <option value="Medium">
                    Medium
                  </option>
                  <option value="Hard">
                    Hard
                  </option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for>二酸化炭素添加量</label>
                <select v-model="waterplant.addition_amount" class="form-control">
                  <option value="Low">
                    Low
                  </option>
                  <option value="Middle">
                    Middle
                  </option>
                  <option value="High">
                    High
                  </option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for>葉長<small>(mm))</small></label>
                <input v-model="waterplant.leaf_length" type="text" class="form-control" name="Positions">
              </div>
            </div>
          </div>
          <div class="form-group mb-3">
            <label for>水質</label>
            <input v-model="waterplant.water_quality" type="text" class="form-control" name="Positions">
          </div>
          <button type="submit" class="btn btn-success">
            更新
          </button>
        </form>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head () {
    return {
      title: '水草編集ページ'
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
      },
      preview: ''
    }
  },
  async asyncData ({ $axios, params }) {
    try {
      const waterplant = await $axios.$get(`/waterplants/${params.id}`)
      return { waterplant }
    } catch (e) {
      return { waterplant: [] }
    }
  },
  methods: {
    onFileChange (e) {
      const files = e.target.files || e.dataTransfer.files
      if (!files.length) {
        return
      }
      this.waterplant.picture = files[0]
      this.createImage(files[0])
    },
    createImage (file) {
      const reader = new FileReader()
      const vm = this
      reader.onload = (e) => {
        vm.preview = e.target.result
      }
      reader.readAsDataURL(file)
    },
    async submitWaterPlant () {
      const editedWaterPlant = this.waterplant
      if (editedWaterPlant.picture.includes('http://') !== -1) {
        delete editedWaterPlant.picture
      }
      const config = {
        headers: { 'content-type': 'multipart/form-data' }
      }
      const formData = new FormData()
      for (const data in editedWaterPlant) {
        formData.append(data, editedWaterPlant[data])
      }
      try {
        const response = await this.$axios.$patch(`/waterplants/${editedWaterPlant.id}/`, formData, config)
        this.$router.push('/waterplants/')
        console.log(response)
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>

<style>
</style>
