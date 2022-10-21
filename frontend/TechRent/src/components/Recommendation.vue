<script setup>
defineProps({
  ItemImage: {
    type: String,
    default: '../assets/defaultPicRec.png'
  },
  ItemName: {
    type: String,
    required: true
  }
})
</script>

<template lang="">
  <a class="recommendations-card">
    <img :src="ItemImage" alt="item image" id="itemId" />
    <p>{{ ItemName }}</p>
    <nav></nav>
  </a>
</template>

<style scoped>
.recommendations-card {
  width: 200px;
  height: 200px;
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
  height: 195px;
  margin-right: 5px;
}

a {
  color: var(--color-primary);
}
</style>
