from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *

#Nikola Krstic 0273/19
#Anja Jevtovic 0281/19


"""Klasa UslugeSerializer se koristi za serijalizaciju klase Usluge"""
class UslugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usluge
        fields = [
            "idU",
            "cena",
            "opis"
        ]


"""Klasa RegistracijaSerializer se koristi za serijalizaciju podataka za registrovanje novog korisnika,
funkcija save se koristi za cuvanje novog korisnika u bazi"""
class RegistracijaSerializer(serializers.ModelSerializer):

    ime = serializers.CharField()
    prezime = serializers.CharField()
    matbroj = serializers.CharField(validators=[UniqueValidator(queryset=Informacije.objects.all())])
    tipK = serializers.CharField()

    class Meta:
        model = Korisnik
        fields = [
            'email',
            'password',
            'ime',
            'prezime',
            'matbroj',
            'tipK',
        ]
        extra_kwargs = {
            'password':{'write_only' : True},
        }

    def save(self):
        korisnik = Korisnik(
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        korisnik.set_password(password)
        korisnik.save()
        informacije = Informacije(
            ime = self.validated_data['ime'],
            prezime = self.validated_data['prezime'],
            matbroj= self.validated_data['matbroj'],
            tipK = self.validated_data['tipK'],
            idK = korisnik
        )
        informacije.save()
        return korisnik


"""Klasa MojProfilPregledSerializer se koristi za serijalizaciju klase Pregledi"""
class MojProfilPregledSerializer(serializers.ModelSerializer):

    class Meta:
        model = Korisnik
        fields = ['id', 'email']


"""Klasa MojProfilUpdateSerializer se koristi za serijalizaciju podataka prilikom azuriranja profila korisnika"""
class MojProfilUpdateSerializer(serializers.ModelSerializer):

    ime = serializers.CharField()
    prezime = serializers.CharField()
    matbroj = serializers.CharField(validators=[UniqueValidator(queryset=Informacije.objects.all())])

    class Meta:
        model = Korisnik
        fields = ['email', 'ime', 'prezime', 'matbroj']


"""Klasa MojiIzvestajiSerializer se koristi za serijalizaciju klase Izvestaj"""
class MojiIzvestajiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Izvestaj
        fields = ['idI', 'datum', 'vrsta']

"""Klasa MojiZahteviSerializer se koristi za serijalizaciju klase Zahpre"""
class MojiZahteviSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zahpre
        fields = ['idZ', 'opis', 'dvod', 'dvdo', 'idK']

"""Klasa MojiPreglediSerializer se koristi za serijalizaciju klase Pregledi"""
class MojiPreglediSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pregledi
        fields = ['idP', 'opis', 'dv', 'trajanje']


"""Klasa LekoviSerializer se koristi za serijalizaciju klase Lekovi"""
class LekoviSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lekovi
        fields = ['idL', 'opis']

"""Klasa TerapijaSerializer se koristi za serijalizaciju klase Terapija"""
class TerapijaSerializer(serializers.ModelSerializer):

    idL = LekoviSerializer()

    class Meta:
        model = Terapija
        fields = ['idI', 'kolicina', 'idL']


"""Klasa StomatoloziSerializer se koristi za serijalizaciju informacija o stomatolozima"""
class StomatoloziSerializer(serializers.ModelSerializer):

    class Meta:
        model = Informacije
        fields = ['idK', 'ime', 'prezime']

"""Klasa ZahteviSerializer se koristi za serijalizaciju klase Zahpre,
funkcija save se koristi za cuvanje zahteva u bazi podataka"""
class ZahteviSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zahpre
        fields = ['idK', 'idS', 'dvod', 'dvdo', 'opis']

    def save(self):
        zahtev = Zahpre(
            idK=self.validated_data['idK'],
            idS = self.validated_data['idS'],
            dvod = self.validated_data['dvod'],
            dvdo = self.validated_data['dvdo'],
            opis = self.validated_data['opis']
        )
        zahtev.save()



"""Klasa MojiIzvestajiPacijentSerializer se koristi za serijalizaciju izvestaja koji su vezani za pacijenta"""
class MojiIzvestajiPacijentSerializer(serializers.ModelSerializer):

    ime = serializers.CharField()
    prezime = serializers.CharField()

    class Meta:
        model = Izvestaj
        fields = ['idI', 'datum', 'vrsta', 'ime', 'prezime']

"""Klasa MojiIzvestajiStomatologSerializer se koristi za serijalizaciju izvestaja koji su vezani za stomatologa"""
class MojiIzvestajiStomatologSerializer(serializers.ModelSerializer):

    ime = serializers.CharField()
    prezime = serializers.CharField()
    matbroj = serializers.CharField()

    class Meta:
        model = Izvestaj
        fields = ['idI', 'datum', 'vrsta', 'ime', 'prezime', 'matbroj']


"""Klasa MojPregledSerializer se koristi za serijalizaciju klase Pregled"""
class MojPregledSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pregledi
        fields = ['idP', 'opis', 'dv', 'trajanje', 'idK', 'idS']

"""Klasa InformacijeSerializer se koristi za serijalizaciju klase Informacije"""
class InformacijeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Informacije
        fields = ['idK','ime', 'prezime', 'matbroj', 'tipK', 'slika']


"""Klasa PitanjaSerializer se koristi za serijalizaciju klase Pitanja"""
class PitanjaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pitanja
        fields = ['idP', 'naslov', 'opis', 'email']


"""Klasa OceneSerializer se koristi za serijalizaciju klase Ocene"""
class OceneSerializer(serializers.ModelSerializer):

    ime = serializers.CharField()
    prezime = serializers.CharField()

    class Meta:
        model = Ocene
        fields = ['idO', 'ocena', 'opis', 'ime', 'prezime']