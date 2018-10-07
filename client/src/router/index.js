import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Guide from '@/components/Guide'
import About from '@/components/About'
import Timeline from '@/components/Timeline'
import LightTimeline from 'vue-light-timeline'
Vue.use(LightTimeline)

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/about',
      name: 'About',
      component: About
    },
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
      path: '/timeline',
      name: 'Timeline',
      component: Timeline 
    }
  ]
})
