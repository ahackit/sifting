<template>
  <div class="bg-white overflow-hidden overflow-hidden shadow rounded-lg">
    <div class="px-4 py-5 sm:p-6">
      <!-- Content goes here -->
      <img
        src="https://res.cloudinary.com/drkjixre2/image/upload/v1572823949/refried_beans_zj5ehv.jpg"
        alt="RefriedBeans"
        srcset=""
        class="bg-contain"
      />
    </div>
    <div class="border-t border-gray-200 px-4 py-4 sm:px-6">
      <!-- Content goes here -->
      <!-- We use less vertical padding on card footers at all sizes than on headers or body sections -->
      <Button class="float-right"></Button>
    </div>
  </div>
</template>

<script>
import Button from './Button'
export default {
  name: 'RecipeCard',
  components: { Button }
}
</script>

<style></style>
