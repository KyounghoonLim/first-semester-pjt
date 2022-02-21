<template>
  <div @click="goDetail" class="profile-other-card">
    <img :src="thumbnailSrc" :alt="article.title">
    <hr>
    <h3>{{ article.title | truncate(10) }}</h3>
    <p>{{ article.updated_at | dateTime }}</p>
  </div>
</template>

<script>
export default {
  props: {
    article: Object
  },
  methods: {
    goDetail: function () {
      this.$router.push({name: 'Community_Detail', params: {articleId: this.article.id}})
    }
  },
  filters: {
    truncate: function(target ,num){
      if (target.length > num){
        return target.slice(0, num) + '...'
      }
      return target
    },
    dateTime: function(target){
      const date = new Date(target)
      return date.toLocaleString()
    },
  },
  computed: {
    thumbnailSrc: function(){
      if (this.article.thumbnail){
        return 'http://localhost:8000' + this.article.thumbnail
      }
      else {
        return require('@/assets/photo.png')
      }
    }
  },
}
</script>

<style>
  .profile-other-card {
    cursor: pointer;
    display: flex;
    flex-direction: column;
    background: white;
    margin: 1rem;
    width: 20vw;
    height: 40vh;
    overflow: hidden;
    border: none;
    border-radius: 1rem;
  }

  .profile-other-card > img {
    height: 70%;
    background-color: rgb(126, 126, 126, 0.75);
  }

  .profile-other-card > h3 {
    display: flex;
    margin: 0.1rem auto;
  }

  .profile-other-card > p {
    font-size: 0.75rem;
  }
</style>