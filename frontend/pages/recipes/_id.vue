<template>
  <div class="grid grid-cols-1/3-2/3 border border-gray-200 p-4">
    <div class="border-r pr-4">
      <div class="flex-shrink-0">
        <img :src="recipe.main_image_url" class="h-48 w-full object-cover" />
      </div>
      <p class="font-bold">Details</p>
      <ul class="grid grid-cols-2 grid-rows-4 mb-4">
        <li>Cuisine: {{ recipe.cuisine }}</li>
        <li>Category: {{ recipe.dish_category }}</li>
        <li>Difficulty: {{ recipe.difficulty }}</li>
        <li>Subcategory: {{ recipe.dish_subcategory }}</li>
        <li>Prep Time: {{ recipe.prep_time }}</li>
        <li>Servings: {{ recipe.servings }}</li>
        <li>Total Time: {{ recipe.total_time }}</li>
        <li>Calories/Serving: {{ recipe.calories_per_serving }}</li>
      </ul>
      <p class="font-bold">Cookware</p>
      <ul class="grid grid-cols-2 grid-rows-4 mb-4">
        <li v-for="ware in recipe.cookware" :key="ware">{{ ware }}</li>
      </ul>
      <p class="font-bold">Ingredients</p>
      <ul class="grid grid-cols-2 grid-rows-4">
        <li v-for="ingredient in recipe.ingredients" :key="ingredient">
          {{ ingredient }}
        </li>
      </ul>
    </div>
    <div class="flex flex-col text-center">
      <h1 class="text-5xl">{{ recipe.title }}</h1>
      <p class="text-2xl">{{ recipe.description }}</p>
      <div class="self-center mt-12">
        <div class="text-xl">Steps</div>
        <ol class="">
          <li
            class="text-lg"
            v-for="(step, index) in recipe.steps"
            :key="index"
          >
            {{ `${index + 1}. ${step.description} ` }}
            <span v-if="step.note" class="block text-xs">{{ step.note }}</span>
          </li>
        </ol>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      recipe: {}
    }
  },
  mounted() {
    this.fetchRecipe()
  },
  methods: {
    async fetchRecipe() {
      const recipe = await this.$axios.$get(`recipes/${this.$route.params.id}`)
      this.recipe = recipe
    }
  }
}
</script>

<style></style>
