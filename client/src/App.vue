<template>
  <div id="app">

    <Navbar></Navbar>

      <router-view/>

    <Footer></Footer>

  </div>
</template>

<script>
import Footer from './components/Footer'
import Navbar from './components/Navbar'

export default 
{
  name: 'App', 
  components: {Footer,Navbar}
}
</script>






<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #1979da;
}
a {
 text-decoration: none;
}
</style>
