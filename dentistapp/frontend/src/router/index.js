import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/o-nama',
    name: 'AboutView',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/registracija',
    name: 'UserRegistration',
    component: () => import(/* webpackChunkName: "about" */ '../views/UserRegistration.vue')
  },
  {
    path: '/usluge',
    name: 'TheServices',
    component: () => import(/* webpackChunkName: "about" */ '../views/TheServices.vue')
  },
  {
    path: '/login',
    name: 'UserLogin',
    component: () => import(/* webpackChunkName: "about" */ '../views/UserLogin.vue')
  },
  {
    path: '/zakazi-pregled',
    name: 'NewAppointment',
    component: () => import(/* webpackChunkName: "about" */ '../views/NewAppointment.vue')
  },
  {
    path: '/prikazi-evidenciju',
    name: 'ShowReport',
    component: () => import(/* webpackChunkName: "about" */ '../views/ShowReport.vue')
  },
  {
    path: '/ocene',
    name: 'TheReviews',
    component: () => import(/* webpackChunkName: "about" */ '../views/TheReviews.vue')
  },
  {
    path: '/korisnicka-podrska',
    name: 'CustomerService',
    component: () => import(/* webpackChunkName: "about" */ '../views/CustomerService.vue')
  },
  {
    path: '/uredi-preglede',
    name: 'ManageAppointments',
    component: () => import(/* webpackChunkName: "about" */ '../views/ManageAppointments.vue')
  },
  {
    path: '/novi-izvestaj',
    name: 'NewReport',
    component: () => import(/* webpackChunkName: "about" */ '../views/NewReport.vue')
  },
  {
    path: '/moj-profil',
    name: 'MyProfile',
    component: () => import(/* webpackChunkName: "about" */ '../views/MyProfile.vue')
  },
  {
    path: '/korisnicka-podrska-admin',
    name: 'CustomerServiceAdmin',
    component: () => import(/* webpackChunkName: "about" */ '../views/CustomerServiceAdmin.vue')
  },
  {
    path: '/zahtevi',
    name: 'NewRequests',
    component: () => import(/* webpackChunkName: "about" */ '../views/NewRequests.vue')
  },
  {
    path: '/uredi-ordinaciju',
    name: 'ManageOffice',
    component: () => import(/* webpackChunkName: "about" */ '../views/ManageOffice.vue')
  },
  {
    path: '/moji-izvestaji',
    name: 'MyAllReports',
    component: () => import(/* webpackChunkName: "about" */ '../views/MyAllReports.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
