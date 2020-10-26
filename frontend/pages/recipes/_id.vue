<template>
  <div class="grid grid-cols-1/3-2/3">
    <div>
      <div class="flex-shrink-0">
        <img :src="recipe.main_image_url" class="h-48 w-full object-cover" />
      </div>
      <p>Details</p>
      <ul>
        <li>{{ recipe.title }}</li>
        <li>Cuisine: {{ recipe.cuisine }}</li>
        <li>Category: {{ recipe.dish_category }}</li>
        <li>Subcategory: {{ recipe.dish_subcategory }}</li>
        <li>Difficulty: {{ recipe.difficulty }}</li>
        <li>Difficulty: {{ recipe.difficulty }}</li>
        <li>Servings: {{ recipe.servings }}</li>
        <li>Calories/Serving: {{ recipe.calories_per_serving }}</li>
      </ul>
      <p>Cookware</p>
      <ul>
        <li v-for="ware in recipe.cookware" :key="ware">{{ ware }}</li>
      </ul>
      <p>Ingredients</p>
      <ul>
        <li v-for="ingredient in recipe.ingredients" :key="ingredient">
          {{ ingredient }}
        </li>
      </ul>
    </div>
    <div>
      <p>{{ recipe.description }}</p>
      <ul>
        <li v-for="step in recipe.steps" :key="step.description">
          {{ step.description }}
        </li>
      </ul>
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
