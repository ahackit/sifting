<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="w-1/2 mx-auto flex flex-row justify-center mt-8">
      <div>
        <p>Convert</p>
        <input
          class="border"
          type="number"
          name="amount-uom"
          id="amount-uom"
          v-model="amountUOM"
        />
        <select class="border" name="uom-type" id="uom-type" v-model="startUOM">
          <option
            v-for="option in options"
            :value="option.measurement"
            :key="option.id"
            >{{ option.measurement }}</option
          >
        </select>
        <p>To</p>
        <select class="border" name="uom-type" id="uom-type" v-model="endUOM">
          <option
            v-for="option in options"
            :value="option.measurement"
            :key="option.id"
            >{{ option.measurement }}</option
          >
        </select>
        <button @click="getConversion">Generate</button>
      </div>
      <div>
        <p>Results: {{ conversionResults }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      options: [],
      startUOM: '',
      endUOM: '',
      amountUOM: 0,
      conversionResults: ''
    }
  },
  async mounted() {
    const response = await this.$axios.get('/uoms')
    this.options = response.data
  },
  methods: {
    async getConversion() {
      const response = await this.$axios.get(
        `/uoms/convert/?start_uom_number=${this.amountUOM}&start_uom=${this.startUOM}&end_uom=${this.endUOM}`
      )
      this.conversionResults = response.data
    }
  }
}
</script>

<style></style>
