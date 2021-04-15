import Vue from 'vue'
import Router from 'vue-router'
import createaccount from '@/components/createaccount'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/createaccount',
      name: 'createaccount',
      component: createaccount
    }
  ]
})
