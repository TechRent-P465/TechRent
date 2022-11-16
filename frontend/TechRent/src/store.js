import { createStore } from 'vuex'

// imports of AJAX functions will go here
import { postNewItem, authenticate, register } from '@/api'

import { isValidJwt } from '@/utils'

const store = createStore({
  state: {
    // single source of data
    items: [],
    currentItem: {},
    userData: {},
    jwt: ''
  },

  actions: {
    login(context, userData) {
      context.commit('setUserData', { userData })
      return authenticate(userData)
        .then((response) => {
          console.log(response.data)
          context.commit('setJwtToken', { jwt: response.data })
        })
        .catch((error) => {
          console.log('Error Authenticating: ', error)
          //EventBus.$emit('failedAuthentication', error)
        })
    },
    register(context, userData) {
      context.commit('setUserData', { userData })
      return register(userData)
        .then(context.dispatch('login', userData))
        .catch((error) => {
          console.log('Error Registering: ', error)
          //EventBus.$emit('failedRegistering: ', error)
        })
    },
    submitNewItem(context, item) {
      return postNewItem(item, context.state.jwt.token)
    }
  },

  mutations: {
    setUserData(state, payload) {
      console.log('setUserData payload = ', payload)
      state.userData = payload.userData
    },
    setJwtToken(state, payload) {
      console.log('setJwtToken payload = ', payload)
      localStorage.token = payload.jwt.token
      state.jwt = payload.jwt
    }
  },

  getters: {
    isAuthenticated(state) {
      return isValidJwt(state.jwt.token)
    }
  }
})

export default store
