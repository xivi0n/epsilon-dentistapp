import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.core.validators import  MaxValueValidator, MinValueValidator, MinLengthValidator

# Create your models here.

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



class Korisnik(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default = False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = CustomAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class Informacije(models.Model):
    idK = models.OneToOneField(Korisnik, on_delete = models.CASCADE, primary_key = True)
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length= 30)
    matbroj = models.CharField(max_length= 13, validators=[MinLengthValidator(13)])
    slika = models.ImageField(upload_to='imgs/', null=True)
    tipK = models.CharField(max_length=20, default='pacijent')

class Ocene(models.Model):
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


class Usluge(models.Model):
    idU = models.AutoField(primary_key = True)
    cena = models.DecimalField(max_digits = 10, decimal_places=2)
    opis = models.CharField(max_length=255)

class Izvestaj(models.Model):
    idI = models.AutoField(primary_key = True)
    idK = models.ForeignKey(Korisnik, related_name = 'pacijent_izvestaj', on_delete = models.CASCADE)
    idS = models.ForeignKey(Korisnik, related_name = 'stomatolog_izvestaj', on_delete = models.CASCADE)
    vrsta = models.CharField(max_length=50)
    dijagnoza = models.TextField(max_length=1000)

class Lekovi(models.Model):
    idL = models.AutoField(primary_key = True)
    opis = models.CharField(max_length=255)

class Terapija(models.Model):
    idI = models.OneToOneField(Izvestaj, on_delete=models.CASCADE) #ovo mozda nije dobro
    idL = models.ForeignKey(Lekovi, on_delete = models.CASCADE)
    kolicina = models.CharField(max_length=100)

class Pitanja(models.Model):
    idP = models.AutoField(primary_key = True)
    idK = models.ForeignKey(Korisnik, on_delete = models.CASCADE)
    naslov = models.CharField(max_length=100)
    opis = models.TextField(max_length= 255)

class Pregledi(models.Model):
    idP = models.AutoField(primary_key = True)
    idK = models.ForeignKey(Korisnik, related_name = 'pacijent_pregled', on_delete = models.CASCADE)
    idS = models.ForeignKey(Korisnik, related_name = 'stomatolog_pregled', on_delete = models.CASCADE)
    opis = models.TextField(max_length=255)
    dv = models.DateTimeField(default = datetime.datetime.now())
    trajanje = models.IntegerField(default=0) #mozda bolje integer

class Zahpre(models.Model):
    idZ = models.AutoField(primary_key = True)
    idK = models.ForeignKey(Korisnik, related_name='pacijent_zahtev', on_delete = models.CASCADE)
    idS = models.ForeignKey(Korisnik, related_name = 'stomatolog_zahtev', on_delete = models.CASCADE)
    opis = models.CharField(max_length=255)
    dvod = models.DateTimeField(default = datetime.datetime.now())
    dvdo = models.DateTimeField(default = datetime.datetime.now())


