<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-row">
    <div class="w-1/2 mx-auto flex flex-col justify-center mt-8">
      <div class="flex flex-row justify-center">
        <div class="flex flex-col justify-center w-1/3  text-center">
          <p class="text-xl">Volume Calculator</p>
          <p>Convert</p>
          <input
            class="border px-2"
            type="number"
            name="amount-uom"
            id="amount-uom"
            v-model="amountUOM"
          />
          <select
            class="border"
            name="uom-type"
            id="uom-type"
            v-model="startUOM"
          >
            <option
              v-for="option in volumeUOMs"
              :value="option.measurement"
              :key="option.id"
              >{{ option.measurement }}</option
            >
          </select>
          <p class="text-center">To</p>
          <select class="border" name="uom-type" id="uom-type" v-model="endUOM">
            <option
              v-for="option in volumeUOMs"
              :value="option.measurement"
              :key="option.id"
              >{{ option.measurement }}</option
            >
          </select>
          <button
            class="bg-orange-200 rounded border-orange-400 mt-2 py-2 px-4 hover:bg-orange-400"
            @click="getConversion"
          >
            Generate
          </button>

          <div>
            <p>Results: {{ conversionResults }} {{ endUOM }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="w-1/2 mx-auto flex flex-col justify-center mt-8">
      <div class="flex flex-row justify-center">
        <div class="flex flex-col justify-center w-1/3 text-center">
          <p class="text-xl">Weight Calculator</p>
          <p>Convert</p>
          <input
            class="border px-2"
            type="number"
            name="amount-uom"
            id="amount-uom"
            v-model="amountWeightUOM"
          />
          <select
            class="border"
            name="uom-type"
            id="uom-type"
            v-model="startWeightUOM"
          >
            <option
              v-for="option in weightUOMs"
              :value="option.measurement"
              :key="option.id"
              >{{ option.measurement }}</option
            >
          </select>
          <p>To</p>
          <select
            class="border"
            name="uom-type"
            id="uom-type"
            v-model="endWeightUOM"
          >
            <option
              v-for="option in weightUOMs"
              :value="option.measurement"
              :key="option.id"
              >{{ option.measurement }}</option
            >
          </select>
          <button
            class="bg-orange-200 rounded border-orange-400 mt-2 py-2 px-4 hover:bg-orange-400"
            @click="getWeightConversion"
          >
            Generate
          </button>

          <div>
            <p>Results: {{ weightConversionResults }} {{ endWeightUOM }}</p>
          </div>
        </div>
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
      startWeightUOM: '',
      endWeightUOM: '',
      amountWeightUOM: 0,
      conversionResults: '',
      weightConversionResults: ''
    }
  },
  computed: {
    volumeUOMs() {
      return this.options.filter(
        (option) => option.conversion_type === 'volume'
      )
    },
    weightUOMs() {
      return this.options.filter(
        (option) => option.conversion_type === 'weight'
      )
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
    },
    async getWeightConversion() {
      const response = await this.$axios.get(
        `/uoms/convert/?start_uom_number=${this.amountWeightUOM}&start_uom=${this.startWeightUOM}&end_uom=${this.endWeightUOM}`
      )
      this.weightConversionResults = response.data
    }
  }
}
</script>

<style></style>
