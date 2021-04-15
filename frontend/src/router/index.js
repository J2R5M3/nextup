import Vue from 'vue'
import Router from 'vue-router'
import createaccount from '@/components/createaccount'
import login from '@/components/login'
import room from '@/components/room'
import admin from '@/components/admin'
import joinroom from '@/components/joinroom'
import hostroom from '@/components/hostroom'
import inroom from '@/components/inroom'
import suggestions from '@/components/suggestions'
import add from '@/components/add'
import deletemedia from '@/components/deletemedia'
import review from '@/components/review'

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
    },
    {
      path: '/admin',
      name: 'admin',
      component: admin
    },
    {
      path: '/joinroom',
      name: 'joinroom',
      component: joinroom
    },
    {
      path: '/hostroom',
      name: 'hostroom',
      component: hostroom
    },
    {
      path: '/inroom',
      name: 'inroom',
      component: inroom
    },
    {
      path: '/suggestions',
      name: 'suggestions',
      component: suggestions
    },
    {
      path: '/add',
      name: 'add',
      component: add
    },
    {
      path: '/deletemedia',
      name: 'deletemedia',
      component: deletemedia
    },
    {
      path: '/review',
      name: 'review',
      component: review
    }
  ]
})
