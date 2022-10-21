<template>
  <header>
    <div class="wrapper">
      <LogoLink msg="<TechRent>" />
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/login">Login</router-link>
      </nav>
    </div>
  </header>
  <div class="content-wrapper">
    <router-view id="content" />
  </div>
  <footer>
    <h1>Contact</h1>
    <ul>
      <li>email: TechRent@gmail.com</li>
      <li>317-123-1234</li>
    </ul>
    <h2>GitHub: <a href="https://github.com/cam-line/TechRent">TechRent</a></h2>
  </footer>
</template>

<script>
//import { RouterLink, RouterView } from "vue-router";
import LogoLink from '@/components/LogoLink.vue'

export default {
  components: {
    LogoLink
  }
}
</script>

<style scoped>
@import './assets/normalize.css';
.content-wrapper {
  min-height: 100%;
}

#content {
  margin: 0 auto;
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

@media (min-width: 1024px) {
  header .wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  header {
    position: fixed;
    z-index: 9999999;
    width: 100%;
    height: 108px;
    background: var(--color-secondary);
    border-bottom: 5px solid var(--color-pop);
    -webkit-box-shadow: 0 3px 5px rgba(57, 63, 72, 0.3);
    -moz-box-shadow: 0 3px 5px rgba(57, 63, 72, 0.3);
    box-shadow: 0 3px 5px rgba(57, 63, 72, 0.3);
    padding: 20px 50px;
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
