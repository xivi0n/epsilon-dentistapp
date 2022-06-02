<template>
<!-- @/assets/ord1.jpg -->
	<div class="container"> 
		<div class="row">
			<div class="col-lg-8 col-12">
				<Carousel :autoplay="5000">
					<Slide v-for="slide in slides" :key="slide">
						<div class="carousel__item"><img :src="slide" alt=""></div>
					</Slide>
					<template #addons>
						<Pagination />
					</template>
				</Carousel>
			</div>
			<div class="col-lg-4 col-12">
				<p class="text-center opis p-5 cell">
					Stomatološka ordinacija DentistApp otvorena je 2022. godine 
					<br><br>
					Naš tim čine specijalisti sa dugogodišnjim iskustvom, koji Vam mogu pružiti usluge iz svih oblasti stomatologije. 
					Raspolažemo savremenom opremom i najnovijim materijalima.
				</p>
			</div>
		</div>
		<div class="row my-4 cell">
			<div class="col-12 col-md-6 cell d-table">
				<div class="center h-100 w-100">
					<p class="heading text-center p-5 h-100 w-100">
						Neka ocene naših pacijenata
						<br>
						govore umesto nas
					</p>
					<p v-if="logged_in == true && tipK =='pacijent'">
						Želite i vi da napišete ocenu? 
						Kliknite <router-link to="/dodaj-ocenu">ovde</router-link>
					</p>
				</div>
			</div>
			
			<div class="col-12 col-md-6 px-4" v-if="reviews.length > 0">
				<Carousel :autoplay="5000">
					<Slide v-for="review in reviews" :key="review.idO">
						<div class="carousel__item">
							<div class="card-body">
								<h5 class="card-subtitle mb-2 text-muted">{{review.ime}} {{review.prezime}} - Ocena {{review.ocena}}</h5>
								<hr class="">
								<p class="card-text text-center pb-2">{{review.opis}}</p>
							</div>
						</div>
					</Slide>
					<template #addons>
						<Pagination />
						<Navigation />
					</template>
				</Carousel>
			</div>
		</div>
		<div class="row my-4 cell">
			<div class="col-12 col-md-6 center-services">
				<div class="row service-row" :key="service.idU" v-for="service in services.slice(0,5)">
					<TheService :service="service" :show_price="false"/>
				</div>
			</div>
			<div class="col-12 col-md-6 cell d-table">
				<div class="center h-100 w-100">
					<p class="heading text-center p-5 h-100 w-100">
						Ostale usluge proverite <router-link to="/usluge">ovde</router-link>
					</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import ord1 from '@/assets/ord1.jpg'
import ord2 from '@/assets/ord2.jpg'
import ord3 from '@/assets/ord3.jpg'
import axios from 'axios'

import { Carousel, Pagination, Slide, Navigation } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'
import TheService from '@/components/TheService.vue'

// @ is an alias to /src
export default {
	name: "HomeView",
	components: {
		Carousel,
		Slide,
		Pagination,
		Navigation,
		TheService
	},
	data () {
		return {
			slides: [ord1, ord2, ord3],
			reviews: [],
			logged_in: (localStorage.getItem("logged_in") === 'true'),
			tipK: localStorage.getItem("tipK"),
			services: []
		}
	},
	mounted() {
		document.title = "DentistApp"
		axios.get("http://localhost:8000/api/v1/ocene/")
		.then(response => {
			console.log(response)
            this.reviews = response.data
        }).catch(error => {
            console.log(error)
            // this.$router.push("/404")
        })

		axios.get('http://localhost:8000/api/v1/sve-usluge/')
		.then(response => {
			this.services = response.data
			this.services.forEach(e => {
				e.cena = Math.trunc(e.cena)
			})
			console.log(this.services)
		})
		.catch(error => {
			console.log(error)
		})
	},
	methods: {
	}
};
</script>

<style scoped>
	.center {
		display: table-cell;
		vertical-align: middle;
	}

	a {
		text-decoration: none;
		color: #0583D2;
	}
	
	p {
		text-align: center;
		display: block;
	}

	p.heading {
		font-weight: 600;
		font-size: 24px;
		color: #05284B;
	}

	p.opis {
		font-weight: 400;
		font-size: 20px;
		color: #05284B;
	}

	img {
		height: 240px;
		background: #FFFFFF;
		border-radius: 10px;
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
	}

	@media screen and (max-width: 1100px){
		.container {
			width: 100%;
		}

		img {
			height: 350px;
		}
	}

	@media screen and (min-width: 1100px){
		.container {
			width: 75%;
		}
		img {
			height: 500px;
		}
	}

	.cell {
        /* background: #FFFFFF; */
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
        border-radius: 10px;
    }
	
</style>