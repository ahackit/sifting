<template>
  <div>
    <div class="text-center flex justify-center">
      <table class="border-orange-200 border table-auto">
        <thead>
          <th class="px-4 py-2">Type</th>
          <th class="px-4 py-2">Name</th>
          <th class="px-4 py-2">Amount</th>
          <th class="px-4 py-2">UOM</th>
        </thead>
        <tbody>
          <tr v-for="recipe in sortedFetchedRecipes" :key="recipe.name">
            <td class="td border border-orange-200 px-4 py-2">
              {{ recipe.grocery }}
            </td>
            <td class="td border border-orange-200 px-4 py-2">
              {{ recipe.name }}
            </td>
            <td class="td border border-orange-200 px-4 py-2">
              {{ recipe.amount }}
            </td>
            <td class="td border border-orange-200 px-4 py-2">
              {{ recipe.uom }}
            </td>
          </tr>
        </tbody>
      </table>
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
