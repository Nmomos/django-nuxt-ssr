<template>
  <div class="card water-plant-card">
    <img :src="waterplant.picture" class="card-img-top">
    <div class="card-body">
      <h5 class="card-title">
        {{ waterplant.name }}
      </h5>
      <p class="card-text">
        <strong>配置場所:</strong> {{ waterplant.position }}
      </p>
      <div class="action-buttons">
        <nuxt-link :to="`/waterplants/${waterplant.id}/`" class="btn btn-sm btn-success">
          詳細
        </nuxt-link>
        <nuxt-link :to="`/waterplants/${waterplant.id}/edit/`" class="btn btn-sm btn-primary">
          編集
        </nuxt-link>
        <button @click="onDelete(waterplant.id)" class="btn btn-sm btn-danger">
          削除
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ['waterplant', 'onDelete']
}
</script>
<style>
.water-plant-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
</style>
