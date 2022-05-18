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


