<!-- eslint-disable vue/multi-word-component-names -->
<script setup>
import Recommendation from "./Recommendation.vue";
</script>

<template lang="">
  <div class="dashboard-container">
    <div class="dashboard-aside">
      <nav></nav>
    </div>
    <div class="dashboard-content">
      <h1>Dashboard</h1>
      <p>
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Doloribus
        explicabo corporis maiores repudiandae praesentium aliquam, omnis nisi!
        Non ea, ab itaque, modi enim cum natus architecto at, iure facere
        dolorum?
      </p>
    </div>
  </div>
  <div class="search-container">
    <form action="" class="search-content">
      <input class="search-bar" type="text" v-model="search" placeholder="Search For Items" />
      <button type="submit" class="search-button"> <img src="../assets/search.png" class="my-icon">  </button>

    </form>
    </div>

  <div class="recommendations-container">
    <div class="recommendations-content">
      <div class="recommendations-header">
        <h2> Recommended Items</h2>
      </div>
      <div class="recommendations-item-container">
        <Recommendation ItemImage="../assets/defaultPicRec.png" ItemName="Default Laptop"/>
      </div>
      <div class="recommendations-item-container">
        <Recommendation ItemImage="../assets/defaultPicRec.png" ItemName="Default Laptop"/>
      </div>
      <div class="recommendations-item-container">
        <Recommendation ItemImage="../assets/defaultPicRec.png" ItemName="Default Laptop"/>
      </div>
      <div class="recommendations-item-container">
        <Recommendation ItemImage="../assets/defaultPicRec.png" ItemName="Default Laptop"/>
      </div>
      <div class="recommendations-item-container">
        <Recommendation ItemImage="../assets/defaultPicRec.png" ItemName="Default Laptop"/>
      </div>
      <div class="recommendations-item-container">
        <Recommendation ItemImage="../assets/defaultPicRec.png" ItemName="Default Laptop"/>
      </div>
    </div>


  </div>
</template>

<script >
export default {
  data() {
    return {
      search: ''
    }
  }
};
</script>

<style scoped>
.dashboard-container {
  display: flex;
  justify-content: space-between;
  width: 85%;
}
.dashboard-aside {
  top: 120px;
  width: 15%;
  height: 100%;
  border: 1px solid var(--color-text);
  padding: 4rem 4rem;
  border-radius: 5px;
  background: var(--color-highlight);
  margin-right: 20px;
}
.dashboard-content {
  top: 120px;
  width: 85%;
  height: 100%;
  border: 1px solid var(--color-text);
  padding: 4rem 4rem;
  border-radius: 5px;
  background: var(--color-highlight);
}
.recommendations-container {
  display: flex;
  justify-content: space-between;
  width: 91%;
  top: 140px;
  align-items: left;
  position: relative;
}
.recommendations-content {
  top: 0px;
  width: 91%;
  height: 70%;
  left: 15%;
  border: 1px solid var(--color-text);
  padding: 4rem 4rem;
  border-radius: 5px;
  background: var(--color-highlight);
  display: flex;
}
.recommendations-item-container
{
  position: relative;
  width: 100%;
  left: 0%;
  display: flex;
  justify-content: left;
  align-items: left;
  flex-wrap: wrap;
  padding: 5px;
  margin-top: 8%;
}
.recommendations-header
{
  position:relative;
  align-self: flex-start;
  display: flex;
  left: 5%;
  white-space: nowrap;
}
.search-container {
  display: flex;
  justify-content: space-between;
  width: 85%;
  background-position: center;
  background-size: cover;
  align-items: center;
  justify-content: center;
  left: 220px;
  top: 130px;
}
.search-content{
  width: 100%;
  display:flex;
  align-items: center;
  border-radius: 60px;
  padding: 10 px 20px;

}
.my-icon {
    width: 30px;
    height: 30px;
}
.search-bar {
    width: 100%;
    max-width: 700px;
    height: 50px;
    background: transparent;
    outline: none;
    font-size: 20px;
    display: flex;
    align-items: center;
    border-radius: 60px;
}
.search-button
{
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  background: transparent;
  right: 60px;
}





</style>
