// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueCookie from 'vue-cookie'



import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import moment from 'moment'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueCookie)
Vue.prototype.moment = moment

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
