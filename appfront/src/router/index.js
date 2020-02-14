import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Company from '@/components/Company'
import Coder from '@/components/Coder'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/coder',
      name: 'Coder',
      component: Coder
    },
    {
      path: '/company',
      name: 'Company',
      component: Company
    }
  ]
})
