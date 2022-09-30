<script setup>
import { RouterLink, RouterView } from "vue-router";
import LogoLink from "./components/LogoLink.vue";
</script>

<template>
  <header>
    <div class="wrapper">
      <LogoLink msg="<TechRent>" />
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
        <RouterLink to="/register">Register</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView id="content" />
</template>

<style scoped>
#content {
}

header {
  width: 100%;
  position: fixed;
  top: 0;
  padding: 10px;
  background-color: grey;
  line-height: 1.5;
  max-height: 100vh;
}

nav {
  z-index: 1000;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    justify-content: space-around;
  }

  header .wrapper {
    width: 80%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
