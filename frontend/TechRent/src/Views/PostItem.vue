<template lang="">
  <div class="post-item">
    <div class="post-item-container">
      <form @submit.prevent="postItem">
        <h1 class="">Post Item</h1>
        <div class="or">
          <h4>Details</h4>
          <hr />
        </div>
        <div class="input">
          <label for="name">Item Name</label>
          <input
            class="form-input"
            type="text"
            name="name"
            v-model="item_name"
            placeholder="name of item you are renting out"
          />
          <div
            class="error"
            v-for="(error, index) of v$.item_name.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>

        <div class="input">
          <label for="brand">Description</label>
          <textarea
            class="form-input"
            type="textarea"
            name="brand"
            v-model="description"
            placeholder="brief description of item and additional details"
          ></textarea>
          <div
            class="error"
            v-for="(error, index) of v$.description.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>
        <div class="input">
          <label for="brand">Brand</label>
          <input
            class="form-input"
            type="text"
            name="brand"
            v-model="brand"
            placeholder="item brand"
          />
          <div
            class="error"
            v-for="(error, index) of v$.brand.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>
        <div class="input">
          <label for="price">Price</label>
          <input
            class="form-input"
            type="number"
            name="price"
            v-model="price"
            placeholder="price to rent item (per day)"
          />
          <div
            class="error"
            v-for="(error, index) of v$.price.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>
        <div class="input">
          <label for="price">Location</label>
          <input
            class="form-input"
            type="text"
            name="location"
            v-model="location"
            placeholder="address to pick up item from"
          />
          <div
            class="error"
            v-for="(error, index) of v$.location.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>
        <div class="input">
          <label for="item-image">Image</label>
          <input
            class="form-input"
            type="file"
            name="item-image"
            v-on:change="image_url"
            accept="image/*"
          />
        </div>
        <div class="or">
          <h4>Contact</h4>
          <hr />
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
          <div
            class="error"
            v-for="(error, index) of v$.email.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>
        <div class="input">
          <label for="phone">Phone Number</label>
          <input
            class="form-input"
            type="text"
            name="phone"
            v-model="phone"
            placeholder="###-###-####"
          />
        </div>
        <button type="submit" class="" id="register_button">
          Post to Website
        </button>
      </form>
    </div>
  </div>
</template>
<script>
import { email, required } from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'
export default {
  name: 'RegisterUser',
  setup() {
    return { v$: useVuelidate() }
  },
  data() {
    return {
      item_name: '',
      description: '',
      brand: '',
      price: 0,
      location: '',
      image_url: '',
      email: '',
      phone: ''
    }
  },
  methods: {
    postItem() {
      this.v$.$validate()
      console.log(this.v$)
      if (!this.v$.$error && confirm('Are you sure you want to post?')) {
        const data = {
          item_name: this.item_name,
          description: this.description,
          brand: this.brand,
          price: this.price,
          location: this.location,
          image_url: this.image_url,
          email: this.email,
          phone: this.phone,
          posted_at: new Date()
        }

        this.$store.dispatch('submitNewItem', data).then(() => {
          this.$router.push('/browse')
          alert('Form submitted successfully')
        })
      } else {
        console.log(this.v$)
        console.log(this.v$.$errors)
      }
    }
  },
  validations() {
    return {
      item_name: { required },
      description: { required },
      brand: { required },
      price: { required },
      location: { required },
      email: { required, email }
    }
  }
}
</script>
<style scoped>
.post-item-container {
  width: 80%;
  margin: 25px auto;
  padding: 2em;
  border: 3px solid var(--color-primary);
  border-radius: 8px;
}

.error {
  color: red;
}
</style>
