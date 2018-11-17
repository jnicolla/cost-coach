<template>
  <v-app id="app" data-app>
    <navbar></navbar>
    <div class="mb-5 pb-3">
      <transition name="fade" mode="out-in">
        <router-view/>
      </transition>
    </div>
    <div id="foot">
      <Footer></Footer>
    </div>
  </v-app>
</template>

<script>
import Footer from './components/Footer'
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: {
    Footer,
    Navbar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#foot {
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
}

/* transition */
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
