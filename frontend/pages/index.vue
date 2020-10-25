<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="w-1/2 mx-auto flex flex-row justify-center mt-8">
      <RecipeSearchInput></RecipeSearchInput>
    </div>

    <RecipeCardContainer :recipes="recipes"></RecipeCardContainer>
  </div>
</template>

<script>
import RecipeCardContainer from '~/components/RecipeCardContainer.vue'
import RecipeSearchInput from '~/components/RecipeSearchInput.vue'

export default {
  components: {
    RecipeSearchInput,
    RecipeCardContainer
  },
  data() {
    return {
      recipes: []
    }
  },
  mounted() {
    this.fetchRecipes()
  },
  methods: {
    async fetchRecipes() {
      const recipes = await this.$axios.$get('recipes/')
      this.recipes = recipes
    }
  }
}
</script>

<style>
/* Sample `apply` at-rules with Tailwind CSS
.container {
  @apply min-h-screen flex justify-center items-center text-center mx-auto;
}
*/
</style>
