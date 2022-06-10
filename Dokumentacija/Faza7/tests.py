from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from .models import *

# Create your tests here.


class RegistracijaTest(APITestCase):

    def testReg(self):
        data = {
            "email":"test@mail.com",
            "password":"123",
            "tipK":'pacijent',
            "matbroj":"1111111111111",
            "ime":"Imetest",
            "prezime":"prezimeTest",
        }
        response = self.client.post(reverse('registracija'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class NovaOcenaTest(APITestCase):

    def testOcena(self):
        user = Korisnik.objects.create_user('test@mail.com',  '123')
        self.client.force_authenticate(user)
        data = {
            "opis":"odlcan posao",
            "ocena":"5",
        }
        response = self.client.post(reverse('novaOcena'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SveUslugeTest(APITestCase):

    def testUsluge(self):
        usluge = Usluge.objects.create(cena='500', opis='uslugaOpis')
        response = self.client.get(reverse('sveUsluge'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BrisanjeZahtevaTest(APITestCase):

    def testZahtevi(self):
        user = Korisnik.objects.create_user('test@test.com', '123')
        stomatolog = Korisnik.objects.create_user('stom@stom.com', '223')
        zahtev = Zahpre.objects.create(idK=user, idS=stomatolog, opis='Ekstra', dvod=datetime.datetime.now(), dvdo=datetime.datetime.now())
        informacijeU = Informacije.objects.create(ime='User', prezime='PrezU', tipK='pacijent', matbroj='1231231231231', idK=user)
        informacijeS = Informacije.objects.create(ime='User2', prezime='PrezU2', tipK='stomatolog', matbroj='1231231231222', idK=stomatolog)
        self.client.force_authenticate(user)
        data = {
            'idZ':zahtev.idZ
        }
        response = self.client.post(reverse('brisanjeZahteva'), data)
        self.assertEqual(response.data, "Uspesno izbrisan zahtev")

class BrisanjePregledaTest(APITestCase):

    def testPregledi(self):
        user = Korisnik.objects.create_user('test@test.com', '123')
        stomatolog = Korisnik.objects.create_user('stom@stom.com', '223')
        informacijeU = Informacije.objects.create(ime='User', prezime='PrezU', tipK='pacijent', matbroj='1231231231231',idK=user)
        informacijeS = Informacije.objects.create(ime='User2', prezime='PrezU2', tipK='stomatolog', matbroj='1231231231222', idK=stomatolog)
        pregled = Pregledi.objects.create(idK=user, idS=stomatolog, opis='Neki opis', dv=datetime.datetime.now(), trajanje='40')
        self.client.force_authenticate(user)
        data = {
            'idP':pregled.idP
        }
        response = self.client.post(reverse('brisanjePregleda'), data)
        self.assertEqual(response.data, "Uspesno obrisan pregled")


class SviStomatoloziTest(APITestCase):

    def testStomatolozi(self):
        user = Korisnik.objects.create_user('test@test.com', '123')
        stomatolog = Korisnik.objects.create_user('stom@stom.com', '223')
        informacijeU = Informacije.objects.create(ime='User', prezime='PrezU', tipK='pacijent', matbroj='1231231231231', idK=user)
        informacijeS = Informacije.objects.create(ime='User2', prezime='PrezU2', tipK='stomatolog',matbroj='1231231231222', idK=stomatolog)
        self.client.force_authenticate(user)
        response = self.client.get(reverse('sviStomatolozi'))
        self.assertEqual(response.data[0]['idK'], stomatolog.id)


class MojProfilViewTest(APITestCase):

    def testProfil(self):
        user = Korisnik.objects.create_user('test@test.com', '123')
        informacijeU = Informacije.objects.create(ime='User', prezime='PrezU', tipK='pacijent', matbroj='1231231231231',idK=user)
        self.client.force_authenticate(user)
        response = self.client.get(reverse('mojProfil'))
        self.assertEqual(response.data['id'], user.id)


class MojiIzvestajiTest(APITestCase):

    def testIzvestaji(self):
        stomatolog = Korisnik.objects.create_user('stom@stom.com', '223')
        pacijent = Korisnik.objects.create_user('test@test.com', '123')
        informacijeU = Informacije.objects.create(ime='User', prezime='PrezU', tipK='pacijent', matbroj='1231231231231',idK=pacijent)
        informacijeS = Informacije.objects.create(ime='User2', prezime='PrezU2', tipK='stomatolog',matbroj='1231231231222', idK=stomatolog)
        izvestaj = Izvestaj.objects.create(vrsta='nekaVrsta', dijagnoza='dijagn1', datum=datetime.datetime.now(), idK=pacijent, idS=stomatolog)
        self.client.force_authenticate(stomatolog)
        response = self.client.get(reverse('mojiIzvestaji'))
        self.assertEqual(response.data[0]['idI'], izvestaj.idI)

class LogoutTest(APITestCase):

    def testLogout(self):
        pacijent = Korisnik.objects.create_user('test@test.com', '123')
        self.client.force_authenticate(pacijent)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.data, "Izlogovan")

class MojiZahteviTest(APITestCase):

    def testMojiZahtevi(self):
        user = Korisnik.objects.create_user('test@test.com', '123')
        stomatolog = Korisnik.objects.create_user('stom@stom.com', '223')
        zahtev = Zahpre.objects.create(idK=user, idS=stomatolog, opis='Ekstra', dvod=datetime.datetime.now(),dvdo=datetime.datetime.now())
        informacijeU = Informacije.objects.create(ime='User', prezime='PrezU', tipK='pacijent', matbroj='1231231231231',idK=user)
        informacijeS = Informacije.objects.create(ime='User2', prezime='PrezU2', tipK='stomatolog', matbroj='1231231231222', idK=stomatolog)
        self.client.force_authenticate(user)

        response = self.client.get(reverse('mojiZahtevi'))
        self.assertEqual(response.data[0]['idZ'], zahtev.idZ)

class MojiPreglediTest(APITestCase):

    def testMojiPregledi(self):
        user = Korisnik.objects.create_user('test@test.com', '123')
        stomatolog = Korisnik.objects.create_user('stom@stom.com', '223')
        informacijeU = Informacije.objects.create(ime='User', prezime='PrezU', tipK='pacijent', matbroj='1231231231231',idK=user)
        informacijeS = Informacije.objects.create(ime='User2', prezime='PrezU2', tipK='stomatolog',matbroj='1231231231222', idK=stomatolog)
        pregled = Pregledi.objects.create(idK=user, idS=stomatolog, opis='Neki opis', dv=datetime.datetime.now(), trajanje='40')
        self.client.force_authenticate(user)
        response = self.client.get(reverse('mojiPregledi'))
        self.assertEqual(response.data[0]['idP'], pregled.idP)

class TestPosaljiZahtev(APITestCase):

    def testPosaljiZahtev(self):
        user = Korisnik.objects.create_user('test@test.com', '123')
        stomatolog = Korisnik.objects.create_user('stom@stom.com', '223')
        informacijeU = Informacije.objects.create(ime='User', prezime='PrezU', tipK='pacijent', matbroj='1231231231231',idK=user)
        informacijeS = Informacije.objects.create(ime='User2', prezime='PrezU2', tipK='stomatolog',matbroj='1231231231222', idK=stomatolog)
        self.client.force_authenticate(user)
        data = {
            'idS':stomatolog.id,
            'dvod':datetime.datetime.now(),
            'dvdo':datetime.datetime.now(),
            'opis':'opisneki',
        }
        response = self.client.post(reverse('posaljiZahtev'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestSviLekovi(APITestCase):

    def testSviLekovi(self):
        user = Korisnik.objects.create_user('test@test.com', '123')
        self.client.force_authenticate(user)
        lek = Lekovi.objects.create(opis='Lek1')

        response = self.client.get(reverse('sviLekovi'))
        self.assertEqual(response.data[0]['idL'], lek.idL)

class TestNovoPitanje(APITestCase):

    def testNovoPitanje(self):
        data = {
            'email':'email@test.com',
            'naslov':'naslovTest',
            'opis':'opisTest',
        }

        response = self.client.post(reverse('novoPitanje'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestDohvatiPitanje(APITestCase):

    def testDohvatiPitanje(self):
        stomatolog = Korisnik.objects.create_user('stom@stom.com', '223')
        informacijeS = Informacije.objects.create(ime='User2', prezime='PrezU2', tipK='stomatolog', matbroj='1231231231222', idK=stomatolog)
        self.client.force_authenticate(stomatolog)
        pitanje = Pitanja.objects.create(email='neki email', opis='neki opis', naslov='nekinaslov')

        response = self.client.get(reverse('dohvatiPitanja'))
        self.assertEqual(response.data[0]['idP'], pitanje.idP)

class TestDohvatiPitanjePacijent(APITestCase):

    def testPacijentPitanje(self):
        user = Korisnik.objects.create_user('test@test.com', '123')
        informacijeU = Informacije.objects.create(ime='User', prezime='PrezU', tipK='pacijent', matbroj='1231231231231', idK=user)
        self.client.force_authenticate(user)
        pitanje = Pitanja.objects.create(email='neki email', opis='neki opis', naslov='nekinaslov')
        response = self.client.get(reverse('dohvatiPitanja'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TestObrisiPitanje(APITestCase):

    def testObrisiPitanje(self):
        stomatolog = Korisnik.objects.create_user('stom@stom.com', '223')
        informacijeS = Informacije.objects.create(ime='User2', prezime='PrezU2', tipK='stomatolog',matbroj='1231231231222', idK=stomatolog)
        self.client.force_authenticate(stomatolog)
        pitanje = Pitanja.objects.create(email='neki email', opis='neki opis', naslov='nekinaslov')
        data = {
            'idP':pitanje.idP
        }

        response = self.client.post(reverse('obrisiPitanje'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestDohvatiOcene(APITestCase):

    def testDohvatiOcene(self):
        user = Korisnik.objects.create_user('test@test.com', '123')
        informacijeU = Informacije.objects.create(ime='User', prezime='PrezU', tipK='pacijent', matbroj='1231231231231',idK=user)
        ocena1 = Ocene.objects.create(idK=user, ocena='5', opis='odlicno')
        ocena2 = Ocene.objects.create(idK=user, ocena='5', opis='odlicno')
        ocena3 = Ocene.objects.create(idK=user, ocena='5', opis='odlicno')
        ocena4 = Ocene.objects.create(idK=user, ocena='5', opis='odlicno')
        ocena5 = Ocene.objects.create(idK=user, ocena='5', opis='odlicno')

        response = self.client.get(reverse('dohvatiOcene'))
        self.assertEqual(response.data[0]['ime'], informacijeU.ime)