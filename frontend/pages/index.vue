<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="w-1/2 mx-auto flex flex-row justify-center mt-8">
      <RecipeSearchInput></RecipeSearchInput>
    </div>
    <RecipeCardContainer :recipes="filteredRecipes"></RecipeCardContainer>
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
  computed: {
    parsedSearch() {
      return this.$store.getters['search/parsedSearch']
    },
    filteredRecipes() {
      let filterRecipes = [...this.recipes]
      if (this.parsedSearch) {
        filterRecipes = filterRecipes.filter((recipe) => {
          let match = true
          this.parsedSearch.forEach((search) => {
            if (search.includes(':')) {
              const keySearch = search.split(':')
              if (
                !(
                  recipe[keySearch[0].toLowerCase()].toLowerCase() ===
                  keySearch[1].toLowerCase()
                )
              ) {
                match = false
              }
            } else if (
              !recipe.title.toLowerCase().includes(search.toLowerCase())
            ) {
              match = false
            }
          })
          if (match) {
            return recipe
          }
        })
      }
      return filterRecipes
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
