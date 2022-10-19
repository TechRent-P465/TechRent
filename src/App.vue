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
      </nav>
    </div>
  </header>
  <div class="content-wrapper">
    <RouterView id="content" />
  </div>
  <footer></footer>
</template>

<style scoped>
.content-wrapper {
  min-height: 100%;
}

#content {
  margin: 0 auto;
}

header {
  z-index: 1000;
  width: 100%;
  position: fixed;
  top: 0;
  padding: 10px;
  background-color: var(--color-secondary);
  line-height: 1.5;
  max-height: 100vh;
  border-bottom: 5px solid var(--color-heading);
}

nav {
  font-size: 12px;
  text-align: center;
  justify-content: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-background);
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

footer {
  background-color: var(--color-heading);
  height: 50px;
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
