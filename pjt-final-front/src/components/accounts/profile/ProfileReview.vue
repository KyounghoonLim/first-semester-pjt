<template>
  <div class="user-review">
    <h4>{{ review.movie.title }}</h4>
    <span>
      <p>{{ review.content | truncate(10) }}</p>
      <p>{{ review.score }}</p>
    </span>
  </div>
</template>

<script>
export default {
  props: {
    review: Object
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
  .user-review {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    border-radius: 0.5rem;
    padding: 1rem;
    background-color: #ffffff;
    color: black;
    margin-bottom: 0.5rem;
  }

  .user-review * {
    margin: 0;
  }

  .user-review span {
    display: flex;
    justify-content: space-between;
    align-self: stretch;
  }
</style>