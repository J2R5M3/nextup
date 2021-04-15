<template>
  <div id="deletemedia">
        <label for="media id">Media ID:</label><br>
        <input type="text" id="media_id" name="media-id"><br>
    <router-link to="admin" v-if="$route.path != '/admin'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
         @click="navigate()">
         Delete Media
        </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'deletemedia'
}
</script>

<style>
#deletemedia {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #084583;
  margin-top: 70px;
}
</style>
