<!-- eslint-disable vue/multi-word-component-names -->
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
</template>
<script>
export default {};
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
</style>
