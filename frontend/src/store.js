import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    headerShow:false,
    oesViewAbleProjectId:'',
    oesViewAbleProjectName:'',
  },
  mutations: {
    headerShow(state){
      state.headerShow = true;
    },
    headerHide(state){
      state.headerShow = false;
    },
    setOESViewAbleProjectId(state,projectId){
      state.oesViewAbleProjectId = projectId;
    },
    setOESViewAbleProjectName(state,projectName){
      state.oesViewAbleProjectName = projectName;
    },
  },
  actions: {

  }
})
