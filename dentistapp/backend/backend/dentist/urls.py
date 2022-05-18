from django.urls import path, include
from .views import *


urlpatterns = [
    path('sve-usluge/', SveUsluge.as_view()),
]