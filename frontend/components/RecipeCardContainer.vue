<template>
  <div
    class="relative bg-gray-50 pt-16 pb-20 px-4 sm:px-6 lg:pt-24 lg:pb-28 lg:px-8"
  >
    <div class="absolute inset-0">
      <div class="bg-white h-1/3 sm:h-2/3"></div>
    </div>
    <div class="relative max-w-7xl mx-auto">
      <div class="grid gap-5 max-w-lg mx-auto lg:grid-cols-3 lg:max-w-none">
        <RecipeCard></RecipeCard>
        <RecipeCard></RecipeCard>
        <RecipeCard></RecipeCard>
        <RecipeCard></RecipeCard>
        <RecipeCard></RecipeCard>
        <RecipeCard></RecipeCard>
        <RecipeCard></RecipeCard>
        <RecipeCard></RecipeCard>
        <RecipeCard></RecipeCard>
      </div>
    </div>
  </div>
</template>

<script>
import RecipeCard from './RecipeCard.vue'

export default {
  name: 'RecipeCardContainer',
  components: { RecipeCard }
}
</script>

<style></style>
