<template>
  <div @click="goToDetail" class="user-community">
    <h4>{{ article.title | truncate(10) }}</h4>
    <p>{{ article.content | truncate(30) }}</p>
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
    }
  },
  filters: {
    truncate: function(target ,num){
      if (target.length > num){
        return target.slice(0, num) + '...'
      }
      return target
    }
  }
}
</script>

<style>
  .user-community {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;
    border-radius: 0.5rem;
    padding: 1rem;
    background-color: rgba(255, 255, 255);
    color: rgb(0, 0, 0);
    cursor: pointer;
    margin-bottom: 0.5rem;
  }

  .user-community * {
    margin: 0;
  }
</style>