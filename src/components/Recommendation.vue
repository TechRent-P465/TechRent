<script setup>
defineProps({
  ItemImage: {
    type: Image,
    required: true,
  },
  ItemName: {
    type: String,
    required: true,
  },
});
</script>

<template lang="">
<div class="recommendations-card">
    <img src={{ItemImage}} alt="item image" id="itemId" />
    <p> {{ItemName}}</p>
    <nav></nav>
</div>
</template>

<style scoped>

.recommendations-card
{
  width: 200px;
  position:relative;
  height: 200px;
  background: var(--color-highlight);
  margin: 10px 5px;
  padding: 20px 15px;
  display: flex;
  box-shadow: 0.5px 10px;
  transition: 0.3s ease-in-out;
  margin-top: 5%;
  flex-direction: column;
  right: 130%;
}

</style>

