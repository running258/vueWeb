import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      // name: 'project',
      // component: () => import('./views/ProjectView.vue')
      component: () => import('./views/VAProjectView.vue')
    },
    {
      path: '/InterProjectView',
      name: 'InterProjectView',
      component: () => import('./views/InterProjectView.vue')
    },
    {
      path: '/InterProjectDetailView',
      name: 'InterProjectDetailView',
      component: () => import('./views/InterProjectDetailView.vue')
    },
    {
      path: '/loginEnv',
      name: 'loginEnv',
      component: () => import('./views/LoginEnvView.vue')
    },
    {
      path: '/OESProjectView',
      name: 'OESProjectView',
      component: () => import('./views/OESProjectView.vue')
    },
    {
      path: '/OESProjectDetailView',
      name: 'OESProjectDetailView',
      component: () => import('./views/OESProjectDetailView.vue')
    },
    {
      path: '/VAView',
      name: 'VAView',
      component: () => import('./views/VAView.vue')
    },
    {
      path: '/VAProject',
      name: 'VAProject',
      component: () => import('./views/VAProjectView.vue')
    },
  ]
})
