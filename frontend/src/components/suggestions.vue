<template>
  <div id="suggestions">
      <h1>
          ROOM CODE:<br>
          GROUP SUGGESTIONS
      </h1>
    <router-link to="room" v-if="$route.path != '/room'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
          @click="navigate()">
         Exit
        </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'inroom'
}
</script>

<style>
#inroom {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #070f18;
  margin-top: 70px;
}
</style>
