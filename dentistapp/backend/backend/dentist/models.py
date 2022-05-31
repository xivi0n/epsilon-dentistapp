import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.core.validators import  MaxValueValidator, MinValueValidator, MinLengthValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

#Nikola Krstic 0273/19
#Anja Jevtovic 0281/19

"""Klasa CustomAccountManager se koristi za kreiranje korisnika
funkcija create_user se koristi za kreiranje obicnog korisnika,
funkcija create_superuser se koristi za kreiranje superusera"""
class CustomAccountManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Morate imati email adresu.")
        user = self.model(
            email = email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email = email,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)



"""Klasa Korisnik se koristi za modelovanje Korisnika u bazi podataka"""
class Korisnik(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default = False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


"""Klasa Informacije se koristi za modelovanje Informacija u bazi podataka,
funkcija create se koristi za kreiranje objekta klase Informacije"""
class Informacije(models.Model):

    @classmethod
    def create(cls, idK, ime, prezime, matbroj, slika, tipK):
        return cls(idK = idK, ime = ime, prezime = prezime, matbroj = matbroj, slika = slika, tipK= tipK)

    idK = models.OneToOneField(Korisnik, on_delete = models.CASCADE, primary_key = True)
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length= 30)
    matbroj = models.CharField(max_length= 13, validators=[MinLengthValidator(13)], unique=True)
    slika = models.ImageField(upload_to='imgs/', null=True, blank=True) #dodao
    tipK = models.CharField(max_length=20, default='pacijent')


"""Klasa Ocene se koristi za modelovanje Ocena u bazi podataka,
funkcija create se koristi za kreiranje objekta klase Ocene"""
class Ocene(models.Model):

    @classmethod
    def create(cls, idK, idO, ocena, opis):
        return cls(idK=idK, idO=idO, ocena = ocena, opis = opis)

    idK = models.ForeignKey(Korisnik, on_delete = models.CASCADE)
    idO = models.AutoField(primary_key = True)
    ocena = models.IntegerField(
        default = 1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    opis = models.CharField(max_length=255)

"""Klasa Usluge se koristi za modelovanje usluga u bazi podataka,
funkcija create se koristi za kreiranje objekta klase Usluge"""
class Usluge(models.Model):

    @classmethod
    def create(cls, idU, cena, opis):
        return cls(idU=idU, cena=cena, opis=opis)

    idU = models.AutoField(primary_key=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    opis = models.CharField(max_length=255)

"""Klasa Izvestaj se koristi za modelovanje izvestaja u bazi podataka,
funkcija create se koristi za kreiranje objekta klase Izvestaj"""
class Izvestaj(models.Model):

    @classmethod
    def create(cls, idI, idK, idS, vrsta, dijagnoza):
        return cls(idI=idI, idK=idK, idS=idS, vrsta=vrsta, dijagnoza=dijagnoza)

    idI = models.AutoField(primary_key = True)
    idK = models.ForeignKey(Korisnik, related_name = 'pacijent_izvestaj', on_delete = models.CASCADE)
    idS = models.ForeignKey(Korisnik, related_name = 'stomatolog_izvestaj', on_delete = models.CASCADE)
    vrsta = models.CharField(max_length=50)
    dijagnoza = models.TextField(max_length=1000)
    datum = models.DateTimeField(default = datetime.datetime.now())


"""Klasa Lekovi se koristi za modelovanje Lekova u bazi podataka,
funkcija create se koristi za kreiranje objekta klase Lekovi"""
class Lekovi(models.Model):

    @classmethod
    def create(cls, idL, opis):
        return cls(idL=idL, opis=opis)

    idL = models.AutoField(primary_key = True)
    opis = models.CharField(max_length=255)


"""Klasa Terapija se koristi za modelovanje Tereapije u bazi podataka,
funkcija create se koristi za kreiranje objekta klase Terapija"""
class Terapija(models.Model):

    @classmethod
    def create(cls, idI, idL, kolicina):
        return cls(idI = idI, idL=idL, kolicina=kolicina)

    idI = models.ForeignKey(Izvestaj, on_delete=models.CASCADE) #ovo mozda nije dobro
    idL = models.ForeignKey(Lekovi, on_delete = models.CASCADE)
    kolicina = models.CharField(max_length=100)


"""Klasa Pitanja se koristi za modelovanje Pitanja u bazi podataka,
funkcija create se koristi za kreiranje objekta klase Pitanja"""
class Pitanja(models.Model):

    @classmethod
    def create(cls, idP, idK, naslov, opis):
        return cls(idP=idP, idK=idK, naslov=naslov, opis=opis)

    idP = models.AutoField(primary_key = True)
    email = models.EmailField(max_length=100, default="")
    naslov = models.CharField(max_length=100)
    opis = models.TextField(max_length= 255)


"""Klasa Pregledi se koristi za modelovanje Pregleda u bazi podataka,
funkcija create se koristi za kreiranje objekta klase Pregledi"""
class Pregledi(models.Model):

    @classmethod
    def create(cls, idP, idK, idS, opis, dv, trajanje):
        return cls(idP=idP, idK=idK, idS=idS, opis = opis, dv = dv, trajanje = trajanje)

    idP = models.AutoField(primary_key = True)
    idK = models.ForeignKey(Korisnik, related_name = 'pacijent_pregled', on_delete = models.CASCADE)
    idS = models.ForeignKey(Korisnik, related_name = 'stomatolog_pregled', on_delete = models.CASCADE)
    opis = models.TextField(max_length=255)
    dv = models.DateTimeField(default = datetime.datetime.now())
    trajanje = models.IntegerField(default=0) #mozda bolje integer


"""Klasa Zahpre se koristi za modelovanje zahteva za pregled u bazi podataka,
funkcija create se koristi za kreiranje objekta klase Zahpre"""
class Zahpre(models.Model):

    idZ = models.AutoField(primary_key = True)
    idK = models.ForeignKey(Korisnik, related_name='pacijent_zahtev', on_delete = models.CASCADE)
    idS = models.ForeignKey(Korisnik, related_name = 'stomatolog_zahtev', on_delete = models.CASCADE)
    opis = models.CharField(max_length=255)
    dvod = models.DateTimeField(default = datetime.datetime.now())
    dvdo = models.DateTimeField(default = datetime.datetime.now())


"""funkcija create_auth_token se koristi za kreiranje tokena za autentikaciju korisnika"""
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
