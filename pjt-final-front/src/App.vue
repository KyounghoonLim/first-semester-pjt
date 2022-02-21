<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'Main' }" id="nav-main">
        <img src="@/assets/film.png" alt="logo">
      </router-link>
      <span v-if="!isAuthenticated" id="nav-route">
        <router-link :to="{ name: 'Signup' }">Sign Up</router-link>
        <router-link :to="{ name: 'Login' }">Log In</router-link>
      </span>
      <span v-if="isAuthenticated" id="nav-route">
        <router-link :to="{ name: 'Community' }"><img src="@/assets/bubble-chat.png" alt="community"></router-link>
        <a @click="profile = !profile"><img src="@/assets/profile.png" alt="profile"></a>
      </span>
      <transition name="slide">
        <profile v-show="profile" @profile-hide="profile = !profile"></profile>
      </transition>
    </nav>
    <router-view/>
    <footer>
      <p>movie project name is Shroom. developed by SH, KH</p>
    </footer>
  </div>
</template>

<script>
import Profile from "@/components/accounts/profile/Profile";

export default {
  data: function(){
    return {
      profile: false,
      isAuthenticated: false
    }
  },
  components : {
    Profile
  },
  created: function(){
    this.isAuthenticated = localStorage.getItem('jwt')
    if (!this.isAuthenticated){
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    min-height: 100vh;
    height: 100%;
    background: url('../src/assets/velvet-4.png');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: space-between;
  }

  nav {
    position: sticky;
    top: 0%;
    z-index: 9999;
  }

  #nav-main {
    display: flex;
    align-items: center;
    margin: 0.5rem;
  }

  #nav-main h1 {
    margin: 0 0.5rem;
    color: #42b983;
  }

  #nav-route {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  #nav-route img {
    width: 2rem;
    height: 2rem;
    margin: 0;
  }

  nav {
    padding: 10px;
    display: flex;
    justify-content: space-between;
    background-color: #f6f5ef;
  }

  nav a {
    font-weight: bold;
    color: #2c3e50;
    text-decoration: none;
    cursor: pointer;
    margin: 0.5rem 2rem;
  }

  nav a.router-link-exact-active {
    color: #42b983;
  }

  nav img {
    width: 3rem;
    height: 3rem;
  }

  button {
    border: none;
    background-color: royalblue;
    color: white;
    cursor: pointer;
  }

  @keyframes slide {
    from { right: -100% }
    to { right: 0 }
  }

  .slide-enter-active {
    animation: slide 1s ease-out;
  }

  .slide-leave-active {
    animation: slide 1s ease-out reverse;
  }

  footer {
    height: 3rem;
    background-color: rgb(0, 0, 0, 0.5);
    color: white;
    font-size: 0.8rem;
    font-weight: lighter;
    display: flex;
    justify-content: center;
    align-items: center;
    position: sticky;
    bottom: 0;
  }
</style>
