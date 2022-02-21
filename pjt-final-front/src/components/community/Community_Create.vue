<template>
  <div id="community-create">
    <h1>게시글 작성하기</h1>
    <hr>
    <div class="community-create-container">
      <h3>제목</h3>
      <input type="text" v-model.trim="title" placeholder="제목을 입력해주세요" maxlength="10">
      <h3>내용</h3>
      <input type="text" v-model.trim="content" placeholder="내용을 입력해주세요">
      <h3>이미지</h3>
      <form enctype="multipart/form-data">
        <input type="file" accept="image/*" @change="inputChange">
      </form>
    </div>
    <button @click="createArticle" class="community-create-button">게시글 등록</button>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data: function () {
    return {
      title: null,
      content: null,
      thumbnail: null
    }
  },
  methods: {
    createArticle: function () {
      if (this.title) { 
        const article = new FormData()
        article.append('title', this.title); article.append('content', this.content);
        article.append('user', '')
        if (this.thumbnail){
          article.append('thumbnail', this.thumbnail)
        }
        else {
          article.append('thumbnail', '')
        }
        axios({
          method: 'post',
          url: 'http://localhost:8000/community/',
          data: article,
          headers: { 
            'Content-Type': 'multipart/form-data',
            'Authorization': `JWT ${localStorage.getItem('jwt')}` 
          }
        })
          .then(response => {
            console.log(response)
            this.$router.push({name: 'Community'})
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    inputChange: function(event){
      console.log(event.target.files)
      this.thumbnail = event.target.files[0]
    }
  }
}
</script>

<style>
  #community-create {
    width: 30vw;
    margin: 3rem auto;
    padding: 2rem;
    /* background-color: #f6f5ef; */
    background-color: white;
    border-radius: 2rem;
  }

  .community-create hr {
      width: 80%;
    }

.community-create-container {
  margin: 1rem auto;
  padding: 1rem auto;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  /* align-items: center; */
  /* width: 80%; */
}

.community-create-container input {
  width: 100%;
  height: 2rem;
}


.community-create-button {
    cursor: pointer;
    display: block;
    background-color: rgb(22, 165, 117);
    border-radius: 0.5rem;
    margin: 2rem auto;
    padding: 0.5rem 2rem;
    font-size: 1.25rem;
    font-weight: bold;
  }

#community-create h3 {
  display: flex;
  
}

</style>








