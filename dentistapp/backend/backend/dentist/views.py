from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

class SveUsluge(APIView):
    def get(self, request, format=None):
        usluge = Usluge.objects.all()
        serializer = UslugeSerializer(usluge, many = True)
        return Response(serializer.data)


