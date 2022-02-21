<template>
  <div v-if="movies" id="choice-movies">
    <h1>관심있는 영화를 선택해주세요</h1>
    <h4>선택한 영화를 기준으로 추천해드릴게요! 😎</h4>
    <div id="choice-container">
      <span v-for="movie of pagenatedMovie" :key="movie.id">
        <choice-moviecard :moviechoice="movie" @check-movie="checkMovie" @remove-movie="removeMovie"/>
      </span>
    </div>
    <button @click="setUserGenres" id="choice-button" :class="{ 'twinkle' : checked.length > 0 }">send</button>
  </div>
</template>

<script>
import ChoiceMoviecard from '@/components/movies/ChoiceMoviecard';
import axios from 'axios';


export default {
  data: function(){
    return {
      movies: null,
      pagination: 1,
      checked: []
    }
  },
  components: {
    ChoiceMoviecard
  },
  methods: {
    checkMovie: function(idx){
      this.checked.push(idx)
    },
    removeMovie: function(idx){
      const indexNum = this.checked.findIndex(element => element === idx)
      this.checked.splice(indexNum, 1)
    },
    setUserGenres: function(){
      if (this.checked.length == 0){
        return alert('영화를 선택해주세요!')
      }
      axios({
        method: 'put',
        url: 'http://localhost:8000/accounts/profile/',
        data: {
          like_movies: this.checked
        },
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
      .then(response => {
        console.log(response)
        this.$router.push({ name: 'Main' })
      })
    }
  },
  computed: {
    pagenatedMovie: function(){
      return this.movies.slice(0, this.pagination * 8)
    }
  },
  beforeCreate: function(){
    axios({
      method: 'get',
      url: 'http://localhost:8000/movies/?page=3',
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
    })
    .then(response => {
      console.log(response)
      this.movies = response.data
    })
  },
  mounted: function(){
    document.addEventListener('scroll', () => {
      const {scrollHeight, scrollTop, clientHeight} = document.documentElement
      if (scrollHeight - Math.round(scrollTop) === clientHeight && this.pagination < 5){
        this.pagination += 1
      }
    })
  }
}
</script>

<style>
  #choice-movies {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 1rem;
    height: 100%;
    background-color: black;
    color: rgb(255, 255, 255);
  }

  #choice-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }

  #choice-button {
    position: sticky;
    bottom: 8%;
    left: 100%;
    cursor: pointer;
    display: block;
    background-color: rgb(22, 165, 117);
    border: none;
    border-radius: 1rem;
    margin: 3rem auto 1rem;
    padding: 0.5rem 2rem;
    font-size: 1.25rem;
    font-weight: bold;
  }

  @keyframes twinkle {
    from {
      background-color: white;
      color: rgb(22, 165, 117);
    }
    to {
      background-color: rgb(22, 165, 117);
      color: white;
    }
  }

  .twinkle {
    animation: twinkle 0.75s ease-in-out 1s infinite alternate;
  }
</style>