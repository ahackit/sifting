<template>
  <nav class="mx-auto bg-orange-200 p-4 flex flex-row justify-between">
    <div class="w-1/4 text-center flex flex-row justify-between">
      <p class="pl-16 font-semibold">Sifting</p>
    </div>
    <div class="w-1/4 text-center flex flex-row justify-between">
      <nuxt-link to="/" class="font-bold text-sm">Recipes</nuxt-link>
      <nuxt-link to="/" class="font-bold text-sm">UOM Calc</nuxt-link>
      <nuxt-link to="/" class="font-bold text-sm">Grocery Planner</nuxt-link>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style></style>
