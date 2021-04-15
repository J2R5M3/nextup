<template>
  <div id="room">
    <router-link to="hostroom" v-if="$route.path != '/hostroom'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
          @click="navigate()">
         Create Room
        </button>
      </router-link>
    <router-link to="joinroom" v-if="$route.path != '/joinroom'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
         @click="navigate()">
         Join Room
        </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'room'
}
</script>

<style>
#room {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #084583;
  margin-top: 70px;
}
</style>
