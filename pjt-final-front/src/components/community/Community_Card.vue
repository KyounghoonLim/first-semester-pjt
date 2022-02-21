<template>
  <div v-if="article" class="community-card">
    <img @click="goToDetail" :src="thumbnailSrc" :alt="article.title">
    <h2>{{ article.title | truncate(10) }}</h2>
    <hr>
    <span id="card-profile">
      <img @click="goToDetailProfile" id="profile-image" :src="profileSrc" alt="">
      <h5 @click="goToDetailProfile">{{ article.user.username }}</h5>
    </span>
    <p>{{ article.updated_at | dateTime }}</p>
    <button @click="goToDetail">Detail</button>
  </div>
</template>

<script>
export default {
  props: {
    article: Object
  },
  methods: {
    goToDetail: function(){
      this.$router.push({ name: 'Community_Detail', params: { articleId: this.article.id }})
    },
    goToDetailProfile: function(){
      this.$router.push({ name: 'ProfileOther', params: { username: this.article.user.username}})
    }
  },
  computed: {
    thumbnailSrc: function(){
      if (this.article.thumbnail){
        return 'http://localhost:8000' + this.article.thumbnail
      }
      else {
        return require('@/assets/photo.png')
      }
    },
    profileSrc: function(){
      if (this.article.user.profile_img){
        return 'http://localhost:8000/' + this.article.user.profile_img
      }
      return require('@/assets/profile.png')
    },
  },
  filters: {
    dateTime: function(target){
      const date = new Date(target)
      return date.toLocaleString()
    },
    truncate: function(target ,num){
      if (target.length > num){
        return target.slice(0, num) + '...'
      }
      return target
    }
  }
}
</script>

<style scoped>
  #card-profile {
    display: flex;
    justify-content: center;
    cursor: pointer;
    z-index: 1;
  }
  
  .community-card{
    display: flex;
    flex-direction: column;
    justify-content: center;
    overflow: hidden;
    background-color: white;
    border: none;
    border-radius: 2rem;
    position: relative;
    width: 20vw;
    height: 30vw;
    margin: 1.2rem;
    /* overflow: hidden; */
  }

  .community-card > img {
    width: auto;
    height: 50%;
    background-color: rgb(126, 126, 126, 0.75);
    margin: 0;
    cursor: pointer;
  }

  .community-card h2, p {
    margin: 0.5rem;
  }

  .community-card hr {
    width: 80%;
  }

  button {
    cursor: pointer;
    display: block;
    background-color: rgb(22, 165, 117);
    /* border: none; */
    border-radius: 0.5rem;
    margin: 1rem auto 2rem;
    padding: 0.5rem 2rem;
    font-size: 1.25rem;
    font-weight: bold;
    /* opacity: 75%; */
  }

  h4 {
    margin: 0.5rem;
  }

  p {
    font-size: 0.75rem;
  }

  #profile-image {
    width: 10%;
    aspect-ratio: 1 / 1;
    border: 2px rgb(187, 187, 187) solid;
    border-radius: 50%;
    background-color: rgb(207, 207, 207);
    margin: 1rem;
  }
</style>