import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue'
import VueRouter from 'vue-router'
import axios from 'axios'

Vue.prototype.$http = axios.create({
  baseURL: "http://127.0.0.1:5000",
  timeout: 5000,
  headers: {'Content-Type': 'application/json'}
});

Vue.use(ElementUI)
Vue.use(VueRouter)


import Project from "./components/Project.vue"
import ProjectDetail from "./components/ProjectDetail.vue"
import InterfaceDetail from "./components/InterfaceDetail.vue"

const routes = [
  {path:'/Project', component:Project},
  {path:'/ProjectDetail/:aid', component:ProjectDetail},
  {path:'/InterfaceDetail', component:InterfaceDetail},
  {path:'*', redirect:"/InterfaceDetail"}
]

const router = new VueRouter({
  routes
})

new Vue({
  el: '#app',
  router,
  render: h => h(App),
  
})

