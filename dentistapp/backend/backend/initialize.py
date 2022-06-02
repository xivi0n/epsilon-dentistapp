from dentist.models import *
from django.contrib.auth.hashers import make_password
import datetime
from django.contrib.auth.models import User
import random

def initKorisnik():
    # NAPRAVITI SUPERUSERA PRE OVOGA
    k = Korisnik(email='anja.jevtovic@dentisapp.com', id=2, password=make_password('123'))
    k.save()
    k1 = Korisnik(email='nikola.krstic@dentisapp.com', id=3, password=make_password('123'))
    k1.save()
    k2 = Korisnik(email='mihailo.jovanovic@dentisapp.com', id=4, password = make_password('123'))
    k2.save()
    k3 = Korisnik(email='aleksa.vladic@dentisapp.com', id=5, password = make_password('123'))
    k3.save()

    i = Informacije.create(k, 'Anja', 'Jevtovic', 1712000443322, 'Picture1.png', 'pacijent')
    i.save()
    i1 = Informacije.create(k1, 'Nikola', 'Krstic', 1411000443322, 'Picture1.png', 'pacijent')
    i1.save()
    i2 = Informacije.create(k2, 'Mihailo', 'Jovanovic', 1212000443322, 'Picture1.png', 'stomatolog')
    i2.save()
    i3 = Informacije.create(k3, 'Aleksa', 'Vladic', 1515000443322, 'Picture1.png', 'stomatolog')
    i3.save()

def initOcene():
    text_ocene = [
        'Izuzetno prijatan ambijent sa prelepim morskim akvarijumom',
        'izuzetno prijatani doktor i sestra učiniće da potpuno zaboravite da se nalazite u stomatološkoj stolici',
        'Od mene najviša ocena!!!',
        'Super anestezija, nisam nista osetila!',
        'Moja topla preporuka!'
        'Zaista su se potrudili da se osecam kao kod kuce :)',
        'Sigurno cu ih opet'
    ]

    for j in range(2):
        for i in range(2, Korisnik.objects.count()):
            k = Korisnik.objects.get(id=i)
            o = Ocene(idK=k, ocena=random.randint(4,5), opis=text_ocene[random.randint(0, len(text_ocene) - 1)])
            o.save()

def initUsluge():
    usluge = [
        ('Stomatološki pregled', 1000),
        ('Specijalistički pregled', 1500),
        ('Kompozitni ispun', 2000),
        ('Lečenje inficiranog kanala', 2000),
        ('Terapija dubokog karijesa', 3000),
        ('Rutinsko vađenje zuba', 2000),
        ('Komplikovano vađenje zuba', 3000),
        ('Hirurško vađenje zuba', 6000),
        ('Resekcija zuba', 10000),
        ('Cistektomija', 12000),
        ('Nivelacija grebena', 6000),
        ('Fluorizacija zuba', 1000),
        ('Hirurška odbrana paradoncijuma', 4000),
        ('Totalna proteza', 25000),
        ('Direktno podlaganje proteze', 4000),
        ('Teleskop krunica', 13000),
        ('Fiberglas kočić', 6000),
        ('Folija protiv bruksizma', 8500),
        ('Ugradnja implanta sa abatmentom', 50000),
        ('Beljenje zuba po vilici', 12000),
    ]

    for i, us in enumerate(usluge):
        u = Usluge.create(i + 1, us[1], us[0])
        u.save()

def initLekovi():
    lekovi = [
        'Ampicilin',
        'Amoksicilin',
        'Benzilpenicilin',
        'Aspirin',
        'Paracetamol',
        'Febricet',
        'Kafetin',
        'Kodein',
        'Metadon',
        'Fentanyl',
        'Aspirin',
        'Analgin',
        'Panadol'
    ]

    for i, l in enumerate(lekovi):
        l = Lekovi.create(i + 1, l)
        l.save()

def initPitanja():
    pitanja = [
        ("Stomatološki problem", "Imam bol u zubu, kojim lekovima bih mogao da ublažim?"),
        ("Tehnički problem", "Ne umem da se registrujem, možete li mi pomoći?"),
        ("Informacije", "Da li doktor Jovan radi sutra prvu ili drugu smenu?"),
    ]
    for i in range(len(pitanja)):
        k = Korisnik.objects.get(id=i+2)
        p_t = pitanja[i]
        p = Pitanja(email="mihailo.jovanovich@gmail.com", naslov=p_t[0], opis=p_t[1])
        p.save()

def initPregledi():
    st = Korisnik.objects.get(id=5)
    k1 = Korisnik.objects.get(id=4)
    k2 = Korisnik.objects.get(id=3)

    pr = Pregledi.create(1, k1, st, "Endodoncija", datetime.datetime(2022, 6, 2, 15, 00), 60)
    pr.save()
    pr1 = Pregledi.create(2, k1, st, "Rekonstruktivna stomatologija",datetime.datetime(2022, 6, 2, 16, 00), 75)
    pr1.save()
    pr2 = Pregledi.create(3, k2, st, "Estetska stomatologija",datetime.datetime(2022, 6, 2, 17, 15), 90)
    pr2.save()

def initZahpre():
    st = Korisnik.objects.get(id=5)
    k1 = Korisnik.objects.get(id=4)
    k2 = Korisnik.objects.get(id=3)

    z = Zahpre(idZ = 1, idK = k1, idS = st, opis = 'Voleo bih da izeblim zube', dvod = datetime.datetime(2022, 6, 2, 12, 00) , dvdo =datetime.datetime(2022, 6, 2, 16, 00))
    z.save()
    z1 = Zahpre(idZ = 2, idK = k1, idS = st, opis = 'Boli me zub, verovatno bih ga izvadila', dvod = datetime.datetime(2022, 6, 2, 15, 30), dvdo = datetime.datetime(2022, 6, 2, 19, 30))
    z1.save()
    z2 = Zahpre(idZ = 3, idK = k2, idS = st, opis = 'Trebalo bi da uklonim protezu', dvod = datetime.datetime(2022, 6, 2, 10, 00), dvdo = datetime.datetime(2022, 6, 2, 18, 00))
    z2.save()

def initIzvestaj():
    st = Korisnik.objects.get(id=5)
    k1 = Korisnik.objects.get(id=4)
    k2 = Korisnik.objects.get(id=3)
    k3 = Korisnik.objects.get(id=3)
    k4 = Korisnik.objects.get(id=3)
    iz = Izvestaj(idK=k1, idS=st, vrsta='Kompozitni ispun', dijagnoza='Veoma je bitno pratiti temperaturu, u slučaju povišene temperature obavezno pozvati ordinaciju', datum=datetime.datetime(2022, 6, 2, 10, 00))
    iz.save()
    iz1 = Izvestaj(idK=k1, idS=st, vrsta='Resekcija zuba', dijagnoza='Stavljati hladne obloge i skenirati zub sledeće nedelje', datum=datetime.datetime(2022, 6, 2, 10, 00))
    iz1.save()
    iz2 = Izvestaj(idK=k2, idS=st, vrsta='Beljenje zuba po vilici', dijagnoza='Sve je prošlo kako treba, dodatno izbeljivanje je moguće tek za mesec dana', datum=datetime.datetime(2022, 6, 2, 10, 00))
    iz2.save()
    iz3 = Izvestaj(idK=k3, idS=st, vrsta='Fluorizacija zuba', dijagnoza='Stabilni zubi, ako osetite neku bol javite se', datum=datetime.datetime(2022, 6, 2, 10, 00))
    iz3.save()
    iz4 = Izvestaj(idK=k4, idS=st, vrsta='Hirurško vađenje zuba', dijagnoza='Postoji mogućnost otoka, pratiti stanje i javiti se ako nastane problem', datum=datetime.datetime(2022, 6, 2, 10, 00))
    iz4.save()

    kolicine = ["2x 1", "3x 2", "1x 1", "5x 1", "1x 5"]
    for i in range(random.randint(0, 3)):
        t = Terapija.create(iz, Lekovi.objects.get(idL=random.randint(1, Lekovi.objects.count())), random.choice(kolicine))
        t.save()
    
    for i in range(random.randint(0, 2)):
        t = Terapija.create(iz1, Lekovi.objects.get(idL=random.randint(1, Lekovi.objects.count())), random.choice(kolicine))
        t.save()

    for i in range(random.randint(0, 5)):
        t = Terapija.create(iz2, Lekovi.objects.get(idL=random.randint(1, Lekovi.objects.count())), random.choice(kolicine))
        t.save()

    for i in range(random.randint(0, 2)):
        t = Terapija.create(iz3, Lekovi.objects.get(idL=random.randint(1, Lekovi.objects.count())), random.choice(kolicine))
        t.save()

    for i in range(random.randint(0, 4)):
        t = Terapija.create(iz4, Lekovi.objects.get(idL=random.randint(1, Lekovi.objects.count())), random.choice(kolicine))
        t.save()

def init():
    initKorisnik()
    initOcene()
    initUsluge()
    initLekovi()
    initPitanja()
    initPregledi()
    initZahpre()
    initIzvestaj()