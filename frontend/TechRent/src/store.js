import { createStore } from "vuex"

const store = createStore({
  state: {
    user: {
      loggedIn: false,
      data: null,
      passedVerification: false,
      securityQuestion1: "",
      securityQuestion2: ""
    }
  },
  getters: {
    user(state) {
      return state.user
    }
  },
  mutations: {
    SET_LOGIN_STATUS(state, val) {
      state.user.loggedIn = val
    },
    SET_USER_DATA(state, data) {
      state.user.data = data
    },
    SET_QUESTION_VERIFICATION_STATUS(state, val) {
      state.user.passedVerification = val
    }
  },
  actions: {
    async register() {},
    async login() {},
    async forgotPasswordLogin() {
      //Check for security questions if they match
    },
    async logout() {},
    async getUser() {}
  }
})

export default store
