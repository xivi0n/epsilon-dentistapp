from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *

class UslugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usluge
        fields = [
            "idU",
            "cena",
            "opis"
        ]


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


class MojProfilPregledSerializer(serializers.ModelSerializer):

    class Meta:
        model = Korisnik
        fields = ['id', 'email']


class MojProfilUpdateSerializer(serializers.ModelSerializer):

    ime = serializers.CharField()
    prezime = serializers.CharField()
    matbroj = serializers.CharField(validators=[UniqueValidator(queryset=Informacije.objects.all())])

    class Meta:
        model = Korisnik
        fields = ['email', 'ime', 'prezime', 'matbroj']

class MojiIzvestajiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Izvestaj
        fields = ['idI', 'datum', 'vrsta']

class MojiZahteviSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zahpre
        fields = ['idZ', 'opis', 'dvod', 'dvdo', 'idK']

class MojiPreglediSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pregledi
        fields = ['idP', 'opis', 'dv', 'trajanje']

class LekoviSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lekovi
        fields = ['idL', 'opis']

class TerapijaSerializer(serializers.ModelSerializer):

    idL = LekoviSerializer()

    class Meta:
        model = Terapija
        fields = ['idI', 'kolicina', 'idL']

class StomatoloziSerializer(serializers.ModelSerializer):

    class Meta:
        model = Informacije
        fields = ['idK', 'ime', 'prezime']

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



class MojiIzvestajiPacijentSerializer(serializers.ModelSerializer):

    ime = serializers.CharField()
    prezime = serializers.CharField()

    class Meta:
        model = Izvestaj
        fields = ['idI', 'datum', 'vrsta', 'ime', 'prezime']

class MojiIzvestajiStomatologSerializer(serializers.ModelSerializer):

    ime = serializers.CharField()
    prezime = serializers.CharField()
    matbroj = serializers.CharField()

    class Meta:
        model = Izvestaj
        fields = ['idI', 'datum', 'vrsta', 'ime', 'prezime', 'matbroj']


class MojPregledSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pregledi
        fields = ['idP', 'opis', 'dv', 'trajanje', 'idK', 'idS']

class InformacijeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Informacije
        fields = ['idK','ime', 'prezime', 'matbroj', 'tipK', 'slika']

class PitanjaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pitanja
        fields = ['idP', 'naslov', 'opis', 'email']