<template>
  <div v-if="movie" id="detail" :class="{ 'activated': isActive }">
    <div id="detail-container">
      <img id="detail-poster" :src="'https://image.tmdb.org/t/p/original/' + this.movie.poster_path"
      :alt="movie.title" @click="showInfo = !showInfo">
      <transition name="info">
      <span v-show="showInfo" id="movie-info" @click="showInfo = !showInfo">
        <h1>{{ movie.title }}</h1>
        <div id="detail-genres">
          <h2 v-for="genre of movie.genres" :key="genre.id">{{ genre.name }}</h2>
        </div>
        <h2>평점: {{ movie.vote_average }}</h2>
        <h4>개봉일: {{ movie.release_date }}</h4>
        <p>{{ movie.overview }}</p>
      </span>
      </transition>
    </div>
    <button id="create-review-btn" @click="isActive = true">리뷰 작성</button>
    <create-review v-if="isActive" @cancel="isActive = false" @review-created="updateDetail"
     :isActive="isActive" :movie="movie" />
     <div>
       <review v-for="review of movie.review_set" :key="review.id" :review="review" />
     </div>
  </div>
</template>

<script>
import createReview from '@/components/movies/CreateReview';
import Review from '@/components/movies/Review';
import axios from "axios"

export default {
  data: function(){
    return {
      movie: null,
      showInfo: false,
      isActive: false
    }
  },
  components: {
    createReview,
    Review
  },
  methods: {
    updateDetail: function(data){
      this.isActive = false
      this.movie = data
    }
  },
  beforeCreate: function(){
    axios({
      method: 'get',
      url: 'http://localhost:8000/movies/detail/' + this.$route.params.movieId,
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
    })
    .then(response => {
      this.movie = response.data
    })
    .catch(() => console.log('fail...'))
  }
}
</script>

<style scoped>
  #detail {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    z-index: 1;
  }

  #detail-container {
    margin-top: 3rem;
    display: flex;
    justify-content: center;
  }

  #detail-poster {
    width: 30%;
    height: 40%;
    border-radius: 2rem;
    cursor: pointer;
  }

  #movie-info {
    width: 30%;
    height: 40%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    background-color: rgb(0, 0, 0, 0.5);
    padding: 1rem;
    margin-left: 2rem;
    overflow: scroll;
    cursor: pointer;
  }

  #movie-info * {
    margin: 0.5rem;
    color: white;
  }

  @keyframes info {
    from { width: 0; }
    to { width: 25vw; }
  }

  .info-enter-active {
    animation: info 0.5s ease-out;
  }

  .info-leave-active {
    animation: info 0.5s ease-out reverse;
  }

  .activated {
    background-color: rgb(0, 0, 0, 0.3);
  }

  #create-review-btn {
    /* position: absolute;
    bottom: -10%;
    left: 45%; */
    background-color: rgb(22, 165, 117);
    padding: 0.5rem;
    width: 10%;
    font-size: 1rem;
    font-weight: bold;
    border-radius: 10px;
    margin: 2rem;
  }

  #detail-genres {
    display: flex;
    justify-content: center;
  }
</style>