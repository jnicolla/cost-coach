import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import CostCalculator from '@/components/CostCalculator'
import Disclaimer from '@/components/Disclaimer'
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
      path: '/calculator',
      name: 'CostCalculator',
      component: CostCalculator
    },
    {
      path: '/disclaimer',
      name: 'Disclaimer',
      component: Disclaimer
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
