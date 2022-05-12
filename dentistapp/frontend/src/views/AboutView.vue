<template>
	<div class="container">
		<div class="row">
			<div class="col-md-6 col-12">
				<div class="row content-column">
					<div class="col-md-8 col-12">
						<h2>O nama</h2>
					</div>
				</div>
				<div class="row p-2">
					<div class="col-md-8 col-12 about">
						<p class="about-text">
							Ovde mozete naci nase podatke, gde se nalazimo
							<br><br>
							Contrary to popular belief, Lorem Ipsum is not simply random text. 
							It has roots in a piece of classical Latin literature from 45 BC,
							making it over 2000 years old. Richard McClintock, a 
							Latin professor at Hampden-Sydney College in Virginia
							<br><br>
							Ovde mozete naci nase podatke, gde se nalazimo
							<br><br>
							McClintock, a 
							Latin professor at Hampden-Sydney College in Virginia
						</p>
					</div>
				</div>
			</div>
			<div class="col-md-6 col-12">
				<div class="row content-column">
					<div class="col-md-8 col-12">
						<h2>Naša lokacija</h2>
					</div>
				</div>
				<div class="row p-2">
					<div id="map" class="col-md-8 col-12 about">
					</div>
				</div>
			</div>

		</div>
	</div>
</template>

<script>
// @ is an alias to /src
import "leaflet/dist/leaflet.css";
import L from "leaflet";

export default {
	name: 'AboutView',
	components: {
	},
	mounted() {
		var map = L.map('map').setView([44.8057, 20.4763], 16.5);
		L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
			attribution: '',
			maxZoom: 19,
			id: 'mapbox/streets-v11',
			tileSize: 512,
			zoomOffset: -1,
			accessToken: 'pk.eyJ1IjoieGl2aTBuIiwiYSI6ImNsMzM0ejhrdTBodXEzZHA1b2NleW52amoifQ.-MrxrYlvJsspfZWlxKhTUQ'
		}).addTo(map);

		let markerIcon = {
			icon: L.icon({
			iconSize: [25, 41],
			iconAnchor: [10, 41],
			popupAnchor: [2, -40],
			// specify the path here
			iconUrl: "https://unpkg.com/leaflet@1.4.0/dist/images/marker-icon.png",
			shadowUrl: "https://unpkg.com/leaflet@1.4.0/dist/images/marker-shadow.png"
			})
		}
		var marker = L.marker([44.8057, 20.4763], markerIcon).addTo(map);
		marker.bindPopup("<b>Mi smo ovde!</b>").openPopup();
		// L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/20.4758,44.8055,14.59,0/300x200?access_token=pk.eyJ1IjoieGl2aTBuIiwiYSI6ImNsMzM0ejhrdTBodXEzZHA1b2NleW52amoifQ.-MrxrYlvJsspfZWlxKhTUQ")
	}
}
</script>

<style scoped>
	* {
		color: #05284B;
	}

	.about {
		width: 100%;
		padding-left: 10px;
		padding-right: 10px;
		background: white;
		text-align: center;
		display: flex;
		justify-content: center;
		box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
		border-radius: 10px;
	}

	.about-text {
		width: 80%;
		margin-top: 20px;
		margin-bottom: 20px;
		background: white;
		text-align: center;
	}

	h2 {
		font-weight: 700;
		font-size: 40px;

	}

	#map { 
		min-height: 450px;
		
	}

	.nes {
		align-self: stretch;
	}

</style>