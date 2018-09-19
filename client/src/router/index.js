import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Guide from '@/components/Guide'
import About from '@/components/About'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/guide',
      name: 'Guide',
      component: Guide
    },
    {
      path: '/about',
      name: 'About',
      component: About
    }
  ]
})
