<template>
  <div v-if="following" @click="goToProfile" class="profile-other-follower">
    <img :src="ProfileSrc" :alt="following.username">
    <h3>{{ following.username }}</h3>
  </div>
</template>

<script>
export default {
  props: {
    following: Object
  },
  methods: {
    goToProfile: function () {
      this.$router.push({name: 'ProfileOther', params: {username: this.following.username}})
      location.reload()
    }
  },
  computed: {
    ProfileSrc: function(){
      if (this.following.profile_img){
        return 'http://localhost:8000' + this.following.profile_img
      }
      else {
        return require('@/assets/profile.png')
      }
    }
  }
}
</script>

<style>
  .profile-other-follower {
    cursor: pointer;
    display: flex;
    background: rgba(112, 112, 112, 0.5);
    /* justify-content: center; */
    align-items: center;
    margin: 1rem;
    width: 20%;
    border: none;
    border-radius: 1rem;
    overflow: auto;
  }

  .profile-other-follower > img {
    border: 5px rgb(187, 187, 187) solid;
    border-radius: 50%;
    background-color: rgb(207, 207, 207);
    width: 20%;
    margin: 0.5rem;
  }

  .profile-other-follower > h3 {
    display: flex;
    margin: 0.5rem;
  }
</style>