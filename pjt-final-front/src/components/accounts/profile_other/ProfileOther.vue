<template>
  <div v-if="user" id="profile-other">
    <span class="profile-other-info">
      <img :src="profileImg" :alt="username">
      <h1>{{ username }}</h1>
      <div v-if="user.id != this.$store.state.user.id">
        <button v-if="!followed" id="follow" @click="follow">팔로우</button>
        <button v-if="followed" id="follow" class="unfollow" @click="follow">언팔로우</button>
      </div>
    </span>
    <span id="follows">
      <h3 @click="communityShow = true; followerShow = false; followingShow = false">게시글 : {{ user.community_set.length }}</h3>
      <h3 @click="followerShow = true; communityShow = false; followingShow = false">팔로워 : {{ user.followers.length }}</h3>
      <h3 @click="followingShow = true; communityShow = false; followerShow = false">팔로잉 : {{ user.followings.length }}</h3>
    </span>
    <hr>
    <div>
      <span v-if="communityShow" class="other-container">
        <profile-other-community v-for="article in user.community_set" :key="article.id" :article="article"/>
      </span>
      <span v-if="followerShow" class="other-container-follow">
        <profile-other-follower v-for="follower in user.followers" :key="follower.id" :follower="follower" />
      </span>
      <span v-if="followingShow" class="other-container-follow">
        <profile-other-following v-for="following in user.followings" :key="following.id" :following="following" />
      </span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProfileOtherCommunity from '@/components/accounts/profile_other/ProfileOtherCommunity'
import ProfileOtherFollower from '@/components/accounts/profile_other/ProfileOtherFollower'
import ProfileOtherFollowing from '@/components/accounts/profile_other/ProfileOtherFollowing'

export default {
  data: function () {
    return {
      user: null,
      userId: this.$router.history.current.params.userId,
      username: this.$router.history.current.params.username,
      communityShow: true,
      followerShow: false,
      followingShow: false,
    }
  },
  components: {
    ProfileOtherCommunity,
    ProfileOtherFollower,
    ProfileOtherFollowing
  },
  methods: {
    follow: function(){
      axios({
        method: 'post',
        url: `http://localhost:8000/accounts/${ this.user.id }/follow/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
      .then(response => {
        // console.log(response)
        this.user.followers = response.data.followers
      })
    }
  },
  computed: {
    profileImg: function(){
      if (this.user.profile_img){
        return 'http://localhost:8000' + this.user.profile_img
      } 
      return require('@/assets/profile.png')
    },
    followed: function(){
      if (this.user.followers.find(idx => idx.id == this.$store.state.user.id)){
        return true
      }
      return false
    }
  },
  beforeCreate: function () {
    if (localStorage.getItem('jwt')){
      axios({
        method: 'get',

        url: `http://localhost:8000/accounts/${this.$route.params.username}/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
        .then(response => {
          console.log(response.data)
          this.user = response.data
        })
        .catch(err => {
          console.log(this.username)
          console.log(err)
        })
    }
  }
}
</script>

<style>
  #profile-other{
    width: 70vw;
    margin: 3rem auto 3rem;
    background: #f6f5ef;
    border-radius: 1rem;
  }

  .other-container{
    display: flex;
    flex-wrap: wrap;
    margin: 1rem;
    justify-content: center;
  }

  .other-container-follow{
    display: flex;
    flex-wrap: wrap;
    margin: 1rem;
  }

  .profile-other-info{
    display: flex;
    justify-content: center;
    align-items: center;  
  }

  .profile-other-info * {
    margin: 2rem;
  }

  .profile-other-info > img {
      border: 5px rgb(187, 187, 187) solid;
      border-radius: 50%;
      background-color: rgb(207, 207, 207);
      width: 5rem;
      height: 5rem;
    }

  #follow {
    border: none;
    border-radius: 10px;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    font-weight: bold;
  }

  #follows h3 {
    cursor: pointer;
  }

  .unfollow {
    background-color: rgb(240, 115, 115);
  }
</style>