import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'


import index from '@/components/index'
import Recipe from '@/components/Recipe'
import Recipe_list from '@/components/Recipe_list'
import Product_list from '@/components/Product_list'
import Product from '@/components/Product'
import Register from '@/components/Register'
import Publicity_campaign from '@/components/Publicity_campaign'
import Publicity_campaign_list from '@/components/Publicity_campaign_list'
import Tag_NFC from '@/components/Tag_NFC'
import Point_list from '@/components/Point_list'

import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },   
    {
      path: '/products_list',
      name: 'Product_list',
      component: Product_list
    },
    {
      path: '/product/:id',
      name: 'Product',
      component: Product
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/publicity_campaign/:id',
      name: 'publicity_campaign',
      component: Publicity_campaign
    },
    {
      path: '/recipe/:id',
      name: 'recipe',
      component: Recipe
    },
    {
      path: '/publicity_campaign_list',
      name: 'publicity_campaign_list',
      component: Publicity_campaign_list
    },
    {
      path: '/recipe_list',
      name: 'recipe_list',
      component: Recipe_list
    },
    {
      path: '/tag/:id',
      name: 'tag',
      component: Tag_NFC
    },
    {
      path: '/point',
      name: 'point',
      component: Point_list
    },
  ],
  mode: 'history'
})