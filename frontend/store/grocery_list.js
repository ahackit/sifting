export const state = () => ({
  list: []
})

export const getters = {
  findRecipe: (state) => (recipe) => {
    return state.list.find((r) => r.id === recipe.id)
  }
}

export const mutations = {
  addToGroceryList(state, recipe) {
    state.list.push(recipe)
  },
  removeFromGroceryList(state, recipe) {
    state.list = state.list.filter((r) => r.id !== recipe.id)
  }
}
