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




