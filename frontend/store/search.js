export const state = () => ({
  searchString: ''
})

export const getters = {
  parsedSearch: (state) => {
    return state.searchString.split(' ')
  }
}
export const mutations = {
  updateSearch(state, text) {
    state.searchString = text
  }
}
