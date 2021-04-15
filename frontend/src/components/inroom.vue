<template>
  <div id="inroom">
      <h1>
          ROOM CODE:
      </h1>
    <router-link to="suggestions" v-if="$route.path != '/suggestions'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
          @click="navigate()">
         DONE
        </button>
    </router-link> <br><br>
    <router-link to="review" v-if="$route.path != '/review'">
        <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
          @click="navigate()">
         Write Review
        </button>
    </router-link> <br><br>
     <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
          @click="navigate()">
         Yes
        </button>
     <button
         class="btn btn-primary btn-margin"
         v-if="!authenticated"
          @click="navigate()">
         No
        </button>
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
