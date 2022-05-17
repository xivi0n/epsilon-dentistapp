from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Korisnik)
admin.site.register(Informacije)
admin.site.register(Ocene)
admin.site.register(Usluge)
admin.site.register(Izvestaj)
admin.site.register(Lekovi)
admin.site.register(Terapija)
admin.site.register(Pitanja)
admin.site.register(Pregledi)
admin.site.register(Zahpre)
