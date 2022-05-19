from rest_framework import serializers

from .models import *

class UslugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usluge
        fields = [
            "idU",
            "cena",
            "opis"
        ]


class KorisnikSerializer(serializers.ModelSerializer):

    ime = serializers.CharField()
    prezime = serializers.CharField()
    matbroj = serializers.CharField()
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



