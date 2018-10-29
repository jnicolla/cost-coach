<template>
  <div id="app">
    <Navbar></Navbar>
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: 
  {
    Navbar
  }
}
</script>


<style <style lang="scss">
@import "~vue-material/dist/theme/engine"; // Import the theme engine

@include md-register-theme("default", (
 primary: #d65f36, // The primary color of your brand
  accent: #232859 // The secondary color of your brand
));

@import "~vue-material/dist/theme/all"; // Apply the theme
</style>

