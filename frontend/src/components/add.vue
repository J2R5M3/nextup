<template>
  <div id="add">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="arturl">Art Url:</label><br>
        <input type="text" id="arturl" name="arturl"><br>
        <label for="releasedate">Release Date:</label><br>
        <input type="text" id="releasedate" name="releasedate"><br>
        <label for="genre">Genre:</label><br>
        <input type="text" id="genre" name="genre"><br>
        <label for="runningtime">Running Time:</label><br>
        <input type="text" id="runningtime" name="runningtime"><br>
        <label for="director">Director:</label><br>
        <input type="text" id="director" name="director"><br>
        <label for="season">Season:</label><br>
        <input type="text" id="season" name="season"><br>
        <label for="episode">Episode:</label><br>
        <input type="text" id="episode" name="episode"><br>
        <label for="description">Description:</label><br>
        <input type="text" id="description" name="description"><br><br>
    <router-link to="admin" v-if="$route.path != '/admin'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
         @click="navigate()">
         Add Media
        </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'add'
}
</script>

<style>
#add {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #084583;
  margin-top: 70px;
}
</style>
