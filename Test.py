#1 – Esittely

#Tämä video opettaa Pythonin perusteet aloittelijalle.
#Esittele itsesi ja kerro lyhyesti ohjelmointitaustasi.

#Koodi:

print("Tervetuloa Python-opetukseen!")  
# Tulostaa viestin näytölle, kertoo videon aloituksen

#2– Pythonin esittely

#Python on helppo, selkeä ja monipuolinen ohjelmointikieli.
#Käytetään mm. web-kehityksessä, tietojenkäsittelyssä, tekoälyssä ja automaatiossa.
#Tulkattava kieli: koodi suoritetaan riviltä riville ilman erillistä käännöstä.
#Eroaa muista kielistä selkeydellä ja vähäisellä sulkujen käytöllä.

#Koodi:


print("Python on helppo ja monipuolinen ohjelmointikieli!")  
# Tulostaa näytölle Pythonin kuvauksen


#3 – Muuttujat

#Muuttuja on nimetty säiliö tiedolle (teksti, luku, totuusarvo).
#Nimeämisrajoituksia: ei numeroa alussa, ei erikoismerkkejä (paitsi _).
#Hyvä nimi kuvaa muuttujan sisältöä (esim. nimi, ika).

#Koodi:

nimi = "Mikko"   # Tekstimuotoinen muuttuja
ika = 25         # Kokonaisluku
pisteet = 88.5   # Liukuluku
print(nimi, ika, pisteet)  # Tulostaa kaikki muuttujat näytölle



#4 – Syötteet ja tulostaminen

#Teoria:
#input() ottaa käyttäjän syötteen näppäimistöltä.
#Syöte on aina teksti, voidaan muuntaa int() avulla kokonaisluvuksi.
#print() tulostaa tekstin ja muuttujia voi yhdistää +, , tai f-merkkijonolla.
#Erikoismerkit voidaan käsitellä -merkinnällä.

#Koodi:

# Pyydetään käyttäjältä nimi
nimi = input("Anna nimesi: ")

# Pyydetään ikä ja yritetään muuntaa se kokonaisluvuksi
ika_syote = input("Anna ikäsi: ")
try:
    ika = int(ika_syote)
    print(f"Hei {nimi}, olet {ika} vuotta vanha!")
except ValueError:
    print("Virhe: ikä pitää antaa numerona.")



# 5 – Merkkijonot

#Merkkijono = teksti.
#len() kertoo merkkijonon pituuden.
#[alku:loppu] leikkaa osan merkkijonosta.
#Toistaminen *-operaattorilla.
##Valmisfunktiot: upper(), lower(), strip(), replace(), split().

#Koodi:

teksti = "  Hei Python  "                   # Merkkijono, jossa on välilyöntejä
print(len(teksti))                          # Tulostaa merkkijonon pituuden
print(teksti.strip())                       # Poistaa välilyönnit alusta ja lopusta
print(teksti.upper())                       # Muuttaa kaikki kirjaimet isoiksi
print(teksti.replace("Python","Maailma"))  # Korvaa sanan "Python" sanalla "Maailma"
print(teksti*2)                             # Toistaa merkkijonon kaksi kertaa



#6 – Valintarakenteet (if-lause)
#if-lause suorittaa koodilohkon, jos ehto on tosi.
#if-else: jos ehto epätosi, suoritetaan toinen lohko.
#if-elif-else: useita ehtoja peräkkäin.
#Sisennys määrittää lohkon.
#Vertailut: ==, !=, <, >, <=, >=, in, not in.
#Ehdot voidaan yhdistää: and, or, not.

#Koodi:

ika = 20
if ika >= 18:              # Tarkistaa, onko käyttäjä täysi-ikäinen
    print("Olet täysi-ikäinen")  # Suoritetaan, jos ehto on tosi
elif ika >= 13:            # Jos ensimmäinen ehto epätosi, tarkistetaan tämä
    print("Olet teini")     # Suoritetaan, jos ehto on tosi
else:                       # Jos mikään yllä olevista ehdoista ei ole tosi
    print("Olet lapsi")     # Suoritetaan tämä


#7 Toistorakenteet
#Toistorakenne suorittaa koodia useita kertoja.
#while: toistaa niin kauan kuin ehto on tosi.

#for: käy läpi jonon tai range() määrän.
#break keskeyttää, continue hyppää seuraavaan kierrokseen, pass ei tee mitään.
#else voidaan käyttää, jos silmukka päättyy normaalisti.

#Koodi:

for i in range(5):         # Toistaa silmukan 5 kertaa (0–4)
    if i == 3:              
        continue           # Ohittaa kierroksen, jos i on 3
    print(i)               # Tulostaa i:n arvon

laskuri = 0
while laskuri < 3:         # Toistaa niin kauan kuin laskuri on pienempi kuin 3
    print("Laskuri:", laskuri)  
    laskuri += 1           # Lisää laskuriin 1 joka kierroksella


#8 – Tiedostojen käsittely
#open() tiedoston käsittelyyn: "r" luku, "w" kirjoitus, "rb"/"wb" binaari.
#with sulkee tiedoston automaattisesti, mikä on turvallista.

#Koodi:

# Tekstitiedoston kirjoittaminen
with open("esimerkki.txt", "w") as f:  # Avaa tiedoston kirjoitustilassa
    f.write("Hei Python!\n")           # Kirjoittaa tekstin tiedostoon

# Tekstitiedoston lukeminen
with open("esimerkki.txt", "r") as f:  # Avaa tiedoston lukutilassa
    print(f.read())                     # Lukee ja tulostaa tiedoston sisällön

# Binaaritiedoston käsittely
data = b"Python bytes"                  # Binaarimuotoinen data
with open("esimerkki.bin","wb") as f:  # Avaa tiedoston binaarikirjoitusta varten
    f.write(data)                       # Kirjoittaa datan tiedostoon
with open("esimerkki.bin","rb") as f:  # Avaa tiedoston binäärilukua varten
    print(f.read())                     # Lukee ja tulostaa binaaridatan



#9 – Funktiot
#Funktio = koodilohko uudelleenkäyttöön.
#Parametrit = dataa funktiolle, return palauttaa arvon.
#Pääfunktio = ohjelman aloitus, alifunktio = mitä tahansa muuta funktiota.

#Koodi:

def tervehdi(nimi):                # Määrittelee funktion, joka ottaa parametrin nimi
    return f"Hei {nimi}!"          # Palauttaa tulostettavan merkkijonon

print(tervehdi("Anna"))            # Kutsuu funktiota ja tulostaa sen palauttaman arvon


#10 – Moduulit
#Moduuli = erillinen Python-tiedosto, jossa on funktioita ja koodia.
#Mahdollistaa koodin uudelleenkäytön.

#Koodi:

def tervehdi(nimi):
    """Palauttaa tervehdyksen annetulla nimellä."""
    return f"Heippa {nimi}!"

print(tervehdi("Mikko"))



#11 – Virheenkorjaus
#ry-except: varautuu virheisiin (esim. väärä syöte).
#else suoritetaan, jos virhettä ei tullut.
#finally suoritetaan aina riippumatta virheestä.

#Koodi:

try:
    luku = int(input("Anna luku: "))  # Yritetään muuntaa syöte numeroksi
except ValueError:                     # Suoritetaan, jos virhe tapahtuu
    print("Virhe! Et antanut lukua.")
else:                                  # Suoritetaan, jos virhettä ei tullut
    print("Annoit luvun:", luku)
finally:                               # Suoritetaan aina
    print("Ohjelma päättyi.")


#12 – Tietotyypit
#Lista = muokattava, järjestetty kokoelma.
#Sanakirja = avain-arvo-pari.
#Tuple = järjestetty, mutta muuttumaton.

#Koodi:

lista = [1,2,3]               # Lista, muokattava kokoelma
lista.append(4)                # Lisää alkion listan loppuun
print(lista)                   # Tulostaa listan

sanakirja = {"nimi":"Anna","ika":20}  # Sanakirja, avain-arvo-pari
sanakirja["kaupunki"]="Helsinki"      # Lisää uuden avain-arvo-parin
print(sanakirja)                      # Tulostaa sanakirjan

tuple_ = ("Matti",25)         # Tuple, järjestetty mutta muuttumaton
print(tuple_[0])               # Tulostaa ensimmäisen alkion


#13 – Oliot ja luokat
#Luokka = mallipohja, olio = instanssi.
#Jäsenmuuttujat tallentavat tiedon, jäsenfunktiot toiminnon.
#Periytyminen = uusi luokka saa ominaisuuksia vanhasta.
#Suojatut jäsenet (__nimi) hallitsevat pääsyä.

#Koodi:

class Koira:                    # Luokka, mallipohja
    def __init__(self, nimi):   # Alustaja (constructor)
        self.nimi = nimi        # Jäsenmuuttuja tallentaa koiran nimen

    def hauku(self):            # Jäsenfunktio
        print(f"{self.nimi} sanoo: Hau hau!")  # Funktio tulostaa koiran haukun
        

# Esimerkin käyttö
lemmikki = Koira("Rex")  # Luodaan olio
lemmikki.hauku()          # Kutsutaan hauku-funktiota
