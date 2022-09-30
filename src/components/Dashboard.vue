<!-- eslint-disable vue/multi-word-component-names -->
<template lang="">
  <div class="dashboard-container">
    <div class="dashboard-content">
      <h1>Dashboard</h1>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
.dashboard-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.dashboard-content {
  position: absolute;
  top: 200px;
  width: 80%;
  height: 100%;
  border: 1px solid lightgray;
  padding: 4rem 4rem;
  border-radius: 5px;
  background: black;
}
</style>
