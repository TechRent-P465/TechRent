<template lang="">
  <div class="login-view">
    <form @submit.prevent="login">
      <h2 class="">Login</h2>
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
      <div class="login-question">
        <a class="forgot-password" @click="routeToRegister">
          Forget your password?
        </a>
      </div>
      <div class="login-question">
        Don't have an account?
        <a class="register-account" @click="routeToRegister"> Register </a>
      </div>
      <button type="submit" class="" id="login_button">Login</button>
    </form>
    <div class="or">
      <h4>OR</h4>
      <hr />
    </div>

    <h3>Login with:</h3>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { ref } from "vue";
import { useStore } from "vuex";

export default {
  name: "LoginUser",
  setup() {
    const store = useStore();
    const router = useRouter();
    const email = ref("");
    const password = ref("");
    const error = ref(null);

    const login = async () => {
      try {
        await store.dispatch("login", {
          email: email.value,
          password: password.value,
        });

        router.push("/");
      } catch (err) {
        error.value = err.message;
      }
    };
    return { login, email, password, error };
  },

  methods: {
    routeToRegister() {
      this.$router.push("/register");
    },
  },
};
</script>
<style scoped>
.login-view {
  position: fixed;
  z-index: 10000;
  top: 55%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: 1px solid lightgray;
  padding: 4rem 4rem;
  border-radius: 5px;
  background: black;
}

.login-question {
  margin-bottom: 10px;
}

button {
  width: 100%;
}

hr {
  height: 0.2rem;
  width: 100%;
  margin-left: 10px;
  border-width: 0;
  background-color: lightgray;
}

.or {
  display: flex;
  align-items: center;
  margin: 15px 0;
}
</style>
