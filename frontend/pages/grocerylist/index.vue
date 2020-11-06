<template>
  <div>
    <div>
      <p v-for="recipe in sortedFetchedRecipes" :key="recipe.name">
        {{ recipe.grocery }}
        {{ recipe.name }}
        {{ recipe.amount }}
        {{ recipe.uom }}
      </p>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data() {
    return {
      fetchedRecipes: []
    }
  },
  computed: {
    ...mapState({
      selectedRecipes: (state) => state.grocery_list.list
    }),
    sortedFetchedRecipes() {
      const newList = this.fetchedRecipes
      return newList.sort((a, b) => (a.grocery > b.grocery ? 1 : -1))
    }
  },
  methods: {
    async fetchSelectedRecipe(id) {
      const response = await this.$axios.get(`/recipes/${id}/grocerylist`)
      response.data.ingredients.forEach((ingredient) => {
        const groceryDetails = {
          amount: ingredient.amount.number,
          uom: ingredient.amount.uom,
          grocery: ingredient.grocery.type_txt,
          name: ingredient.name
        }
        this.fetchedRecipes = [...this.fetchedRecipes, groceryDetails]
      })
    }
  },
  mounted() {
    this.selectedRecipes.forEach((recipe) =>
      this.fetchSelectedRecipe(recipe.id)
    )
  }
}
</script>

<style></style>
