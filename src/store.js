import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
} from "firebase/auth";
import { auth } from "./firebaseconfig";
import { createStore } from "vuex";

const store = createStore({
  state: {
    user: {
      loggedIn: false,
      data: null,
    },
  },
  getters: {
    user(state) {
      return state.user;
    },
  },
  mutations: {
    SET_LOGIN_STATUS(state, val) {
      state.user.loggedIn = val;
    },
    SET_USER_DATA(state, data) {
      state.user.data = data;
    },
  },
  actions: {
    async register(context, { email, password, name }) {
      const res = await createUserWithEmailAndPassword(auth, email, password);
      if (res) {
        context.commit("SET_USER_DATA", res.user);
        res.user.displayName = name;
      } else {
        alert("Unable to register user.");
        throw new Error("Unable to register user.");
      }
    },
    async login(context, { email, password }) {
      const res = await signInWithEmailAndPassword(auth, email, password);
      if (res) {
        context.commit("SET_USER_DATA", res.user);
      } else {
        alert("Unable to login.");
        throw new Error("Unable to login.");
      }
    },
    async logout() {},
    async getUser() {},
  },
});

export default store;
