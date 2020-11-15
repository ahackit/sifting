<template>
  <nav class="mx-auto bg-orange-200 p-4 flex flex-row justify-center">
    <div class="w-1/4 text-center flex flex-row justify-between">
      <nuxt-link to="/" class="font-extrabold text-sm">Recipes</nuxt-link>
      <nuxt-link to="/calculators" class="font-extrabold text-sm"
        >Calculators</nuxt-link
      >
      <nuxt-link to="/grocerylist" class="font-extrabold text-sm"
        >Grocery Planner</nuxt-link
      >
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style></style>
