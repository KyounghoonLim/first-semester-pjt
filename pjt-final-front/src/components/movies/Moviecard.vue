<template>
  <div @mouseover="hover" @mouseout="hover" @click="goToDetail" class="card">
    <img :src="posterPath" :alt="movie.title">
    <span v-show="show">
      <h2>{{ movie.title }}</h2>
      <div id="movie-card-genres">
        <h3 v-for="genre of movie.genres" :key="genre.id">{{ genre.name }}&nbsp;</h3>
      </div>
      <p>{{ movie.overview | truncate(180) }}</p>
    </span>
  </div>
</template>

<script>
export default {
  data: function(){
    return {
      show: false
    }
  },
  props: {
    movie: Object
  },
  methods: {
    hover: function(){
      this.show = !this.show
    },
    goToDetail: function(){
      this.$router.push({name: 'Detail', params: { movieId: this.movie.id }})
    }
  },
  filters: {
    truncate: function(target ,num){
      if (target.length > num){
        return target.slice(0, num) + '...'
      }
      return target
    }
  },
  computed: {
    posterPath: function(){
      if (this.movie.poster_path){
        return 'https://image.tmdb.org/t/p/original/' + this.movie.poster_path
      }
      else {
        return '@/assets/photo.png'
      }
    }
  }
}
</script>

<style>
  .card {
    border: none;
    border-radius: 1rem;
    background-color: blanchedalmond;
    position: relative;
    width: 100%;
    height: 100%;
    cursor: pointer;
    margin: 1rem;
    box-shadow: rgb(0, 0, 0, 0.5) 1rem 1rem 1rem 0.5rem;
  }

  .card img {
    width: 100%;
    height: 110%;
  }

  .card span {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: absolute;
    background-color: rgb(0, 0, 0, 0.5);
    color: white;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }

  .card h2 {
    margin-bottom: 0;
    word-break: keep-all;
    text-align: center;
  }

  .card p {
    word-break:keep-all;
    padding: 1rem;
    margin: 0;
  }

  #movie-card-genres {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }
</style>