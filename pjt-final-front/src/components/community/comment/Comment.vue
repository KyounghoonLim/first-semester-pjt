<template>
  <div v-if="comment" id="comment">
    <img @click="goToDetail" class="profile" id="profile-image" :src="profileSrc" alt="">
    <h5 @click="goToDetail" class="profile">{{ comment.user.username }}</h5>
    <p>{{ comment.content }}</p>
    <div>
      <img :class="{ 'on-like': liked }" :src="require('@/assets/like.png')" alt="">
      <h5>{{ comment.like_users.length }}</h5>
    </div>
  </div>  
</template>

<script>

export default {
  data: function () {
    return {
    }
  },
  props: {
    comment: Object,
    articleId: Number
  },
  methods: {
    like: function () {

    },
    goToDetail: function(){
      this.$router.push({ name: 'ProfileOther', params: { username: this.comment.user.username}})
    }
  },
  computed: {
    profileSrc: function(){
      if (this.comment.user.profile_img){
        return 'http://localhost:8000/' + this.comment.user.profile_img
      }
      return require('@/assets/profile.png')
    },
    // liked: function(){
    //   if (this.article.like_users.find(ele => ele == this.$store.state.user.id)){
    //     return true
    //   }
    //   return false
    // }
  }
}
</script>

<style scoped>
  #comment {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    background-color: rgb(128, 128, 128, 0.5);
    border-radius: 10px;
    border-bottom: 4px gray solid;
    margin: 0.25rem;
    padding: 0 1rem;
    align-self: stretch;
    position: relative;
  }

  #comment * {
    margin: 1rem 0.5rem;
  }

  #profile-image {
    width: 4%;
    border: 2px rgb(187, 187, 187) solid;
    border-radius: 50%;
    background-color: rgb(207, 207, 207);
  }

  #comment div {
    display: flex;
    position: absolute;
    left: 90%;
  }

  #comment div img {
    width: 4%;
  }

  .on-like {
    color: red;
  }

  .profile {
    cursor: pointer;
  }
</style>