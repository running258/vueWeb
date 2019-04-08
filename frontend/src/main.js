import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import commonJs from './js/commonJs'
import './registerServiceWorker'
import './plugins/element.js'

Vue.config.productionTip = false
Vue.prototype.axios = axios
Vue.prototype.commonJs = commonJs

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
