<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="w-1/2 mx-auto flex flex-row justify-center mt-8">
      <div>
        <p>Convert</p>
        <input class="border" type="number" name="amount-uom" id="amount-uom" />
        <select class="border" name="uom-type" id="uom-type">
          <option
            v-for="option in options"
            :value="option.measurement"
            :key="option.id"
            >{{ option.measurement }}</option
          >
        </select>
        <p>To</p>
        <select class="border" name="uom-type" id="uom-type">
          <option
            v-for="option in options"
            :value="option.measurement"
            :key="option.id"
            >{{ option.measurement }}</option
          >
        </select>
        <button>Generate</button>
      </div>
      <div>
        <p>Results:</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      options: []
    }
  },
  async mounted() {
    const response = await this.$axios.get('/uoms')
    this.options = response.data
  }
}
</script>

<style></style>
