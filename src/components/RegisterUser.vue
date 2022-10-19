<template lang="">
  <div class="container">
    <div class="register-view">
      <div class="close" @click="routeToDashboard"></div>
      <form @submit.prevent="register">
        <h1 class="">Register</h1>
        <div class="input">
          <label for="name">Name</label>
          <input
            class="form-input"
            type="text"
            name="name"
            placeholder="Johnny Appleseed"
          />
        </div>
        <div class="input">
          <label for="email">Email address</label>
          <input
            class="form-input"
            type="text"
            name="email"
            placeholder="email@adress.com"
          />
        </div>
        <div class="input">
          <label for="password">Password</label>
          <input
            class="form-input"
            type="password"
            name="password"
            placeholder="password"
          />
        </div>
        <div class="or">
          <h4>Security Questions</h4>
          <hr />
        </div>
        <div class="input">
          <label for="question1">What is your mother's maiden name?</label>
          <input class="form-input" type="text" name="question1" />
        </div>
        <div class="input">
          <label for="question2">What high school did you go to?</label>
          <input class="form-input" type="text" name="question2" />
        </div>
        <button type="submit" class="" id="register_button">Register</button>
      </form>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router"
import { ref } from "vue"
import { useStore } from "vuex"

export default {
  name: "RegisterUser",
  setup() {
    const store = useStore()
    const router = useRouter()
    const name = ref("")
    const email = ref("")
    const password = ref("")
    const question1 = ref("")
    const question2 = ref("")
    const error = ref(null)

    const register = async () => {
      try {
        await store.dispatch("register", {
          email: email.value,
          password: password.value,
          name: name.value,
          question1: question1.value,
          question2: question2.value
        })

        router.push("/")
      } catch (err) {
        error.value = err.message
      }
    }
    return { register, name, email, password, question1, question2, error }
  },

  methods: {
    routeToRegister() {
      this.$router.push("/register")
    },
    routeToForgotPassword() {
      this.$router.push("/forgotpassword")
    },
    routeToDashboard() {
      this.$router.push("/")
    }
  }
}
</script>

<style>
.register-view {
  position: fixed;
  z-index: 10000;
  top: 70%;
  left: 50%;
  transform: translate(-50%, -65%);
  border: 1px solid var(--color-primary);
  padding: 4em 4rem;
  border-radius: 5px;
  background: var(--color-highlight);
}

#register_button {
  width: 100%;
}

.close:after {
  display: inline-block;
  position: fixed;
  top: 5px;
  right: 20px;
  content: "\00d7";
  font-size: 30px;
}

.close:hover {
  cursor: pointer;
  color: var(--color-pop);
}
</style>
