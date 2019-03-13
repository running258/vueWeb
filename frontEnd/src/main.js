import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue'
import VueRouter from 'vue-router'
import axios from 'axios'

Vue.use(ElementUI)
Vue.use(VueRouter)

Vue.prototype.axios = axios

import Project from "./components/Project.vue"
import ProjectDetail from "./components/ProjectDetail.vue"
import InterfaceDetail from "./components/InterfaceDetail.vue"

const routes = [
  {path:'*', redirect:"/Project"},
  {path:'/Project', component:Project},
  {path:'/ProjectDetail/:aid', component:ProjectDetail},
  {path:'/Project/:projectName/InterfaceDetail/:interId', component:InterfaceDetail}
]

const router = new VueRouter({
  routes
})

new Vue({
  el: '#app',
  router,
  render: h => h(App),
  
})

