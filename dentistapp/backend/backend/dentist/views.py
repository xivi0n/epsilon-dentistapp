import http

from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import *
from django.contrib.auth import login, authenticate

class SveUsluge(APIView):
    def get(self, request, format=None):
        usluge = Usluge.objects.all()
        serializer = UslugeSerializer(usluge, many = True)
        return Response(serializer.data)


@api_view(['POST',])
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

