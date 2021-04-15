<template>
  <div id="app">
    <h1>
    Nextup!
    </h1>
    <router-link to='login' v-if="$route.path != '/login'">
      <button
      class="btn btn-primary btn-margin"
      v-if="!authenticated"
      @click="navigate()">
      Log In
    </button>
    </router-link>
    <router-link to="createaccount" v-if="$route.path != ('/createaccount')">
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
