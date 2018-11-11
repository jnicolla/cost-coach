import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import CostCalculator from '@/components/CostCalculator'
import Disclaimer from '@/components/Disclaimer'
import Guide from '@/components/Guide'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home
    },
    {
      path: '/CostCalculator',
      name: 'CostCalculator',
      component: CostCalculator
    },
    {
      path: '/Disclaimer',
      name: 'Disclaimer',
      component: Disclaimer
    }, 
    {
      path: '/Guide',
      name: 'Guide',
      component: Guide
    }

  ]
})
