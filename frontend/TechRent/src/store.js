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

// import { createStore } from "vuex"

// const store = createStore({
//   state: {
//     user: {
//       loggedIn: false,
//       data: null,
//       passedVerification: false,
//       securityQuestion1: "",
//       securityQuestion2: ""
//     }
//   },
//   getters: {
//     user(state) {
//       return state.user
//     }
//   },
//   mutations: {
//     SET_LOGIN_STATUS(state, val) {
//       state.user.loggedIn = val
//     },
//     SET_USER_DATA(state, data) {
//       state.user.data = data
//     },
//     SET_QUESTION_VERIFICATION_STATUS(state, val) {
//       state.user.passedVerification = val
//     }
//   },
//   actions: {
//     async register() {},
//     async login() {},
//     async forgotPasswordLogin() {
//       //Check for security questions if they match
//     },
//     async logout() {},
//     async getUser() {}
//   }
// })

// export default store
