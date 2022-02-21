<template>
  <div id="login">
    <h1>Login</h1>
    <div class="login-container">
      <form @submit.prevent="login">
        <input type="text" placeholder="username">
        <input type="password" placeholder="password">
        <button>Login</button>
      </form>
    </div>
    <button @click="goSignup" class="signup-button">Sign up</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    login: function(event){
      if (!event.target[0].value){
        return alert('아이디를 입력해주세요!')
      }
      else if (!event.target[1].value){
        return alert('비밀번호를 입력해주세요!')
      }
      axios({
        method: 'post',
        url: 'http://localhost:8000/accounts/api-token-auth/',
        data: {
          username: event.target[0].value,
          password: event.target[1].value
        }
      })
      .then(response => {
        localStorage.setItem('jwt', response.data.token)
        location.reload()
        this.$router.push({ name: 'Main' })
      })
      .catch(() => alert('아이디 혹은 비밀번호가 틀렸습니다.'))
        
      event.target.reset()
    },
    goSignup: function () {
      this.$router.push({name:'Signup'})
    }
  }
}
</script>

<style>
  #login {
    width: 30vw;
    background-color: white;
    margin: auto;
    padding: 2rem;
    border-radius: 2rem;
  }

  #login h1 {
    color: rgb(22, 165, 117);
  }

  .login-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }


  .login-container button {
    cursor: pointer;
    display: block;
    background-color: rgb(22, 165, 117);
    border-radius: 0.5rem;
    margin: 2rem auto;
    padding: 0.5rem 3rem;
    font-size: 1rem;
    font-weight: bold;
  }

  .login-container input {
    display: block;
    margin: 15px;
    height: 2rem;
    background-color: rgb(126, 126, 126, 0.2);
    border: none;
    padding: 0 0 0 1rem;
  }

  .signup-button {
    cursor: pointer;
    display: block;
    background-color: rgb(211, 88, 88);
    border-radius: 0.5rem;
    margin: 0 auto;
    padding: 0.5rem 2.5rem;
    font-size: 1rem;
    font-weight: bold;
  }
</style>