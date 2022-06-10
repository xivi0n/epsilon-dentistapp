from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

#Nikola Krstic 0273/19
#Anja Jevtovic 0281/19

urlpatterns = [
    path('sve-usluge/', SveUsluge.as_view(), name='sveUsluge'),
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
    path('zauzeti-termini/', zauzetiTermini, name='slobodniTermini'),
    path('lista-stomatologa/', sviStomatolozi, name='sviStomatolozi'),
    path('slanje-zahteva/', posaljiZahtev, name='posaljiZahtev'),
    path('zakazi-pregled/', zakaziPregled, name='zakaziPregled'),
    path('svi-lekovi/', sviLekovi, name='sviLekovi'),
    path('nov-izvestaj/', novIzvestaj, name='novIzvestaj'),
    path('pregled/<int:id>/', DohvatiPregled.as_view(), name = 'dohvatiPregled'),
    path('korisnik/<int:id>/', DohvatiKorisnika.as_view(), name = 'dohvatiKorisnika'),
    path('novo-pitanje/', novoPitanje, name='novoPitanje'),
    path('pitanja/', dohvatiPitanja, name = 'dohvatiPitanja'),
    path('obrisi-pitanje/', obrisiPitanje, name='obrisiPitanje'),
    path('odgovori/', odgovoriNaPitanje, name='odgovoriNaPitanje'),
    path('nova-ocena/', novaOcena, name='novaOcena'),
    path('ocene/', dohvatiOcene, name='dohvatiOcene')
]