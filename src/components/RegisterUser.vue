<template lang="">
  <div class="container">
    <div class="register-view">
      <form @submit.prevent="handleSubmit">
        <h2 class="">Register</h2>
        <div class="input">
          <label for="name">Name</label>
          <input
            class="form-input"
            type="text"
            name="name"
            v-model = "name"
            placeholder="Johnny Appleseed"
          />
        </div>
        <div class="input">
          <label for="email">Email address</label>
          <input
            class="form-input"
            type="text"
            name="email"
            v-model="email"
            placeholder="email@adress.com"
          />
        </div>
        <div class="input">
          <label for="password">Password</label>
          <input
            class="form-input"
            type="password"
            name="password"
            v-model="password"
            placeholder="password"
          />
        </div>
        <div class="or">
          <h4>Security Questions</h4>
          <hr />
        </div>
        <div class="input">
          <label for="question1">What is your mother's maiden name?</label>
          <input
            class="form-input"
            type="text"
            v-model="question1"
            name="question1"
          />
        </div>
        <div class="input">
          <label for="question2">What high school did you go to?</label>
          <input
            class="form-input"
            type="text"
            name="question2"
            v-model="question2"
          />
        </div>
        <button type="submit" class="" id="register_button">Register</button>
      </form>
    </div>
  </div>
</template>

<!-- <script>
import { useRouter } from "vue-router";
import { ref } from "vue";
import { useStore } from "vuex";
import axios from 'axios';

export default {
  name: "RegisterUser",
  setup() {
    const store = useStore();
    const router = useRouter();
    const name = ref("");
    const email = ref("");
    const password = ref("");
    const question1 = ref("");
    const question2 = ref("");
    const error = ref(null);

    const register = async () => {
      try {
        await store.dispatch("register", {
          email: email.value,
          password: password.value,
          name: name.value,
          question1: question1.value,
          question2: question2.value
        });

        router.push("/");
      } catch (err) {
        error.value = err.message;
      }
    };
    return { register, name, email, password, question1, question2, error };
  },
  methods : {
    getTestResponse(){
      const path = 'http://127.0.0.1:5000/register'
      axios.get(path)
    .then(response => {
      console.log(response.data);
      this.msg = response.data;
    })
    .catch(err => {
      console.log(err);
    });
    },
  },
  created() {
    this.getTestResponse()
  }
};
</script> -->

<script>

  import axios from 'axios';
  export default {
    name: 'RegisterUser',
    data(){
      return {
        name:'',
        email:'',
        password:'',
        question1:'',
        question2:''

      }
    },
    methods: {
      handleSubmit(){
        const data = {
          name : this.name,
          email : this.email,
          password : this.password,
          question1 : this.question1,
          question2 : this.question2 
        };
        axios.post('http://127.0.0.1:5000/register',data)
        .then(res => {
          console.log(res)
        }).catch(err => {
          console.log(err)
        })
      }
    }
  }


</script>


<style>
.register-view {
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
