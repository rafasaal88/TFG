import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListProduct from '@/components/Product/ListProduct'
import EditProduct from '@/components/Product/EditProduct'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
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
    }
  ],
  mode: 'history'
})
 