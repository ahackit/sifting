<template>
  <div class="flex flex-col rounded-lg shadow-lg overflow-hidden">
    <nuxt-link to="/recipes/1" class="block">
      <div class="flex-shrink-0">
        <img
          src="https://res.cloudinary.com/drkjixre2/image/upload/v1572823949/refried_beans_zj5ehv.jpg"
          alt="RefriedBeans"
          srcset=""
          class="h-48 w-full object-cover"
        />
      </div>
      <div class="flex-1 bg-white p-6 flex flex-col justify-between">
        <div class="flex-1">
          <h3 class="mt-2 text-xl leading-7 font-semibold text-gray-900">
            Refried Beans
          </h3>
          <p class="mt-3 text-base leading-6 text-gray-500">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto
            accusantium praesentium eius, ut atque fuga culpa, similique sequi
            cum eos quis dolorum.
          </p>
        </div>
      </div>
    </nuxt-link>
  </div>
</template>

<script>
export default {
  name: 'RecipeCard'
}
</script>

<style></style>
