<template>
  <div id="signup">
    <h1>Sign up</h1>
    <div class="signup-container">
      <form @submit.prevent="submit">
        <input v-model="username" type="text" placeholder="username">
        <input v-model="password" type="password" placeholder="password">
        <input v-model="passwordConfirmation" type="password" placeholder="password confirmation">
        <button>Sign up</button>
      </form>
    </div>
    <button @click="goLogin" class="login-button">Login</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: function(){
    return {
      username: null,
      password: null,
      passwordConfirmation: null
    }
  },
  methods: {
    submit: function(){
      axios({
        method: 'post',
        url: 'http://localhost:8000/accounts/signup/',
        data: {
          username: this.username, password: this.password,
          passwordConfirmation: this.passwordConfirmation
        }
      })
      .then(() => {
        alert('가입이 완료 되었습니다.')
        this.$router.push({ name: 'Login' })
      })
      .catch(error => {
        console.log(error)
        alert('아이디 혹은 비밀번호가 잘못되었습니다.')
        this.username = null; this.password = null;
        this.passwordConfirmation = null
      })
    },
    goLogin: function () {
      this.$router.push({name:'Login'})
    }
  }
}
</script>

<style>
  #signup {
    width: 30vw;
    background: white;
    margin: 3rem auto;
    padding: 2rem;
    border-radius: 2rem;
  }

  #signup h1 {
    color: rgb(211, 88, 88);
  }

  .signup-container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .signup-container button {
    cursor: pointer;
    display: block;
    background-color: rgb(211, 88, 88);
    border-radius: 0.5rem;
    margin: 2rem auto;
    padding: 0.5rem 3rem;
    font-size: 1rem;
    font-weight: bold;
  }

  .signup-container input {
    display: block;
    margin: 15px;
    height: 2rem;
    background-color: rgb(126, 126, 126, 0.2);
    border: none;
    padding: 0 0 0 1rem;
  }

  .login-button{
    cursor: pointer;
    display: block;
    background-color: rgb(22, 165, 117);
    border-radius: 0.5rem;
    margin: 0 auto;
    padding: 0.5rem 3.5rem;
    font-size: 1rem;
    font-weight: bold;
  }
</style>