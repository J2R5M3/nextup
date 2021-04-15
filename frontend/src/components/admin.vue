<template>
  <div id="admin">
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
    <router-link to="add" v-if="$route.path != '/add'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
         @click="navigate()">
         Add Media
        </button>
    </router-link>
    <router-link to="deletemedia" v-if="$route.path != '/delete'">
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
  name: 'admin'
}
</script>

<style>
#admin {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #084583;
  margin-top: 70px;
}
</style>
