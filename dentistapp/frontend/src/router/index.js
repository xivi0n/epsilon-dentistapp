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
		path: '/korisnicka-podrska',
		name: 'CustomerService',
		component: () => import(/* webpackChunkName: "about" */ '../views/CustomerService.vue')
	},
	{
		path: '/novi-izvestaj/:id',
		name: 'NewReport',
		component: () => import(/* webpackChunkName: "about" */ '../views/NewReport.vue')
	},
	{
		path: '/moj-profil',
		name: 'MyProfile',
		component: () => import(/* webpackChunkName: "about" */ '../views/MyProfile.vue')
	},
	{
		path: '/moji-izvestaji',
		name: 'MyAllReports',
		component: () => import(/* webpackChunkName: "about" */ '../views/MyAllReports.vue')
	},
	{
		path: '/404',
		name: 'The404Error',
		component: () => import(/* webpackChunkName: "about" */ '../views/The404Error.vue')
	},
	{
		path: '/moji-izvestaji/izvestaj/:id',
		name: 'DetailedReport',
		component: () => import(/* webpackChunkName: "about" */ '../views/DetailedReport.vue')
	},
	{
		path: '/moji-zahtevi',
		name: 'MyAllRequests',
		component: () => import(/* webpackChunkName: "about" */ '../views/MyAllRequests.vue')
	},
	{
		path: '/dodaj-ocenu',
		name: 'NewReview',
		component: () => import(/* webpackChunkName: "about" */ '../views/NewReview.vue')
	}
]

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes
})

export default router
