import http

from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import *
import datetime
from django.utils.dateparse import parse_date
from django.db.models import Q
from datetime import datetime, timedelta


class SveUsluge(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        usluge = Usluge.objects.all()
        serializer = UslugeSerializer(usluge, many = True)
        return Response(serializer.data)


@api_view(['POST',])
@permission_classes([])
def registracija(request):

    if request.method == 'POST':
        serializer = RegistracijaSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered'
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)


@api_view(['GET','PUT',])
@permission_classes((IsAuthenticated,))
def mojProfilView(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MojProfilPregledSerializer(korisnik)
        data = {}
        informacije = Informacije.objects.get(idK=korisnik)
        data['id'] = serializer.data['id']
        data['email'] = serializer.data['email']
        data['ime'] = informacije.ime
        data['prezime'] = informacije.prezime
        data['matbroj'] = informacije.matbroj
        data['tipK'] = informacije.tipK
        return Response(data)

    if request.method == "PUT":
        serializer = MojProfilUpdateSerializer(korisnik, data=request.data)
        updateData = request.data
        data = {}
        if serializer.is_valid():
            serializer.save()
            informacije = Informacije.objects.get(idK=korisnik)
            informacije.ime = updateData['ime']
            informacije.prezime = updateData['prezime']
            informacije.matbroj = updateData['matbroj']
            informacije.save()
            data['response'] = "Uspesno azuriran nalog"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MojiIzvestaji(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        korisnik = request.user
        informacije = Informacije.objects.get(idK=korisnik)
        if informacije.tipK == 'pacijent':
            izvestaji = Izvestaj.objects.filter(idK=korisnik)
            serializer = MojiIzvestajiSerializer(izvestaji, many=True)
        else:
            izvestaji = Izvestaj.objects.filter(idS=korisnik)
            serializer = MojiIzvestajiSerializer(izvestaji, many = True)
        return Response(serializer.data)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def logout(request):

    request.user.auth_token.delete()

    return Response("Izlogovan")

class MojiZahtevi(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        korisnik = request.user
        informacije = Informacije.objects.get(idK=korisnik)
        if informacije.tipK == 'pacijent':
            zahtevi = Zahpre.objects.filter(idK=korisnik)
            serializer = MojiZahteviSerializer(zahtevi, many=True)
        else:
            zahtevi = Zahpre.objects.filter(Q(idS=korisnik) | Q(idS_id=1)) #proveriti ovo kad se sredi baza
            serializer = MojiZahteviSerializer(zahtevi, many=True)
        return Response(serializer.data)

class MojiPregledi(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get(self, request, format=None):
        korisnik = request.user
        informacije = Informacije.objects.get(idK=korisnik)
        if informacije.tipK == 'pacijent':
            pregledi = Pregledi.objects.filter(idK=korisnik).filter(dv__gt=datetime.datetime.now())[0:6]
            serializer = MojiPreglediSerializer(pregledi, many=True)
        else:
            pregledi = Pregledi.objects.filter(idS=korisnik)
            serializer = MojiPreglediSerializer(pregledi, many=True)
        return Response(serializer.data)

class MojiIzvestajiDetaljno(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        korisnik = request.user
        data = {}
        izvestaj = Izvestaj.objects.get(idI=id)
        if izvestaj.idK != korisnik:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data['vrsta'] = izvestaj.vrsta
        data['dijagnoza'] = izvestaj.dijagnoza
        data['datum'] = izvestaj.datum
        terapija = Terapija.objects.filter(idI = id)
        serializer = TerapijaSerializer(terapija, many=True)
        data['terapija'] = serializer.data
        return Response(data)

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def brisanjeZahteva(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        informacije = Informacije.objects.get(idK=korisnik)
        data = request.data
        if informacije.tipK == 'pacijent':
            zahtev = Zahpre.objects.get(idZ=data['idZ'])
            if zahtev.idK == korisnik:
                zahtev.delete()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        elif informacije.tipK == 'stomatolog':
            zahtev = Zahpre.objects.get(idZ=data['idZ'])
            if zahtev.idS == korisnik:
                zahtev.delete()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response("Uspesno izbrisan zahtev")


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def brisanjePregleda(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        informacije = Informacije.objects.get(idK=korisnik)
        data = request.data
        if informacije.tipK == 'pacijent':
            pregled = Pregledi.objects.get(idP=data['idP'])
            if pregled.idK == korisnik:
                pregled.delete()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        elif informacije.tipK == 'stomatolog':
            pregled = Pregledi.objects.get(idP=data['idP'])
            if pregled.idS == korisnik:
                pregled.delete()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response("Uspesno obrisan pregled")

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def slobodniTermini(request):
    try:
        korisnik =  request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = request.data
        dvod = data['dvod']
        dvdo = data['dvdo']
        pregledi = Pregledi.objects.filter(dv__gte=dvod).filter(dv__lte=dvdo)
        serializer = MojiPreglediSerializer(pregledi, many=True)
        return Response(serializer.data)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def sviStomatolozi(request):

    if request.method == 'GET':
        stomatolozi = Informacije.objects.filter(tipK__exact='stomatolog')
        serializer = StomatoloziSerializer(stomatolozi, many=True)
        return Response(serializer.data)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def posaljiZahtev(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(stauts=status.HTTP_404_NOT_FOUND)

    try:
        stomatolog = Korisnik.objects.get(id=request.data['idS'])
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    korisnikInfo = Informacije.objects.get(idK=korisnik)
    if korisnikInfo.tipK != 'pacijent':
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        if request.data['idS'] == '1':
            zahtev = Zahpre(
                idK=korisnik,
                idS_id=request.data['idS'],
                dvod=request.data['dvod'],
                dvdo=request.data['dvdo'],
                opis=request.data['opis']
            )
        else:
            informacije = Informacije.objects.get(idK=stomatolog)
            if informacije.tipK == 'stomatolog':
                zahtev = Zahpre(
                    idK=korisnik,
                    idS_id=request.data['idS'],
                    dvod=request.data['dvod'],
                    dvdo=request.data['dvdo'],
                    opis=request.data['opis']
                )
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        data={}
        data['response'] = "Uspesno poslat zahtev"
        zahtev.save()
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def zakaziPregled(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    informacije = Informacije.objects.get(idK=korisnik)

    if informacije.tipK != 'stomatolog':
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        dv = request.data['dv']
        trajanje = request.data['trajanje']
        trajanje = int(trajanje)
        dv = datetime.strptime(dv, "%Y-%m-%dT%H:%M:%S%z")
        dvdo = dv + timedelta(minutes=trajanje)
        data = {}
        uslov1 = Q(idS=korisnik)
        uslov2 = Q(dv__lt=dvdo)
        uslov3 = Q(dv__gt=dv)
        pregledi = Pregledi.objects.filter(uslov1 & uslov2 & uslov3)
        if pregledi:
            return Response("Zauzet termin", status=status.HTTP_400_BAD_REQUEST)
        greska = []

        pregledi = Pregledi.objects.filter(uslov1 & uslov2)

        for p in pregledi:
            datum = p.dv
            trajanje = p.trajanje
            ukupno = datum + timedelta(minutes=trajanje)
            datum2 = datetime.strptime(request.data['dv'], "%Y-%m-%dT%H:%M:%S%z" )
            if ukupno >= datum2:
                greska.append(p)

        if len(greska)>0:
            return Response("Zauzet termin", status=status.HTTP_400_BAD_REQUEST)
        else:
            noviPregled = Pregledi(
                idS=korisnik,
                idK_id=request.data['idK'],
                opis=request.data['opis'],
                dv=request.data['dv'],
                trajanje=trajanje
            )
            noviPregled.save()
            data['poruka'] = 'Uspesno kreiran pregled'
        return Response(data, status=status.HTTP_200_OK)




