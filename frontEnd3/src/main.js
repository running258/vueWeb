import Vue from 'vue'
import ElementUI from 'element-ui';
import App from './App.vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import 'element-ui/lib/theme-chalk/index.css';


Vue.use(ElementUI)
Vue.use(VueRouter)

Vue.prototype.axios = axios

import Project from "./components/Project.vue"
import ProjectDetail from "./components/ProjectDetail.vue"
import InterfaceDetail from "./components/InterfaceDetail.vue"
import InterFaceLoginEnv from "./components/InterFaceLoginEnv.vue"
import VAView from "./components/VAView.vue"
import Record from "./components/Record.vue"

const routes = [
  {path:'*', redirect:"/Project"},
  {path:'/Project', component:Project},
  {path:'/ProjectDetail', component:ProjectDetail},
  {path:'/Project/:projectName/:env/InterfaceDetail/:interId', component:InterfaceDetail},
  {path:'/InterFaceLoginEnv/', component:InterFaceLoginEnv},
  {path:'/VAView/:VAName', component:VAView},
  {path:'/Record', component:Record}
]

const router = new VueRouter({
  routes
})

new Vue({
  el: '#app',
  router,
  render: h => h(App),
  
})

