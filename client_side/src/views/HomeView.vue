<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="image-container">
        <img src="../../public/banner.jpg">
        <div class="overlay"></div> <!-- Add the overlay div -->
        <div class="overlay-text">
          <p class="title mb-6">
            Welcome to Pristine Apparels
          </p>
          <p class="subtitle">
            The Best Online Mall
          </p>
        </div>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      <ProductBox 
        v-for="product in latestProducts"
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

<style>
.image-container {
  position: relative;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Adjust the opacity as needed */
}

.overlay-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: white;
}
</style>

