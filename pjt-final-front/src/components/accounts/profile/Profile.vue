<template>
  <div v-if="user" id="profile">
    <h2>Profile</h2>
    <span id="profile-user">
      <img :src="profileImg" :alt="user.username">
      <h2>반가워요!! {{ user.username }}</h2>
    </span>
    <button id="logout-btn" @click="logout">Logout</button>
    <span id="follows">
      <h3>게시글 : {{ user.community_set.length }}</h3>
      <h3>팔로워 : {{ user.followers.length }}</h3>
      <h3>팔로잉 : {{ user.followings.length }}</h3>
    </span>
    <hr>
    <div id="profile-set">
      <h3>게시글</h3>
      <div id="profile-community-container">
        <user-community v-for="(article, idx) of user.community_set" :key="'community-' + idx" :article="article" />
      </div>
      <h3>영화 리뷰</h3>
      <div id="profile-review-container">
        <user-review v-for="(review, idx) of user.review_set" :key="'review-' + idx" :review="review" />
      </div>
    </div>
    <button id="profile-btn" @click="profileHide">></button>
  </div>
</template>

<script>
import UserReview from '@/components/accounts/profile/ProfileReview';
import UserCommunity from '@/components/accounts/profile/ProfileCommunity';
import axios from "axios"

export default {
  data: function(){
    return {
      user: null
    }
  },
  components: {
    UserReview,
    UserCommunity
  },
  methods: {
    profileHide: function(){
      this.$emit('profile-hide')
    },
    logout: function(){
      if (confirm('로그아웃 하시겠습니까?')){
        localStorage.removeItem('jwt')
        location.reload()
        this.$router.push({ name: 'Login' })
      }
    }
  },
  computed: {
    profileImg: function(){
      if (!this.user.profile_img){
        return require('@/assets/profile.png')
      }
      return this.user.profile_img
    }
  },
  beforeCreate: function(){
    if (localStorage.getItem('jwt')){
      axios({
        method: 'get',
        url: 'http://localhost:8000/accounts/profile/',
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
      .then(response => {
        console.log(response.data)
        this.user = response.data
      })
      .then(() => {
        if (this.user.like_genres.length == 0){
          this.$router.push({ name: 'MovieChoice' })
        }
        this.$store.dispatch('user_update', this.user)
      })
      .catch(() => {
        console.log('fail..')
        if (localStorage.getItem('jwt')){
          localStorage.removeItem('jwt')
          location.reload()
          this.$router.push({ name: 'Login' })
        }
      })
    }
  }
}
</script>

<style>
  #profile {
    width: 30vw;
    height: 100vh;
    position: absolute;
    top: 0;
    right: 0;
    background-color: #e4e2d7;
  }

  #profile-user {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #profile-user > img {
    border: 5px rgb(187, 187, 187) solid;
    border-radius: 50%;
    background-color: rgb(207, 207, 207);
    width: 3rem;
    height: 3rem;
  }

  #profile-user * {
    margin: 0 0.5rem;
  }

  #logout-btn {
    background-color: rgb(235, 111, 111);
    border: none;
    border-radius: 0.5rem;
    padding: 0.25rem 0.5rem;
  }

  #profile-btn {
    background-color: rgb(255, 255, 255, 0.75);
    border-radius: 1rem;
    color: rgb(128, 128, 128, 0.75);
    position: absolute;
    top: 50%;
    left: -2.5%;
    font-size: 1.25rem;
    padding: 0.5rem;
  }
  
  #profile-set {
    padding: 1rem;
  }

  #profile-community-container {
    background-color: rgba(0, 0, 0, 0.75);
    padding: 1rem 1rem 0.5rem 1rem;
    max-height: 20vh;
    overflow: scroll;
  }

  #profile-review-container {
    background-color: rgba(0, 0, 0, 0.75);
    padding: 1rem 1rem 0.5rem 1rem;
    max-height: 20vh;
    overflow: scroll;
  }

  #follows {
    display: flex;
    justify-content: space-evenly;
    width: 75%;
    margin: 1rem auto;
  }
</style>