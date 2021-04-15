<template>
  <div id="createaccount">
    <h1>
    Create An Account
    </h1>
    <form>
        <label for="name">First/Last Name:</label><br>
        <input type="text" id="name" name="name"><br>
        <label for="email">Email:</label><br>
        <input type="text" id="email" name="email"><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br>
    </form>
     <button
      class="btn btn-primary btn-margin"
      v-if="!authenticated"
      @click="navigate()">
      Join
    </button>
  </div>
</template>

<script>
export default {
  name: 'createaccount'
}
</script>

<style>
#createaccount {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
