<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Pristine Apparels
        </p>
        <p class="subtitle">
          The Best Online Mall
        </p>

      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      <productBox
        v-bind="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />
        
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import ProductBox from '@/components/ProductBox'


export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: []
    }
  },
  components: { 
    ProductBox
  },
  mounted() {
    this.getLatestProducts()

    document.title = 'Home | Pristine Apparels'
  },
  methods: {
   async getLatestProducts() {
    this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>


