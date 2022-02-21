<template>
  <div v-if="review" id="review">
    <img @click="goToProfile" class="profile" id="profile-image" :src="profileSrc" alt="">
    <h3 @click="goToProfile" class="profile">{{ review.user.username }}</h3>
    <p>{{ review.content }}</p>
    <p id="score">{{ review.score }}</p>
  </div>  
</template>

<script>

export default {
  data: function () {
    return {
    }
  },
  props: {
    review: Object,
  },
  methods: {
    goToProfile: function(){
      this.$router.push({ name: 'ProfileOther', params: { username: this.review.user.username}})
    }
  },
  computed: {
    profileSrc: function(){
      if (this.review.user.profile_img){
        return 'http://localhost:8000/' + this.review.user.profile_img
      }
      return require('@/assets/profile.png')
    },
  }
}
</script>

<style scoped>
  #review {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
    border-bottom: 4px gray solid;
    margin: 0.25rem;
    padding: 0 1rem;
    align-self: stretch;
    position: relative;
  }

  #review * {
    margin: 1rem 0.5rem;
    color: white;
  }

  #profile-image {
    width: 4%;
    border: 2px rgb(187, 187, 187) solid;
    border-radius: 50%;
    background-color: rgb(207, 207, 207);
  }

  #review div {
    display: flex;
    position: absolute;
    left: 90%;
  }

  #review div img {
    width: 4%;
  }

  .profile {
    cursor: pointer;
  }

  #score {
    margin-left: auto;
  }
</style>