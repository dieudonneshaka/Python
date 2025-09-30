# Muuttujat

# A  Mikä on muuttuja ja mitä sillä tehdään?

# Muuttuja on kuin laatikko, johon voidaan laittaa arvoja säilytettäväksi.
ikä = 20       # kokonaisluku
nimi = "Anna"  # merkkijono (teksti)

# Voimme käyttää näitä muuttujia ohjelmassa myöhemmin
print("Nimi:", nimi)  # tulostaa: Nimi: Anna
print("Ikä:", ikä)    # tulostaa: Ikä: 20


#Selitys:
#Muuttuja tallentaa tiedon, esimerkiksi numeron tai tekstin.
#Sen avulla voimme käsitellä tietoja ohjelmassa, tulostaa ne, laskea niillä, tai muuttaa niiden arvoa.




# B Muuttujien nimeämisen rajoitukset Pythonissa:
#Ei voi alkaa numerolla → 1luku ❌
#Ei erikoismerkkejä (@, #, $, %) → nimi$ ❌
#Ei Pythonin varattuja sanoja (if, for, True) → if ❌
#Hyvä käytäntö:
#Käytä kuvaavia nimiä → ikä_henkilö, nimi_henkilö
#Pienet kirjaimet, sanat erotetaan alaviivalla → oma_muuttuja


#C Pythonin perustietotyypit ovat yksinkertaisia tapoja tallentaa ja käsitellä
#  tietoa ohjelmassa. Ne tärkeimmät ovat

#int = kokonaisluku
#float = desimaaliluku
#str = teksti
#bool = tosi/epätosi


nimi_henkilö = "Anna"
ikä_henkilö = 25

print(nimi_henkilö)  # Anna
print(ikä_henkilö)   # 25



# Kokonaisluku (int)
ikä = 20
print("Ikä:", ikä)  # tulostaa: Ikä: 20

# Liukuluku (float)
hinta = 19.99
print("Hinta:", hinta)  # tulostaa: Hinta: 19.99

# Merkkijono (str)
nimi = "Anna"
print("Nimi:", nimi)  # tulostaa: Nimi: Anna

# Totuusarvo (bool)
on_opiskelija = True
print("On opiskelija:", on_opiskelija)  # tulostaa: On opiskelija: True


# D Miten muuttujia käytetään? (muuttujan luominen, arvon sijoittaminen, arvon lukeminen)
#Muuttujan luominen: kirjoitetaan nimi ja annetaan sille arvo =-merkillä.
#Arvon lukeminen: muuttujan arvo voidaan tulostaa tai käyttää laskuissa.
#Arvon muuttaminen: samaan muuttujaan voidaan sijoittaa uusi arvo milloin tahansa.

#Tässä selitys ja koodiesimerkki muuttujien käytöstä

# 1. Muuttujan luominen ja arvon sijoittaminen
ikä = 25          # kokonaisluku
nimi = "Mikko"    # merkkijono (teksti)
pisteet = 88.5    # liukuluku

# 2. Arvon lukeminen / käyttäminen
print("Nimi:", nimi)       # tulostaa: Nimi: Mikko
print("Ikä:", ikä)         # tulostaa: Ikä: 25
print("Pisteet:", pisteet) # tulostaa: Pisteet: 88.5

# 3. Muuttujan arvon muuttaminen
ikä = 26
print("Uusi ikä:", ikä)    # tulostaa: Uusi ikä: 26



# 3.Syötteet ja tulostaminen
#Pythonissa käyttäjän syöte näppäimistöltä otetaan vastaan input()-funktiolla.
#Tämä funktio pysäyttää ohjelman ja odottaa,
#että käyttäjä kirjoittaa jotain ja painaa Enteriä. Syöte tallennetaan muuttujaan.

# Pyydetään käyttäjää kirjoittamaan jotain
nimi = input("Anna nimesi: ")  # Teksti kysymys näkyy näytöllä

# Tulostetaan käyttäjän syöte
print("Hei", nimi)

#Selitys:
#input() palauttaa aina merkkijonon (string).
#Syöte voidaan tallentaa muuttujaan, jotta sitä voidaan käyttää myöhemmin ohjelmassa.
#Esimerkiksi jos käyttäjä kirjoittaa Anna, muuttuja nimi sisältää tekstin 
# "Anna" ja tulostus näyttää:



# B Syöte on oletuksena tekstiä. Miten se muunnetaan esim. kokonaisluvuksi?

#input()-funktio palauttaa aina tekstin (merkkijonon), vaikka käyttäjä kirjoittaisi numeron.
#  Jos haluat käsitellä syötteen esimerkiksi kokonaislukuna, sinun pitää muuntaa 
# se sopivaan tietotyyppiin, kuten int()-funktiolla.

# Esimerkki 
# Pyydetään käyttäjää kirjoittamaan ikänsä

#ikä_str = input("Anna ikäsi: ")  # palauttaa merkkijonon
#ikä = int(ikä_str)                # muutetaan merkkijono kokonaisluvuksi

# Voidaan nyt tehdä laskuja iällä
#vuosi_syntymästä = 2025 - ikä
#print("Olet syntynyt vuonna", vuosi_syntymästä)


# Pyydetään käyttäjää kirjoittamaan ikänsä
ikä_str = input("Anna ikäsi: ")

try:
    # Yritetään muuntaa syöte kokonaisluvuksi
    ikä = int(ikä_str)
    print("Olet syntynyt vuonna", 2025 - ikä)
except ValueError:
    # Jos syöte ei ole numero, tulostetaan virheilmoitus
    print("Virhe: Anna kokonaisluku!")


#Selitys:
#int(ikä_str) yrittää muuntaa merkkijonon kokonaisluvuksi.
#Jos syöte ei ole numero, Python nostaa ValueError-virheen.
#try-except estää ohjelman kaatumisen ja antaa käyttäjälle selkeän virheilmoituksen.
#Tämä tapa on turvallinen tapa käsitellä käyttäjän syötteitä.


#C Mitä erilaisia tapoja tulostaa teksti näytölle on? Miten muuttujat yhdistetään tekstiin? 
# (plus-merkki, pilkku, tarkempi muotoilu)


nimi = "Anna"
ikä = 20

# 1. Yksinkertainen tulostus
print("Hei maailma!")  # tulostaa: Hei maailma!

# 2. Muuttujien yhdistäminen plus-merkillä (merkkijonot pitää muuttaa stringiksi)
print("Nimi: " + nimi + ", Ikä: " + str(ikä))
# tulostaa: Nimi: Anna, Ikä: 20

# 3. Muuttujien yhdistäminen pilkulla
print("Nimi:", nimi, "Ikä:", ikä)
# tulostaa: Nimi: Anna Ikä: 20
# Huomaa: pilkun käyttö lisää automaattisesti välilyönnin

# 4. F-string eli tarkempi muotoilu (Python 3.6+)
print(f"Nimi: {nimi}, Ikä: {ikä}")
# tulostaa: Nimi: Anna, Ikä: 20

# 5. format-metodi
print("Nimi: {}, Ikä: {}".format(nimi, ikä))
# tulostaa: Nimi: Anna, Ikä: 20

#Selitys:
#+ yhdistää merkkijonot, mutta numerot täytyy muuttaa stringiksi.
#Pilkku , tulostaa automaattisesti välilyönnit ja muuntaa numerot merkkijonoksi.
#F-string ja format() antavat joustavan ja selkeän tavan sijoittaa muuttujia tekstiin.





#D.Miten tekstiin saa esim. lainausmerkin ilman, 
# että Python luulee merkkijonon loppuvan tähän?

# 1. Käyttämällä erilaista lainausmerkkiä
teksti1 = 'Hän sanoi: "Hei!"'  # Ulompi lainausmerkki on yksinkertainen, sisempi kaksoislainaus
teksti2 = "Hän sanoi: 'Hei!'"  # Ulompi lainausmerkki on kaksois, sisempi yksinkertainen

print(teksti1)  # tulostaa: Hän sanoi: "Hei!"
print(teksti2)  # tulostaa: Hän sanoi: 'Hei!'

# 2. Käyttämällä escape-merkkiä (\)
teksti3 = "Hän sanoi: \"Hei!\""
print(teksti3)  # tulostaa: Hän sanoi: "Hei!"



#Selitys:
#Pythonissa voit käyttää ' tai " merkkijonojen ympärillä. 
#Sisempi lainausmerkki ei riko merkkijonoa, jos se eroaa ulommaisesta.
#Jos haluat käyttää samaa merkkiä sisällä kuin ulkona, käytä escape-merkkiä \, 
#joka kertoo Pythonille, että merkki on osa tekstiä eikä merkkijonon loppu.



#4. Merkkijonojen käsittely

#A.Miten selvitetään merkkijonon pituus?
#merkkijonon pituus selvitetään len()-funktiolla.
#Tässä esimerkki:

teksti = "Hei maailma"
pituus = len(teksti)  # len() laskee merkkien määrän

print("Merkkijonon pituus on:", pituus)  # tulostaa: Merkkijonon pituus on: 11

#Selitys:
#len() ottaa argumentiksi merkkijonon (tai muun tietotyypin kuten listan) 
# ja palauttaa sen alkioiden lukumäärän.
#Tämä on hyödyllistä esimerkiksi tarkistettaessa syötteen pituutta
#  tai toistorakenteiden yhteydessä.


#B.Miten Pythonissa otetaan merkkijonosta yksittäinen merkki tai osajono (leikkaus)?
# merkkijono voidaan ottaa yksittäinen merkki tai osajono indeksoinnin ja 
# viipaloinnin (slicing) avulla.


teksti = "Python"

# Yksittäinen merkki
print(teksti[0])   # tulostaa 'P'
print(teksti[-1])  # tulostaa 'n'

# Osajono (leikkaus)
print(teksti[0:4])  # tulostaa 'Pyth'
print(teksti[2:5])  # tulostaa 'tho'
print(teksti[2:])   # tulostaa 'thon'
print(teksti[:4])   # tulostaa 'Pyth'

#Selitys:
#teksti[0] → ensimmäinen merkki
#teksti[-1] → viimeinen merkki
#teksti[aloitus:lopetus] → merkkijonon osa alkaen indeksistä aloitus loppuen lopetus-1
#ilman aloitusta tai loppua tarkoittaa alusta loppuun tai aloituksesta loppuun.


#C. Miten merkkijonoa voidaan toistaa monta kertaa?
#merkkijonoa voidaan toistaa kertomalla se luvulla.

teksti = "Hei! "

# Toistetaan merkkijono 3 kertaa
tulos = teksti * 3
print(tulos)   # tulostaa: Hei! Hei! Hei! 

#Selitys:
#*-operaattoria käytetään kertomaan merkkijono luvulla.
#Jos kerrot merkkijonon esimerkiksi 3:lla, saat sen peräkkäin kolme kertaa.
#Tätä käytetään esim. tulostamaan viesti useasti ilman, että kirjoitat sitä moneen kertaan.


#D.Mitä eri valmisfunktioita merkkijonojen käsittelyyn käytettiin kurssilla?
#Esittele muutama niistä.
#otetaan muutama yleinen merkkijonojen käsittelyfunktio ja 
# laitetaan ne pieninä esimerkkikoodeina

# lower(): muuttaa pieniksi
teksti = "HELLO"
print(teksti.lower())   # tulos: hello

# upper(): muuttaa isoiksi
teksti = "hello"
print(teksti.upper())   # tulos: HELLO

# strip(): poistaa välilyönnit alusta ja lopusta
teksti = "   Python   "
print(teksti.strip())   # tulos: Python

# replace(): korvaa tekstiä
teksti = "kissa ja koira"
print(teksti.replace("kissa", "jänis"))  # tulos: jänis ja koira

# split(): jakaa merkkijonon listaksi
teksti = "omena banaani appelsiini"
print(teksti.split())   # tulos: ['omena', 'banaani', 'appelsiini']

# Näissä esimerkeissä näkyy, miten Pythonin valmisfunktiot toimivat käytännössä: 
# ne helpottavat tekstin käsittelyä ilman, että tarvitsee itse kirjoittaa pitkiä ohjelmia.


#5 Valintarakenne (if-lause)

#A.Miten if-lause toimii? Entä if-else? If-elif-else?
# f-lause tarkistaa, onko ehto tosi. Jos ehto on tosi, sen sisällä oleva koodi suoritetaan.

ikä = 20

if ikä >= 18:         # Tarkistetaan ehto
    print("Olet täysi-ikäinen")   # Suoritetaan vain jos ehto on tosi

#If-else
#Jos ehto ei ole tosi, suoritetaan else-lohko.

ikä = 15

if ikä >= 18:
    print("Olet täysi-ikäinen")
else:
    print("Olet alaikäinen")   # Tänne tullaan jos ehto on epätosi

#If-elif-else
#Jos ehtoja on useampi, käytetään elif (else if). Käydään ehdot järjestyksessä läpi.

ikä = 70

if ikä < 18:
    print("Olet alaikäinen")
elif ikä < 65:
    print("Olet aikuinen")
else:
    print("Olet eläkeläinen")


#Selitys:
#if = tarkistaa ehdon
#else = suoritetaan jos mikään edellinen ehto ei ollut tosi
#elif = lisäehto, jos halutaan tarkistaa useampia vaihtoehtoja


#B.Miten sisennyksiä pitää käyttää koodilohkojen merkitsemiseen?

#sisennys (välilyönnit tai tabit) kertoo, mikä koodi kuuluu mihinkin lohkoon. 
# Toisin kuin monissa muissa kielissä, Pythonissa ei käytetä aaltosulkuja {}
#  vaan sisennys on pakollinen.

ikä = 15

if ikä >= 18:
    print("Olet täysi-ikäinen")   # tämä rivi sisennetty -> kuuluu if-lohkoon
    print("Voit ajaa autoa")      # tämäkin kuuluu if-lohkoon
else:
    print("Olet alaikäinen")      # tämä kuuluu else-lohkoon


#Säännöt:
#Käytä aina samaa sisennystapaa (yleensä 4 välilyöntiä).

#Kaikki rivit, jotka kuuluvat samaan lohkoon, pitää sisentää yhtä paljon.
#Kun lohko päättyy, palataan takaisin vasempaan reunaan.


#C.Mitä erilaisia vertailuja voidaan käyttää valintarakenteen ehtona 
# (se if-sanan ja kaksoispisteen välissä oleva osa)?

#Pythonissa vertailuja käytetään ehtona if-lauseessa. 
# Niillä verrataan arvoja toisiinsa, ja tulos on aina tosi (True) tai epätosi (False).

ikä = 16

# onko ikä 18?
if ikä == 18:
    print("Täytit juuri 18!")

# onko ikä alle 18?
if ikä < 18:
    print("Olet alaikäinen")

# onko ikä vähintään 15?
if ikä >= 15:
    print("Olet vähintään 15-vuotias")


#Lisähuomio:
#Ehtoja voi myös yhdistellä:
#and = molempien ehtojen pitää olla totta
#or = riittää, että yksi ehto on totta
#not = kääntää ehdon (True → False, False → True)
#Esim:

ikä = 20
opiskelija = True

if ikä >= 18 and opiskelija:
    print("Aikuinen opiskelija")




#D Mitä tarkoittaa käytännössä, että ehdon pitää olla tosi tai epätosi?
#  (esim. toimiiko if 2: ?)

#if-lauseen ehto pitää aina arvioitua joko tosi (True) tai epätosi (False).
#Jos ehto on tosi, koodilohko suoritetaan.
#Jos ehto on epätosi, koodilohko ohitetaan.

#Mitä tarkoittaa “tosi” tai “epätosi” käytännössä?
#seuraavat ovat epätosia (False) ehdossa:

#False

#None

#Luku 0 tai 0.0

#Tyhjä merkkijono ""

#Tyhjä lista [], tuple (), sanakirja {}, joukko set()

#Kaikki muu on tosi (True), esimerkiksi:


# Luku 2 on "tosi"
if 2:
    print("Tämä tulostuu, koska 2 on tosi")

    # Luku 0 on "epätosi"
if 0:
    print("Tätä ei tulosteta, koska 0 on epätosi")

# Tyhjä lista on epätosi
lista = []
if lista:
    print("Tätä ei tulosteta")

# Ei-tyhjä lista on tosi
lista = [1, 2, 3]
if lista:
    print("Tämä tulostuu, koska lista ei ole tyhjä")


#E. Miten ehtoja voidaan yhdistellä?
#Ja Molempien ehtojen pitää olla tosia
#TAI Ainakin yhden ehdon pitää olla tosi
#EI Kääntää ehdon totuusarvon

kä = 20
on_opiskelija = True

# Käytetään "and" -> molempien ehtojen pitää olla tosia
if ikä >= 18 and on_opiskelija:
    print("Täysi-ikäinen opiskelija")

    # Käytetään "or" -> vähintään yhden ehdon pitää olla tosi
if ikä < 18 or on_opiskelija:
    print("Tai alaikäinen, tai opiskelija")

    # Käytetään "not" -> kääntää ehdon
if not on_opiskelija:
    print("Ei ole opiskelija")


#6. Toistorakenteet (while ja for)

# A. Mitä tarkoitetaan toistorakenteella?
#Toistorakenne on osa ohjelmointia, jonka avulla voimme suorittaa samaa koodilohkoa 
# useita kertoja ilman, että kirjoittaisimme sen uudestaan joka kerta.
#Toisin sanoen, se "silmukoi" koodin toistuvasti.

#Tässä on Esimerkki while-silmukasta

laskuri = 0

while laskuri < 5:   # Suorita niin kauan kuin laskuri < 5
    print("Laskuri on:", laskuri)
    laskuri += 1     # Lisää laskuriin 1


#Selitys:
#Aluksi laskuri = 0
#Silmukka suoritetaan niin kauan kuin laskuri < 5
#Jokaisen kierroksen jälkeen laskuri kasvaa +1
#Kun laskuri saavuttaa 5, silmukka loppuu

for i in range(5):   # Toista 5 kertaa (0,1,2,3,4)
    print("i on:", i)


#B. Miten while-toistorakenne toimii?

#Mitä on  while-toistorakenne?
#while-silmukka suorittaa koodilohkon toistuvasti niin kauan kuin annettu ehto on tosi (True).
#Kun ehto muuttuu epätodeksi (False), silmukka lopettaa suorituksen.


laskuri = 0  # Aloitusarvo

while laskuri < 5:  # Silmukka jatkuu, kun laskuri on pienempi kuin 5
    print("Laskuri on:", laskuri)
    laskuri += 1  # Lisätään laskuriin 1 joka kierroksella


#Selitys:
#Aluksi laskuri = 0
#Ehto laskuri < 5 tarkistetaan
#Jos ehto on tosi, suoritetaan koodilohko (print ja laskurin kasvatus)
#Ehtoa tarkastellaan uudelleen seuraavalla kierroksella
#Kun laskuri saavuttaa 5, ehto ei enää pidä paikkaansa → silmukka loppuu


#C.  Mikä on ikuinen silmukka ja miten siltä vältytään?

#Ikuinen silmukka (engl. infinite loop) on silmukka, joka jatkuu loputtomiin, 
# koska sen ehto pysyy aina totena (True).
#Tässä on esimerkkki

#while True:
    #print("Tämä tulostuu ikuisesti!")


#Tässä True on aina tosi → silmukka ei koskaan lopu itsestään
#Tämä voi kaataa ohjelman, jos sitä ei pysäytetä manuaalisesti (esim. Ctrl+C)


#Miten siltä vältytään?
#Muuta ehtoa silmukan sisällä, jotta se lopulta tulee epätodeksi (False):

laskuri = 0
while laskuri < 5:
    print("Laskuri:", laskuri)
    laskuri += 1  # Lopulta laskuri = 5 → silmukka loppuu

#D. Miten for-toistorakenne toimii? Koska ”for on vain tiivistetty while”, 
# voit myös vertailla näitä kahta.

#For-silmukka käy läpi jonon, listan, merkkijonon tai jonkin muun iteratiivisen 
# rakenteen yksi kerrallaan.

# Käydään läpi lista
hevoset = ["Ruuvi", "Tarmo", "Pilvi"]
for hevonen in hevoset:
    print("Hevosen nimi:", hevonen)

#hevonen on muuttuja, joka saa yksi kerrallaan listan arvot
#Silmukka päättyy automaattisesti, kun lista loppuu


#For silmukka numerojen kanssa ja range()

# Tulostetaan luvut 0–4
for i in range(5):
    print(i)


#Vertailu while-silmukkaan
#While-silmukka tarvitsee ehdon, ja silmukan muuttujasta huolehtiminen on sinun vastuullasi:

i = 0
while i < 5:
    print(i)
    i += 1  # Muista kasvattaa i, muuten silmukka jatkuu loputtomiin!


#Ero:
#For: yksinkertaisempi, koska käy automaattisesti läpi arvot
#While: joustavampi, perustuu ehtoihin, mutta sinun täytyy itse huolehtia muuttujan
#  kasvattamisesta

#Yhteenveto
#For = kiertää automaattisesti jonon/alueen läpi
#While = jatkuu niin kauan kuin ehto on tosi
#Käytännössä for on “tiivistetty while”, kun halutaan käydä läpi tietty määrä kertoja


#E.Miten range-funktiota voi käyttää for-toistorakenteessa?
#range() luo numeroiden sarjan, jota for-silmukka voi käydä läpi.

# Tulostetaan luvut 0–4
for i in range(5):
    print(i)

#For-silmukka käy ne läpi automaattisesti



#Voit määrittää, kuinka paljon luku kasvaa jokaisella kierroksella:

for i in range(1, 10, 2):  # kasvu 2
    print(i)


# F. Mitä break, continue ja pass tekevät?
#break – Lopettaa silmukan heti
#break keskeyttää silmukan kokonaan ja hyppää sen jälkeen silmukan ulkopuolelle.

for i in range(1, 6):
    if i == 3:
        break  # Lopetetaan silmukka, kun i = 3
    print(i)

#Huomaa: Silmukka ei jatka 3:n jälkeen.


#continue – Hyppää seuraavaan kierrokseen
#continue ohittaa silmukan tämän kierroksen loppuosan ja siirtyy seuraavaan iteraatioon.

for i in range(1, 6):
    if i == 3:
        continue  # Ohitetaan i = 3
    print(i)

#Huomaa: 3 ohitettiin, mutta silmukka jatkoi 4:stä eteenpäin.


#pass – Tee ei mitään
#pass on “tyhjä lauseke”. Käytetään, kun Python vaatii koodirivin, 
# mutta et halua tehdä mitään vielä.

for i in range(1, 6):
    if i == 3:
        pass  # Ei tehdä mitään
    print(i)

#Huomaa: pass ei vaikuta silmukan kulkuun, se vain tyhjentää paikan koodissa.

#Yhteenveto
#Käsky	Mitä tekee
#break	Keskeyttää silmukan kokonaan
#continue	Ohittaa kierroksen loppuosan ja jatkaa
#pass	Ei tee mitään – paikanvaraus koodille

#G. Toisin kuin useimmat muut ohjelmointikielet, Python mahdollistaa 
# else-osan käyttämisen myös toistorakenteissa. Mihin tätä käytetään

#else silmukan yhteydessä
#else suoritetaan vain, jos silmukka päättyy normaalisti (eli ei keskeytynyt break-komennolla).
#Toisin sanoen, jos silmukka loppuu loppuun asti ilman keskeytystä, else-lohko ajetaan.


for i in range(1, 6):
    print(i)
else:
    print("Silmukka päättyi normaalisti")


#Huomaa: else-lohko ei suoritettu, koska silmukka keskeytettiin break-komennolla.



lista = [2, 4, 6, 8]
for luku in lista:
    if luku == 5:
        print("Luku löytyi!")
        break
else:
    print("Lukua ei löytynyt")  # Suoritetaan, koska 5 ei ollut listassa


#Miksi tämä on hyödyllistä?
#Esimerkiksi voidaan etsiä tietty arvo listasta:
#Jos arvo löytyy, käytetään break.
#Jos arvoa ei löydy, else kertoo, että etsintä epäonnistui.

