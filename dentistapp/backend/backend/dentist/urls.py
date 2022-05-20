from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('sve-usluge/', SveUsluge.as_view()),
    path('registracija/', registracija, name = 'registracija'),
    path('login/', obtain_auth_token, name = "login"),
    path('moj-profil/', mojProfilView, name = 'mojProfil'),
    path('moji-izvestaji/', MojiIzvestaji.as_view(), name = 'mojiIzvestaji')
]