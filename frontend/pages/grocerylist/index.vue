<template
  ><p>{{ selectedRecipes }}</p>
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
    })
  },
  methods: {
    async fetchSelectedRecipe(id) {
      const response = await this.$axios.get(`/recipes/${id}/grocerylist`)
      this.fetchedRecipes = [...this.fetchedRecipes, response.data]
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
