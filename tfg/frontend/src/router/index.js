import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import index from '@/components/index'
import Recipe from '@/components/Recipe'
import ListProduct from '@/components/Product/ListProduct'
import Product from '@/components/Product'
import Register from '@/components/Register'
import Publicity_campaign from '@/components/Publicity_campaign'

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
      name: 'ListProduct',
      component: ListProduct
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
  ],
  mode: 'history'
})
 