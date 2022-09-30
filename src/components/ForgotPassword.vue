<template lang="">
  <div class="container">
    <div class="forgotPassword-view">
      <form @submit.prevent="register">
        <h2 class="">Forgot Password</h2>

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
          <label for="question1">What is your mother's maiden name?</label>
          <input
            class="form-input"
            type="text"
            name="question1"
          />
        </div>
        <div class="input">
          <label for="question2">What high school did you go to?</label>
          <input
            class="form-input"
            type="text"
            name="question2"
          />
        </div>
        <div class="input">
          <label for="question3">What is the name of your first pet?</label>
          <input
            class="form-input"
            type="text"
            name="question3"
          />
        </div>
        <button type="submit" class="" id="continue_button">Continue</button>
      </form>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { ref } from "vue";
import { useStore } from "vuex";

export default {
  name: "ForgotPasswordCredentials",
  setup() {
    const store = useStore();
    const router = useRouter();
    const email = ref("");
    const question1 = ref("");
    const question2 = ref("");
    const question3 = ref("");
    const error = ref(null);

    const credentials = async () => {
      try {
        await store.dispatch("register", {
          email: email.value,
          question1: question1.value,
          question2: question2.value,
          question3: question3.value,
        });

        router.push("/");
      } catch (err) {
        error.value = err.message;
      }
    };
    return { credentials, email, question1, question2, question3, error};
  },
};
</script>

<style>
.forgotPassword-view {
  position: fixed;
  z-index: 10000;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: 1px solid lightgray;
  padding: 4rem 4rem;
  border-radius: 5px;
  background: black;
}
</style>