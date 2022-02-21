<template>
  <div @mouseover="hover" @mouseout="hover" @click="check" class="card">
    <img :src="posterPath" :alt="moviechoice.title">
    <span id="card-choice" v-show="checked">
      <img v-show="checked" :src="require('@/assets/checked.png')" alt="checked">
    </span>
    <span id="card-hover" v-show="show">
      <h2>{{ moviechoice.title }}</h2>
      <p>{{ moviechoice.overview | truncate(300) }}</p>
    </span>
  </div>
</template>

<script>
export default {
  data: function(){
    return {
      show: false,
      checked: false
    }
  },
  props: {
    moviechoice: Object
  },
  methods: {
    hover: function(){
      if (!this.checked){
        this.show = !this.show
      }
    },
    check: function(){
      this.checked = !this.checked
      this.show = !this.show
      if (this.checked){
        this.$emit('check-movie', this.moviechoice.id)
      }
      else {
        this.$emit('remove-movie', this.moviechoice.id)
      }
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
      if (this.moviechoice.poster_path){
        return 'https://image.tmdb.org/t/p/original/' + this.moviechoice.poster_path
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
    position: relative;
    width: 20vw;
    height: 30vw;
    cursor: pointer;
    margin: 1rem;
    overflow: hidden;
  }

  .card img {
    width: 100%;
    height: 100%;
  }

  #card-choice {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: absolute;
    background-color: rgb(0, 0, 0, 0.5);
    color: rgb(255, 255, 255, 0.75);
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    font-size: 5rem;
    font-weight: lighter;
  }

  #card-choice img {
    width: 200%;
    height: 150%;
  }

  #card-hover {
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
  }

  .card p {
    word-break:keep-all;
    padding: 1rem;
    margin: 0;
  }
</style>