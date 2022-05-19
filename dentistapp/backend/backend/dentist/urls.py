from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('sve-usluge/', SveUsluge.as_view()),
    path('registracija/', registracija, name = 'registracija'),
    path('login/', obtain_auth_token, name = "login"),
]