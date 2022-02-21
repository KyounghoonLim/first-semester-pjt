import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null
  },
  mutations: {
    USER_UPDATE: function(state, userData){
      state.user = userData
    }
  },
  actions: {
    user_update: function({ commit }, userData){
      commit('USER_UPDATE', userData)
    }
  },
  modules: {
  },
  getters: {
  }
})