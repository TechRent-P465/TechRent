<template lang="">
  <a class="recommendations-card" @click="routeToItem">
    <!-- <div id="image"></div> -->
    <img src="../assets/defaultPicRec.png" alt="item image" id="itemId" />
    <h2>{{ itemName }}</h2>
    <div class="type-and-price">
      <p>{{ itemType }}</p>
      <p>${{ itemPrice }}</p>
    </div>
    <nav></nav>
  </a>
</template>
<script>
import { integer } from '@vuelidate/validators'

export default {
  name: 'purchaseItem',
  data() {
    return {}
  },
  methods: {
    routeToItem() {
      this.$router.push(`/itempage/${this.id}`)
    }
  },
  props: {
    itemImage: {
      type: String,
      default: '../assets/defaultPicRec.png'
    },
    itemName: {
      type: String,
      required: true
    },
    id: Number,
    itemType: String,
    itemBrand: String,
    itemLocation: String,
    itemPrice: String
  }
}
</script>
<style scoped>
.recommendations-card {
  width: 200px;
  height: 240px;
  background: var(--color-highlight);
  padding: 20px 15px;
  border: 5px solid var(--color-tertiary);
  -webkit-box-shadow: 0 3px 5px rgba(57, 63, 72, 0.3);
  -moz-box-shadow: 0 3px 5px rgba(57, 63, 72, 0.3);
  box-shadow: 0 3px 5px rgba(57, 63, 72, 0.3);
  display: flex;
  flex-direction: column;
}
.recommendations-card:hover {
  color: var(--color-tertiary);
  background-color: var(--color-highlight);
  box-shadow: inset 0 0 0 2000px rgba(62, 124, 177, 0.2);
  width: 195px;
  height: 235px;
  margin-right: 5px;
}

a {
  color: var(--color-primary);
}

#image {
  background-image: url('../assets/defaultPicRec.png');
  width: 100%;
}

.type-and-price {
  display: flex;
  justify-content: space-between;
}
</style>
