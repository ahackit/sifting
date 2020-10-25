<template>
  <div class="flex flex-col rounded-lg shadow-lg overflow-hidden">
    <nuxt-link to="/recipes/1" class="block">
      <div class="flex-shrink-0">
        <img :src="recipe.main_image_url" class="h-48 w-full object-cover" />
      </div>
      <div class="flex-1 bg-white p-6 flex flex-col justify-between">
        <div class="flex-1">
          <h3 class="mt-2 text-xl leading-7 font-semibold text-gray-900">
            {{ recipe.title }}
          </h3>
          <p class="mt-3 text-base leading-6 text-gray-500">
            {{ recipe.description }}
          </p>
        </div>
      </div>
    </nuxt-link>
  </div>
</template>

<script>
export default {
  name: 'RecipeCard',
  props: ['recipe']
}
</script>

<style></style>
