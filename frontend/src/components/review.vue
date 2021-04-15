<template>
  <div id="review">
      <label for="rating">Rating:</label><br>
      <input type="text" id="rating" name="rating"><br><br>
      <label for="comment">Comment:</label><br>
      <input type="text" id="comment" name="comment"><br><br>
    <router-link to="suggestions" v-if="$route.path != '/suggestions'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
          @click="navigate()">
         DONE
        </button>
    </router-link> <br><br>
  </div>
</template>

<script>
export default {
  name: 'review'
}
</script>

<style>
#review {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #070f18;
  margin-top: 70px;
}
</style>
