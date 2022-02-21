<template>
  <div v-if="article" id="community-detail">
    <span class="detail-head">
      <h1>{{ article.title }}</h1>
      <span class="detail-like">
        <img id="like" @click="like" :src="liked" alt="like-button">
        <h3>{{ article.like_users.length }}</h3>
      </span>
    </span>
    <span class="detail-col">
      <img @click="goProfile" class="go-profile" :src="profileSrc" alt="">
      <h2 @click="goProfile" class="go-profile">{{ article.user.username }}</h2>
      <p>{{ article.created_at | dateTime }}</p>
    </span>
    <img v-if="thumbnailSrc" :src="thumbnailSrc" alt="">
    <span class="detail-content">
      <p>{{ article.content }}</p>
    </span>
    <div id="comments">
      <form @submit.prevent="commentCreate">
        <input type="text" placeholder="댓글을 입력해주세요!"> 
        <button>add</button>
      </form>
      <comment v-for="comment of article.comment_set" :key="comment.id"
       :comment="comment" :articleId="article.id" />
    </div>
  </div>
</template>

<script>
import Comment from '@/components/community/comment/Comment'
import axios from "axios"

export default {
  data: function () {
    return {
      article: null,
    }
  },
  components: {
    Comment
  },
  methods: {
    goProfile: function () {
      this.$router.push({ name: 'ProfileOther', params: { userId: this.article.user.id, username: this.article.user.username}})
    },
    like: function(){
      axios({
        method: 'post',
        url: `http://localhost:8000/community/${ this.$router.history.current.params.articleId }/like/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
      .then(response => {
        this.article.like_users = response.data.like_users
      })
      .catch(() => console.log('like error!'))
    },
    commentCreate: function(event){
      axios({
        method: 'post',
        url: `http://localhost:8000/community/${ this.article.id }/comment/`,
        data: {
          content: event.target[0].value
        },
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
      })
      .then(response => {
        console.log(response)
        this.article = response.data
      })
      .catch(() => console.log('comment error!!'))
    }
  },
  computed: {
    thumbnailSrc: function(){
      if (this.article.thumbnail){
        return 'http://localhost:8000' + this.article.thumbnail
      }
      else {
        return null
      }
    },
    profileSrc: function(){
      if (this.article.user.profile_img){
        return 'http://localhost:8000/' + this.article.user.profile_img
      }
      return require('@/assets/profile.png')
    },
    liked: function(){
      if (this.article.like_users.find(ele => ele == this.$store.state.user.id)){
        return require('@/assets/heart.png')
      }
      return require('@/assets/heart-blank.png')
    },
  },
  filters: {
    dateTime: function(target){
      const date = new Date(target)
      return date.toLocaleString()
    }
  },
  beforeCreate: function() {
    axios({
      method: 'get',
      url: 'http://localhost:8000/community/' + this.$router.history.current.params.articleId,
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
    })
    .then(response => {
      console.log(response)
      this.article = response.data
    })
    .catch(() => {
      console.log('article error!!')
    })
  }
}
</script>

<style scoped>
  #community-detail {
    color: white;
    margin: 0 auto;
    background-color: rgb(0, 0, 0, 0.5);
    padding: 1rem;
    display: flex;
    width: 60vw;
    min-height: 90vh;
    height: 100%;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 2rem 5rem;
  }
  
  #community-detail h1 {
    margin: 0;
    font-size: 2.5rem;
  }

  .detail-head {
    display: flex;
    width: 100%;
    justify-content: space-between;
  }

  .detail-like {
    display: flex;
    justify-content: flex-end;
    width: 30%;
  }

  .detail-col {
    display: flex;
    align-items: center;
  }

  .detail-col img {
    width: 4%;
    border: 2px rgb(187, 187, 187) solid;
    border-radius: 50%;
    background-color: rgb(207, 207, 207);
    margin: 1rem
  }

  .detail-content {
    display: flex;
    justify-content: flex-start;
    align-self: stretch;
    padding: 1rem;
    margin: 1rem;
    background-color: rgb(128, 128, 128, 0.5);
  }

  p {
    margin: 1rem;
  }

  div img {
    width: 100%;
    margin: auto;
  }

  #like {
    width: 30px;
    aspect-ratio: 1 / 1;
    margin: 1rem;
    cursor: pointer;
    color: white;
  }

  #comments {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
  }

  #comments form {
    display: flex;
    align-items: center;
    width: 100%;
    margin-bottom: 1rem;
  }

  #comments input {
    margin: 0;
    border-radius: 5px;
    padding: 10px;
    width: 100%;
  }

  #comments button {
    padding: 0.5rem 2rem;
    height: 10%;
    border-radius: 10px;
    font-size: 1.25rem;
    font-weight: bold;
    /* bacc */
  }

  .go-profile{
    cursor: pointer;
    font-size: 1.5rem;
    color: papayawhip
  }
  </style>