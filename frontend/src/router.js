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
    },
    {
      path: '/projectDetail',
      name: 'projectDetail',
      component: () => import('./views/ProjectDetailView.vue')
    },
    {
      path: '/VAView',
      name: 'VAView',
      component: () => import('./views/VAView.vue')
    },
  ]
})
