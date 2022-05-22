from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('sve-usluge/', SveUsluge.as_view()),
    path('registracija/', registracija, name = 'registracija'),
    path('login/', obtain_auth_token, name = "login"),
    path('moj-profil/', mojProfilView, name = 'mojProfil'),
    path('moji-izvestaji/', MojiIzvestaji.as_view(), name = 'mojiIzvestaji'),
    path('logout/', logout, name='logout'),
    path('moji-zahtevi/', MojiZahtevi.as_view(), name = 'mojiZahtevi'),
    path('moji-pregledi/', MojiPregledi.as_view(), name='mojiPregledi'),
    path('moji-izvestaji/<int:id>/', MojiIzvestajiDetaljno.as_view(), name = 'mojiIzvestajiDetaljno'),
    path('obrisi-zahtev/', brisanjeZahteva, name='brisanjeZahteva'),
    path('otkazi-pregled/', brisanjePregleda, name='brisanjePregleda'),
    path('slobodni-termini/', slobodniTermini, name='slobodniTermini'),
    path('lista-stomatologa/', sviStomatolozi, name='sviStomatolozi'),
    path('slanje-zahteva/', posaljiZahtev, name='posaljiZahtev'),
    path('zakazi-pregled/', zakaziPregled, name='zakaziPregled'),
]