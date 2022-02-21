<template>
  <div v-if="articles" id="community">
    <br>
    <span class="community-intro">
      <span>
        <img id="community-logo" :src="require('@/assets/film-reel.png')" alt="movie.png">
        <h1>COMMUNITY</h1>
      </span>
      <br>
      <h2>나의 생각을 공유하고 싶나요?</h2>
      <button id="create-btn" @click="goCreate">생각 공유하기</button>
      <br>
    </span>
    <span class="community-container">
      <div v-for="article of pageArticles" :key="article.id">
        <community-card :article="article" />
      </div>
    </span>
  </div>
</template>

<script>
import CommunityCard from '@/components/community/Community_Card';
import axios from "axios"

export default {
  data: function(){
    return {
      articles: null,
      pagination: 1
    }
  },
  components: {
    CommunityCard
  },
  methods: {
    goCreate: function () {
      this.$router.push({ name: 'Community_Create' })
    }
  },
  computed: {
    pageArticles: function(){
      return this.articles.slice(0, this.pagination * 8)
    }
  },
  created: function(){
    axios({
      method: 'get',
      url: 'http://localhost:8000/community/',
      headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` }
    })
    .then(response => {
      console.log(response)
      this.articles = response.data
    })
    .catch(() => console.log('error'))
  },
  mounted: function(){
    document.addEventListener('scroll', () => {
      const {scrollHeight, scrollTop, clientHeight} = document.documentElement
      if (scrollHeight - Math.round(scrollTop) === clientHeight && this.pagination * 8 < this.articles.length){
        this.pagination += 1
      }
    })
  }
}
</script>

<style>
#community {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}


#community-logo {
  width: 3rem;
  margin-right: 1rem;
}

.community-intro {
  color: white;
}

.community-intro > span {
  display: flex;
  justify-content: center;
  align-items: center;
}

#create-btn {
  background: rgb(22, 165, 117);
  cursor: pointer;
  font-size: 1.25rem;
  font-weight: bold;
  border-radius: 0.5rem;
  padding: 0.5rem 2rem;
  margin: 2rem;
}

  
.community-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  /* margin: 1rem auto; */
  width: 100%;
  /* justify-content: space-between; */
  flex-wrap: wrap;
}

</style>