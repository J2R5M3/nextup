import Vue from 'vue'
import Router from 'vue-router'
import createaccount from '@/components/createaccount'
import login from '@/components/login'
import room from '@/components/room'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/createaccount',
      name: 'createaccount',
      component: createaccount
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/room',
      name: 'room',
      component: room
    }
  ]
})
