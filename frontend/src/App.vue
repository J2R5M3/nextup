<template>
  <div id="app">
    <h1>
    Nextup!
    </h1>
     <button
      class="btn btn-primary btn-margin"
      v-if="!authenticated"
      @click="navigate()">
      Log In
    </button>
    <router-link to="createaccount">
      <button
      class="btn btn-primary btn-margin"
      v-if="!authenticated"
      @click="navigate()">
      Create An Account
    </button>
    </router-link>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
