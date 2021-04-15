<template>
  <div id="hostroom">
      <h1>
          Start A New Room
      </h1>
      <form>
        <label for="hostcode">Enter Code:</label><br>
        <input type="text" id="hostcode" name="hostcode"><br>
    </form>
    <router-link to="inroom" v-if="$route.path != '/inroom'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
          @click="navigate()">
         Host
        </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'hostroom'
}
</script>

<style>
#hostroom {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #070f18;
  margin-top: 70px;
}
</style>
