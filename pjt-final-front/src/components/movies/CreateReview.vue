<template>
  <div id="create-review">
    <h1>이 영화는 어떠셨나요? 🤔</h1>
    <div class="create-review-container">
      <form @submit.prevent="createReview">
        <select>
          <option value="1">⭐️</option>
          <option value="2">⭐️x2</option>
          <option value="3">⭐️x3</option>
          <option value="4">⭐️x4</option>
          <option value="5">⭐️x5</option>
          <option value="6">⭐️x6</option>
          <option value="7">⭐️x7</option>
          <option value="8">⭐️x8</option>
          <option value="9">⭐️x9</option>
          <option value="10" selected>⭐️x10</option>
        </select>
        <input type="text" placeholder="여기에 작성해주세요.">
        <button>send</button>
      </form>
    </div>
    <button @click="cancel" class="cancel-button">cancel</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    isActive: Boolean,
    movie: Object
  },
  methods: {
    createReview: function(event){
      console.log(event)
      axios({
        method: 'post',
        url: `http://localhost:8000/movies/review/${ this.movie.id }/`,
        data: {
          content: event.target[1].value,
          score: event.target[0].value
        },
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
      .then(response => {
        console.log(response)
        alert('작성되었습니다☺️')
        this.$emit('review-created', response.data)
      })
      .catch(() => console.log('error!'))
    },
    cancel: function(){
      this.$emit('cancel')
    }
  }
}
</script>

<style scoped>
  #create-review {
    width: 50%;
    background-color: rgb(255, 255, 255);
    margin: auto;
    padding: 2rem;
    border-radius: 2rem;
    position: fixed;
    top: 30%;
    left: 23%;
  }

  #create-review h1 {
    color: rgb(22, 165, 117);
  }

  .create-review-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }


  .create-review-container button {
    cursor: pointer;
    display: block;
    background-color: rgb(22, 165, 117);
    border-radius: 0.5rem;
    margin: 2rem auto;
    padding: 0.5rem 3rem;
    font-size: 1rem;
    font-weight: bold;
  }

  .create-review-container input {
    display: block;
    margin: 15px;
    height: 2rem;
    width: 20rem;
    background-color: rgb(126, 126, 126, 0.2);
    border: none;
    border-radius: 5px;
    padding: 0 0 0 1rem;
  }

  .cancel-button {
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