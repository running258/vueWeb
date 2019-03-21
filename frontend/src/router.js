import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'project',
      component: () => import('./views/ProjectView.vue')
    },
    {
      path: '/project',
      name: 'project',
      component: () => import('./views/ProjectView.vue')
    },
    {
      path: '/loginEnv',
      name: 'loginEnv',
      component: () => import('./views/LoginEnvView.vue')
    }
  ]
})


// import ProjectDetail from "./components/ProjectDetail.vue"
// import InterfaceDetail from "./components/InterfaceDetail.vue"
// import InterFaceLoginEnv from "./components/InterFaceLoginEnv.vue"
// import VAView from "./components/VAView.vue"
// import Record from "./components/Record.vue"


// const routes = [
//   {path:'/ProjectDetail', component:ProjectDetail},
//   {path:'/Project/:projectName/:env/InterfaceDetail/:interId', component:InterfaceDetail},
//   {path:'/InterFaceLoginEnv/', component:InterFaceLoginEnv},
//   {path:'/VAView/:VAName', component:VAView},
//   {path:'/Record', component:Record}
// ]
