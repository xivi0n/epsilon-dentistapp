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
from django.core.mail import EmailMessage
import json

# Nikola Krstic 0273/19
# Anja Jevtovic 0281/19


"""
SveUsluge - Klasa za dohvatanje svih usluga iz baze
"""
class SveUsluge(APIView):
    authentication_classes = []
    permission_classes = []

    """funkcija get vraca sve usluge"""
    def get(self, request, format=None):
        usluge = Usluge.objects.all()
        serializer = UslugeSerializer(usluge, many = True)
        return Response(serializer.data)



"""funkcija registracija koristi se za registrovanje novog korisnika na osnovu podataka koje korisnik unosi
povratna vrednost je infromacija o korisniku i http status"""
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



"""funkcija mojProfilView se koristi za dohvatanje podataka o profilu za korisnika koji je pozove
ukoliko je metoda GET povratna vrednost su informacije o korisniku, a ukoliko je metoda put
azuriraju se podaci korisnika u bazi i povratna vrednost je poruka o uspesnosti """
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


"""klasa MojiIzvestaji se koristi za dohvatanje izvestaja vezanih za korisnike"""
"""funkcija get se koristi za dohvatanje izvestaja"""
class MojiIzvestaji(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        korisnik = request.user
        data = []
        dataSerializer = {}
        informacije = Informacije.objects.get(idK=korisnik)
        if informacije.tipK == 'pacijent':
            izvestaji = Izvestaj.objects.filter(idK=korisnik)
            for i in izvestaji:
                info = Informacije.objects.get(idK=i.idS)
                dataSerializer['ime'] = info.ime
                dataSerializer['prezime'] = info.prezime
                dataSerializer['datum'] = i.datum
                dataSerializer['idI'] = i.idI
                dataSerializer['vrsta'] = i.vrsta
                serializer = MojiIzvestajiPacijentSerializer(dataSerializer)
                data.append(serializer.data)
        else:
            izvestaji = Izvestaj.objects.filter(idS=korisnik)
            for i in izvestaji:
                info = Informacije.objects.get(idK=i.idK)
                dataSerializer['ime'] = info.ime
                dataSerializer['prezime'] = info.prezime
                dataSerializer['matbroj'] = info.matbroj
                dataSerializer['datum'] = i.datum
                dataSerializer['idI'] = i.idI
                dataSerializer['vrsta'] = i.vrsta
                serializer = MojiIzvestajiStomatologSerializer(dataSerializer)
                data.append(serializer.data)
        return Response(data)


"""funkcija logout se koristi za odjavljivanje korisnika iz sistema, brisanjem tokena iz baze"""
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def logout(request):

    request.user.auth_token.delete()

    return Response("Izlogovan")


"""Klasa MojiZahtevi se koristi za dohvatanje zahteva korisnika iz baze podataka"""
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


"""Klasa MojiPregledi se koristi za dohvatanje pregleda korisnika iz baze podataka"""
class MojiPregledi(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get(self, request, format=None):
        korisnik = request.user
        informacije = Informacije.objects.get(idK=korisnik)
        if informacije.tipK == 'pacijent':
            pregledi = Pregledi.objects.filter(idK=korisnik)
            serializer = MojiPreglediSerializer(pregledi, many=True)
        else:
            pregledi = Pregledi.objects.filter(idS=korisnik)
            serializer = MojiPreglediSerializer(pregledi, many=True)
        return Response(serializer.data)


"""Klasa MojiIzvestajiDetaljno se koristi za dohvatanje detaljnih informacija vezanih za izvestaj korisnika"""
class MojiIzvestajiDetaljno(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        korisnik = request.user
        data = {}
        informacije = Informacije.objects.get(idK=korisnik)
        izvestaj = Izvestaj.objects.get(idI=id)
        if izvestaj.idK != korisnik and izvestaj.idS != korisnik:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if informacije.tipK == 'stomatolog':
            pacijent = Informacije.objects.get(idK=izvestaj.idK)
            data['vrsta'] = izvestaj.vrsta
            data['dijagnoza'] = izvestaj.dijagnoza
            data['datum'] = izvestaj.datum
            data['matbroj'] = pacijent.matbroj
            data['ime'] = pacijent.ime
            data['prezime'] = pacijent.prezime
            terapija = Terapija.objects.filter(idI = id)
            serializer = TerapijaSerializer(terapija, many=True)
            data['terapija'] = serializer.data
        else:
            stomatolog = Informacije.objects.get(idK=izvestaj.idS)
            data['vrsta'] = izvestaj.vrsta
            data['dijagnoza'] = izvestaj.dijagnoza
            data['datum'] = izvestaj.datum
            data['ime'] = stomatolog.ime
            data['prezime'] = stomatolog.prezime
            terapija = Terapija.objects.filter(idI=id)
            serializer = TerapijaSerializer(terapija, many=True)
            data['terapija'] = serializer.data

        return Response(data)

"""funkcija brisanjeZahteva se koristi za brisanje zahteva za pregled iz baze podataka, povratna vrednost
je poruka o uspesnosti funkcije"""
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
            if zahtev.idS == korisnik or zahtev.idS == Korisnik.objects.get(id=1):
                zahtev.delete()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response("Uspesno izbrisan zahtev")


"""funkcija brisanjePregleda se koristi za brisanje pregleda iz baze podataka, povratna vrednost je
poruka o uspesnosti funkcije"""
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


"""funkcija zauzetiTermini se koristi za dohvatanje svih zauzetih termina za neki datum,
povratna vrednost funkcije su zauzeti termini u zeljenom datumu"""
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def zauzetiTermini(request):
    try:
        korisnik =  request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    info = Informacije.objects.get(idK=korisnik)

    if request.method == 'GET':
        datum = request.GET.get('datum', '')
        godina = datum[:4]
        mesec = datum[5:7]
        dan = datum[8:10]
        if info.tipK == 'stomatolog':
            termini = Pregledi.objects.filter(dv__year=godina).filter(dv__month=mesec).filter(dv__day=dan).filter(idS=korisnik)
        else:
            idS = request.GET.get('idS', '')
            idS = int(idS)
            termini = Pregledi.objects.filter(dv__year=godina).filter(dv__month=mesec).filter(dv__day=dan).filter(idS_id=idS)
        serializer = MojiPreglediSerializer(termini, many=True)
        return Response(serializer.data)


"""funkcija sviStomatolozi se koristi za dohvatanje svih stomatologa iz baze podataka,
povratna vrednost funkcije je lista stomatologa"""
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def sviStomatolozi(request):

    if request.method == 'GET':
        stomatolozi = Informacije.objects.filter(tipK__exact='stomatolog')
        serializer = StomatoloziSerializer(stomatolozi, many=True)
        return Response(serializer.data)


"""funkcija posaljiZahtev se koristi za slanje zahteva za pregled od strane pacijenta
na osnovu podataka se pamti zahtev u bazi, povratna vrednost je http status i poruka o uspesnosti"""
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


"""funkcija zakaziPregled se koristi za zakazivanje pregleda od strane stomatologa, 
na osnovu podataka, ukoliko je termin slobodan vrsi se upis pregleda u bazu,
povratna vrednost je poruka o uspesnosti i http status"""
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
        dv = datetime.strptime(dv, "%Y-%m-%dT%H:%M:%S.%f%z")
        dvdo = dv + timedelta(minutes=trajanje)
        data = {}
        uslov1 = Q(idS=korisnik)
        uslov2 = Q(dv__lt=dvdo)
        uslov3 = Q(dv__gt=dv)
        pregledi = Pregledi.objects.filter(uslov1 & uslov2 & uslov3)
        if pregledi:
            return Response("Zauzet termin", status=status.HTTP_400_BAD_REQUEST)

        pregledi = Pregledi.objects.filter(uslov1 & uslov2)

        for p in pregledi:
            datum = p.dv
            trajanje = p.trajanje
            ukupno = datum + timedelta(minutes=trajanje)
            datum2 = datetime.strptime(request.data['dv'], "%Y-%m-%dT%H:%M:%S.%f%z")
            if ukupno > datum2:
                return Response("Zauzet termin", status=status.HTTP_400_BAD_REQUEST)

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


"""funkcija sviLekovi se koristi za dohvatanje svih lekova iz baze podataka,
povratna vrednost je lista lekova iz baze"""
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def sviLekovi(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        lekovi = Lekovi.objects.all()
        serializer = LekoviSerializer(lekovi, many=True)

    return Response(serializer.data)


"""funkcija novIzvestaj se koristi za kreiranje novog izvestaja od strane stomatologa,
na osnovu prosledjenih podataka vrsi se upis informacija u bazu, povratna vrednost je http status"""
@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def novIzvestaj(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    informacije = Informacije.objects.get(idK=korisnik)
    if informacije.tipK == 'pacijent':
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        matbroj = request.data['matbroj']
        vrsta = request.data['vrsta']
        terapija = request.data['terapija']
        dijagnoza = request.data['dijagnoza']
        datum = request.data['datum']
        info = Informacije.objects.get(matbroj=matbroj)
        izvestaj = Izvestaj(
            idS=korisnik,
            idK=info.idK,
            vrsta = vrsta,
            dijagnoza=dijagnoza,
            datum=datum
        )
        izvestaj.save()
        for i in range(len(terapija)):
            novaTerapija = Terapija(
                idI=izvestaj,
                idL_id=terapija[i]['idL'],
                kolicina=terapija[i]['kolicina']
            )
            novaTerapija.save()

        return Response(status=status.HTTP_200_OK)



"""Klasa DohvatiPregled se koristi za dohvatanje odredjenog pregleda korisnika
funkcija get na osnovu prosledjenog id dohvata iz baze pregled, povratna vrednost je pregled"""
class DohvatiPregled(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        pregled = Pregledi.objects.filter(idP=id)
        if not pregled:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MojPregledSerializer(pregled, many=True)
        return Response(serializer.data)


"""Klasa DohvatiKorisnika se koirsti za dohvatanje korisnika iz baze podataka
funkcija get na osnovu prosledjenog id dohvata korisnika sa tim id iz baze podataka,
povratna vrednost funkcije su informacije o tom korisniku"""
class DohvatiKorisnika(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        try:
            korisnik = request.user
        except Korisnik.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        infoK = Informacije.objects.get(idK=korisnik)

        if infoK.tipK == 'pacijent':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        informacije = Informacije.objects.get(idK_id=id)
        serializer = InformacijeSerializer(informacije)

        return Response(serializer.data)


"""funkcija novoPitanje se koristi za upis novog pitanja u bazu podataka,
na osnovu prosledjenih podataka, pitanje se cuva u bazi, povratna vrednost je http status"""
@api_view(['POST',])
@permission_classes(())
def novoPitanje(request):

    if request.method == 'POST':
        email = request.data['email']
        naslov = request.data['naslov']
        opis = request.data['opis']

        novoP = Pitanja(
            email=email,
            naslov=naslov,
            opis=opis
        )
        novoP.save()
        return Response(status=status.HTTP_200_OK)

"""funkcija dohvatiPitanja se koristi od strane stomatologa da dohvati sva pitanja iz baze,
povratna vrednost funkcije je lista pitanja"""
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def dohvatiPitanja(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    info = Informacije.objects.get(idK=korisnik)

    if info.tipK == 'pacijent':
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        pitanja = Pitanja.objects.all()

        serializer = PitanjaSerializer(pitanja, many=True)

        return Response(serializer.data)


"""funkcija obrisiPitanje se koristi za brisanje pitanja iz baze na osnovu id koji je prosledjen,
povratna vrednost funkcije je http status"""
@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def obrisiPitanje(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    info = Informacije.objects.get(idK=korisnik)

    if info.tipK == 'pacijent':
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        id = request.data['idP']
        pitanje = Pitanja.objects.get(idP=id)
        pitanje.delete()
        return Response(status=status.HTTP_200_OK)


"""funkcija odgovoriNaPitanje se koristi od strane stomatologa za odgovaranje na odredjeno pitanje korisnika,
funkcija salje email korisniku na adresu prosledjenu u zahtevu, povratna vrednost je http status"""
@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def odgovoriNaPitanje(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    info = Informacije.objects.get(idK=korisnik)

    if info.tipK == 'pacijent':
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        emailTo = request.data['email']
        #emailTo = 'dentistapp4@gmail.com'
        naslov = request.data['naslov']
        odgovor = request.data['odgovor']

        email = EmailMessage(naslov, odgovor, to=[emailTo])
        email.send()
        return Response(status=status.HTTP_200_OK)


"""funkcija novaOcena se koristi za upis ocene u bazu podataka,
povratna vrednost je http status"""
@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def novaOcena(request):
    try:
        korisnik = request.user
    except Korisnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        opis = request.data['opis']
        ocena = request.data['ocena']
        nova = Ocene(
            ocena=ocena,
            opis=opis,
            idK=korisnik,
        )
        nova.save()
        return Response(status=status.HTTP_200_OK)

"""funkcija dohvatiOcene se koristi za dohvatanje poslednjih 5 ocena iz baze podataka,
povratna vrednost su ocene"""
@api_view(['GET',])
@permission_classes(())
def dohvatiOcene(request):

    if request.method == "GET":
        data = {}
        returnData = []
        ocene = Ocene.objects.all()[0:5]
        for o in ocene:
            idK = o.idK
            info = Informacije.objects.get(idK=idK)
            ime = info.ime
            prezime = info.prezime
            data['ime'] = ime
            data['prezime'] = prezime
            data['idO'] = o.idO
            data['opis'] = o.opis
            data['ocena'] = o.ocena
            serializer = OceneSerializer(data)
            returnData.append(serializer.data)
        return Response(returnData)