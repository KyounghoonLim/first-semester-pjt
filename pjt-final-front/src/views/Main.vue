<template>
  <div v-if="movies" id="main">
    <h1 class="main-title" v-if="page == 0">평점순 영화</h1>
    <h1 class="main-title" v-if="page == 1">추천 장르 영화</h1>
    <h1 class="main-title" v-if="page == 2">최신 개봉 영화</h1>
    <div id="carousel">
      <carousel3d :autoplay="true" :autoplayHoverPause="true" :space="400"
      :controls-visible="true">
        <slide v-for="(movie, idx) of movies" :key="movie.id" :index="idx">
          <moviecard :movie="movie"></moviecard>
        </slide>
      </carousel3d>
      <img @click="setMovies(page)" class="change-button" :src="require('@/assets/up-arrow.png')" alt="change">
    </div>
  </div>
</template>

<script>
import Moviecard from '@/components/movies/Moviecard'
import { Carousel3d, Slide } from 'vue-carousel-3d';
import axios from 'axios';

export default {
  data: function(){
    return {
      movies: null,
      cnt: 0
    }
  },
	components: {
		Moviecard,
    Carousel3d,
    Slide
	},
  methods: {
    setMovies: function(p){
      axios({
      method: 'get',
      url: 'http://localhost:8000/movies/?page=' + p,
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
    })
    .then(response => {
      console.log(response)
      this.movies = response.data
      this.cnt += 1
    })
    .catch(() => console.log(`http://localhost:8000/movies/?page=${ this.page }`))
    }
  },
  computed: {
    page: function(){
      return this.cnt % 3
    }
  },
  beforeCreate: function(){
    axios({
      method: 'get',
      url: `http://localhost:8000/movies/?page=0`,
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
    })
    .then(response => {
      console.log(response)
      this.movies = response.data
      this.cnt += 1
    })
    .catch(() => console.log(`http://localhost:8000/movies/?page=${ this.page }`))
  }
}
</script>

<style>
  #main {
    margin: 0 5rem;
    padding: 1rem;
  }

  #carousel {
    display: flex;
    height: 70vh;
    position: relative;
    justify-content: center;
    margin-bottom: 2rem;
  }

  .change-button {
    margin: 1rem auto;
    padding: 0.5rem 2rem;
    cursor: pointer;
    height: 40px;
    position: absolute;
    top: 90%;
  }

  .carousel-3d-container {
    width: 100% !important;
    height: 90% !important;
    overflow: auto;
  }

  .carousel-3d-slide {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    overflow: visible;
    background: none;
    border: none;
    height: auto !important;
  }

  .main-title {
    color: white;
  }

  .carousel-3d-controls[data-v-05517ad0] {
    position: absolute;
    top: 80%;
  }

  .carousel-3d-controls span {
    color: white;
    font-size: 5rem;
  }

  #loader {
    width: 100vw;
    height: 100vh;
    background-color: rgb(0, 0, 0, 0.5);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #loader img {
    /* width: 30; */
  }
</style>