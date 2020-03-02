import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListProduct from '@/components/Product/ListProduct'
import EditProduct from '@/components/Product/EditProduct'
import Register from '@/components/Register'
import index from '@/components/index'
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
      path: '/product_edit/:id',
      name: 'EditProduct',
      component: EditProduct
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

  ],
  mode: 'history'
})
 