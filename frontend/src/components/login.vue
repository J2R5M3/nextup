<template>
  <div id="login">
    <h1>
    Welcome Back
    </h1>
    <form>
        <label for="email">Email:</label><br>
        <input type="text" id="email" name="email"><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br>
    </form>
     <router-link to='room' v-if="$route.path != '/room'">
       <button
        class="btn btn-primary btn-margin"
        v-if="!authenticated"
        @click="navigate()">
        Login
       </button>
     </router-link>
     <router-link to='admin' v-if="$route.path != '/admin'">
       <button
        class="btn btn-primary btn-margin"
        v-if="!authenticated"
        @click="navigate()">
        Admin
       </button>
     </router-link>
  </div>
</template>

<script>
export default {
  name: 'login'
}
</script>

<style>
#login {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
