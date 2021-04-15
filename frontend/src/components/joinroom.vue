<template>
  <div id="joinroom">
      <h1>
          Join A Room
      </h1>
      <form>
        <label for="entercode">Enter Room Code:</label><br>
        <input type="text" id="entercode" name="entercode"><br>
    </form>
    <router-link to="inroom" v-if="$route.path != '/inroom'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
          @click="navigate()">
         Join
        </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'joinroom'
}
</script>

<style>
#joinroom {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #070f18;
  margin-top: 70px;
}
</style>
