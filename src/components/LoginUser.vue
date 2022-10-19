<template lang="">
  <div class="login-view">
    <form @submit="submit">
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
        <a class="forgot-password" @click="routeToForgotPassword">
          Forget your password?
        </a>
      </div>
      <div class="login-question">
        Don't have an account?
        <a class="register-account" @click="routeToRegister"> Register </a>
      </div>
      <button type="submit" class="" id="login_button" @click="routeToLogin">Login</button>
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
  import axios from 'axios';
  
  export default {
    name:'LoginUser',
    data() {
      return {
        msg : ""
      };
    },
    methods : {
      getresponse(){
        const path = 'http://localhost:5000/LoginUser';
        axios.get(path)
        .then ((res) =>{
          console.log(res.data)
          this.msg = res.data
        })
        .catch ((err) => {
          console.error(err)
        });
      },
    },
    created(){
      this.getresponse();
      
    }
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
