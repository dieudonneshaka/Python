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


# Merkkijono (str)
nimi = "Anna"
print("Nimi:", nimi)  # tulostaa: Nimi: Anna


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



#7.Tiedostojen käsittely

#Miten tekstitiedostosta luetaan?

# Luetaan tekstitiedosto "teksti.txt" ja tulostetaan sen sisältö


# Luetaan tekstitiedosto "teksti.txt" ja tulostetaan sen sisältö

with open("teksti.txt", "r", encoding="utf-8") as tiedosto:
    sisalto = tiedosto.read()
    print(sisalto)


#Selitys:
#with open(...) avaa tiedoston turvallisesti ja sulkee sen automaattisesti.
#"r" tarkoittaa, että tiedosto avataan lukemista varten.
#read() lukee koko tiedoston sisällön.
#print() näyttää tiedoston sisällön näytöllä.


#B. Miten tekstitiedostoon kirjoitetaan?

with open("teksti.txt", "w", encoding="utf-8") as tiedosto:
    tiedosto.write("Hei maailma!\n")
    tiedosto.write("Tämä on toinen rivi.")


# Kirjoitetaan teksti tiedostoon "teksti.txt"


#C. Miten bittimuotoista dataa luetaan ja kirjoitetaan? (ks.
#  osio ”12 Tietotyypit ja leikkaukset”)


#Tässä selitys ja yksinkertainen esimerkki Pythonissa bittimuotoisen datan lukemisesta ja
#  kirjoittamisesta. Bittimuotoinen data tarkoittaa, että käsittelemme tiedostoa binäärinä
#  (eli ei pelkkää tekstiä, vaan myös kuvat, videot, tms.).

# Kirjoitetaan bittimuotoista dataa tiedostoon
data = b"Hei Python!"  # 'b' tekee datasta bytes-tyyppisen
with open("bitti_tiedosto.bin", "wb") as tiedosto:  # 'wb' = write binary
    tiedosto.write(data)

# Luetaan bittimuotoista dataa tiedostosta
with open("bitti_tiedosto.bin", "rb") as tiedosto:  # 'rb' = read binary
    luettu_data = tiedosto.read()

print(luettu_data)  # tulostaa: b'Hei Python!'


#Selitys:
#b"..." tarkoittaa bittijonoa (bytes).
#'wb' avaa tiedoston kirjoitusta varten binäärimuodossa.
#'rb' avaa tiedoston lukemista varten binäärimuodossa.
#Tulostus näyttää b'...', koska kyseessä on bytes-tyyppi.


#8. Funktiot

#A. Kurssilla käytetään termiä ”alifunktio”, mutta tämä on käytännössä sama asia kuin funktio.
#  ”Pääfunktio” on se koodi, joka ajetaan ohjelman käynnistyessä, ja ”alifunktio” mikä tahansa
#  funktio, jota se kutsuu.

#Selitetään tämä helposti ja esimerkin avulla.
#Pythonissa funktio on koodilohko, jonka voi kutsua useita kertoja ohjelman aikana.
#Pääfunktio: on  osa koodia, joka ajetaan, kun ohjelma alkaa.
#Alifunktio: funktio, jota pääfunktio (tai joku muu funktio) kutsuu tekemään tietyn tehtävän.

# Alifunktio
def tervehdys(nimi):
    print("Hei, " + nimi + "!")

# Pääfunktio
def main():
    tervehdys("Python")   # kutsutaan alifunktiota

# Ohjelman käynnistys
if __name__ == "__main__":
    main()

#Selitys:
#tervehdys on alifunktio: se tekee yhden tehtävän (tervehtii).
#main on pääfunktio: se hallitsee ohjelman kulkua ja kutsuu alifunktiota.
#if __name__ == "__main__": varmistaa, että main() ajetaan vain, kun tiedosto suoritetaan suoraan.



#B.  Miksi funktioita kannattaa käyttää? Mihin niitä käytetään?

#Funktio on koodin osa, joka tekee tietyn tehtävän.
# ja Miksi käyttää sitä se  helpottaa koodin uudelleenkäyttöä, 
# pitää ohjelman siistinä ja helpottaa virheiden korjaamista.


# Funktio, joka laskee neliön
def neliö(x):
    return x * x

# Käytetään funktiota
luku = 5
tulos = neliö(luku)
print("Luvun", luku, "neliö on", tulos)

#C . Miten funktio määritellään? Miten sitä käytetään (kutsutaan)?

#Funktio määritellään def-avainsanalla, ja sitä käytetään kutsumalla sen 
# nimeä ja mahdollisia parametreja.

def tervehdi(nimi):
    print("Hei, " + nimi + "!")

# Funktion kutsuminen
tervehdi("Anna")  # Tulostaa: Hei, Anna!
tervehdi("Matti") # Tulostaa: Hei, Matti!


#Selitys:
#def kertoo Pythonille, että nyt määritellään funktio.
#tervehdi on funktion nimi.
#(nimi) on parametri, jonka avulla voimme antaa funktiolle tietoa.
#print suoritetaan aina, kun funktio kutsutaan.
# Funktion määrittely

# D. Miten funktiolle annetaan dataa (parametrit)? 
# Mikä on parametrin oletusarvo ja miten sitä käytetään?

#Funktiolle voidaan antaa dataa parametreina sulkujen sisällä. 
#Parametrin oletusarvo tarkoittaa, että jos kutsuessa ei anneta arvoa, käytetään oletusarvoa.

# Parametri ilman oletusarvoa
def kerro_nimi(nimi):
    print("Hei, " + nimi + "!")

kerro_nimi("Anna")  # Tulostaa: Hei, Anna!

# Parametri oletusarvolla
def tervehdi(nimi="Maailma"):
    print("Hei, " + nimi + "!")

tervehdi()        # Tulostaa: Hei, Maailma!
tervehdi("Matti") # Tulostaa: Hei, Matti!

#E. Miten funktio palauttaa dataa kutsujalle (paluuarvo, return)? 
# Mihin muuhun return-käskyä voidaan käyttää kuin arvon palauttamiseen?

#funktio voi palauttaa arvon kutsujalle return-avainsanalla. 
# Paluuarvo voidaan tallentaa muuttujaan tai käyttää suoraan laskutoimituksissa. 
# Lisäksi return voi keskeyttää funktion suorituksen heti, vaikka se ei palauttaisikaan arvoa.

# Paluuarvon käyttö
def summa(a, b):
    return a + b

print(summa(3, 5))  # Tulostaa: 8

# Return keskeyttää funktion
def tarkista(luku):
    if luku < 0: return
    print("Luku on positiivinen")

tarkista(-2)  # Ei tulosta mitään
tarkista(5)   # Tulostaa: Luku on positiivinen


#F. (vapaaehtoinen, haastava) Miten nimiavaruudet ja muuttujien näkyvyys toimivat? 
# (Tai ”minkä ihmeen muuttujan arvon tämä funktio oikein tulostaa?”)

#muuttujien näkyvyys eli scope riippuu siitä, missä muuttuja on määritelty.
# Pääsääntöisesti muuttujat voivat olla globaaleja tai paikallisia.


x = 10  # globaali muuttuja

def funktio():
    y = 5  # paikallinen muuttuja
    print("Paikallinen y:", y)
    print("Globaali x:", x)

funktio()

# print(y)  # Tämä aiheuttaa virheen, koska y on paikallinen


#9. Moduulit

#A.  Mitä ovat moduulit? Miksi ne ovat olemassa?

#Moduuli on Python-tiedosto (.py), jossa on valmiiksi tehtyjä funktioita ja muuttujia.
#Moduuleja voidaan tuoda omaan ohjelmaan ja käyttää niiden sisältöä.

# ja syy miksi ne ovat olemassa:

#Ne säästävät aikaa, koska kaikkea ei tarvitse kirjoittaa itse.
#Ne tekevät koodista selkeämpää ja jaettavampaa.
#Pythonissa on paljon valmiita moduuleja (esim. math, random, os), ja voit myös tehdä omia.

import math   # tuodaan math-moduuli

luku = 16
print(math.sqrt(luku))  # laskee neliöjuuren → tulostaa 4.0


#B. Miten moduuleja käytetään?

#Moduuleja käytetään  import-komennolla.
#Ne sisältävät valmiita funktioita, muuttujia ja luokkia, joita voi käyttää ohjelmassa.

# oma_moduuli.py

# =========================================
# Tämä on "oma_moduuli.py" moduuli
# =========================================
def tervehdys(nimi):
    return f"Heippa, {nimi}!"

def luku_kaksinkertainen(x):
    return x * 2

# =========================================
# Tämä on pääohjelma, sama tiedosto esimerkkinä
# =========================================

# Tuodaan moduulin funktiot käyttöön (simuloidaan import)
# Tässä samassa tiedostossa käytämme suoraan funktioita

# Käytetään funktiota tervehdys
print(tervehdys("Anna"))      # Tulostaa: Heippa, Anna!

# Käytetään funktiota luku_kaksinkertainen
print(luku_kaksinkertainen(5)) # Tulostaa: 10


#C. Miten luot oman moduulin?
#Moduuli on tiedosto, jossa on funktioita.
#import oma_moduuli tuo moduulin käyttöön.
#oma_moduuli.funktio() kutsuu moduulin funktiota.
#Näin voit käyttää samoja funktioita monessa ohjelmassa ilman, 
# että kirjoitat koodia uudelleen.

# --- määritellään moduulin funktiot samassa tiedostossa ---
def tervehdys(nimi):
    return f"Heippa, {nimi}!"

def summa(a, b):
    return a + b

# --- käytetään funktioita ---
print(tervehdys("Anna"))  # Tulostaa: Heippa, Anna!
print(summa(5, 7))        # Tulostaa: 12


#10.Virheenkorjaus

#A. Ohjelman ei ole tarkoitus kaatua, vaikka esimerkiksi käyttäjä antaisi kirjaimen,
#  kun pyydetään numeroa. Miten try-except -rakenteella voi varautua virheisiin?

#Tässä lyhyt ja selkeä selitys esimerkkikoodin kanssa:

# Pyydetään käyttäjältä numeroa
try:
    luku = int(input("Anna kokonaisluku: "))
    print("Annoit luvun:", luku)
except ValueError:
    print("Virhe! Et antanut kokonaislukua.")

#try:-lohkossa laitetaan koodi, joka saattaa aiheuttaa virheen.
#except-lohko käsittelee virheen, jotta ohjelma ei kaadu.
#Tässä esimerkissä, jos käyttäjä kirjoittaa kirjaimen numeron sijaan,
#  ohjelma tulostaa virheilmoituksen eikä kaadu.

#B. Mitä ”else” ja ”finally” ovat try-catch -rakenteessa?

#try: sisältää koodin, joka voi aiheuttaa vrheen.
#except: käsittelee virheen, jos sitä tapahtuu.
#else: suoritetaan vain, jos try onnistui ilman virhettä.
#finally: suoritetaan aina, riippumatta siitä tapahtuiko virhe vai ei.
#Käytännössä else sopii "onnistumisen käsittelyyn" ja finally
#  "siivoukseen" tai koodiin, joka pitää suorittaa aina.

try:
    luku = int(input("Anna luku: "))
except ValueError:
    print("Virhe! Et antanut lukua.")
else:
    print("Annoit luvun oikein:", luku)
finally:
    print("Tämä suoritetaan aina, oli virhe tai ei.")

#C. Miten ohjelmassa voidaan varautua useisiin erilaisiin virheisiin eri tavoilla? 
# Esimerkiksi saattaisit haluta antaa eri virheilmoituksen, 
# jos käyttäjä yrittää antaa lukujen sijaan kirjaimia ja jos hän yrittää jakaa nollalla. 
# (Tässä voi käyttää kurssin esimerkkiä. 
# Oikeita käytännön esimerkkejä useammasta virhetyypistä samaan aikaan ei ole kovin montaa.)

# vähän pitkä kysymys mutta Mä yrittä  selitttä lyhesti

try:
    x = int(input("Anna jakaja: "))
    y = 10 / x
except ValueError:
    print("Virhe! Et antanut lukua.")
except ZeroDivisionError:
    print("Virhe! Jakaminen nollalla ei ole sallittua.")
else:
    print("Laskutoimitus onnistui, tulos:", y)


#ValueError käsittelee tilanteen, jossa käyttäjä ei anna lukua.
#ZeroDivisionError käsittelee tilanteen, jossa yritetään jakaa nollalla.
#else suoritetaan vain, jos virhettä ei tapahtunut.


#D.Kaikkeen ei tarvitse käyttää try-catch -rakennetta.  Esimerkiksi IndexError tapahtuu, 
# kun ohjelma viittaa listan ulkopuolelle eli listan kohtaan, jota ei ole olemassa. 
# Miten tämän voisi estää tavallisella ehtolauseella? (vihje: 
# listan kohdat numeroidaan 0…(listan pituus – 1))


lista = [10, 20, 30]
indeksi = 3  # haluttu kohta

# Tarkistetaan, että indeksi on listan pituuden sisällä
if 0 <= indeksi < len(lista):
    print(lista[indeksi])
else:
    print("Virhe: indeksi ei ole listan sisällä!")



#len(lista) kertoo listan pituuden.

#0 <= indeksi < len(lista) varmistaa, että indeksi ei ole liian pieni
#  (negatiivinen) eikä liian suuri.
#Näin ohjelma ei kaadu, vaikka käyttäjä yrittäisi käyttää olematonta kohtaa.


#11. Tietotyypit ja leikkaukset

#A. Pythonin yleisimpiä tietotyyppejä ovat lista, sanakirja, tuple ja joukko. 
# Esittele kolme näistä tietotyypeistä. Yhden voi siis jättää pois. Kerro, 
# miten tietotyyppi toimii ja miten sitä käytetään (alkion hakeminen, lisääminen, 
# muokkaaminen jos mahdollista).



# Lista (list) – muokattava, järjestetty kokoelma
lista = [10, 20, 30]
print(lista[1])        # hakee toisen alkion -> 20
lista.append(40)       # lisää alkion loppuun
lista[0] = 5           # muuttaa ensimmäisen alkion
print(lista)           # [5, 20, 30, 40]

# Sanakirja (dict) – avain-arvo -pari, muokattava
henkilo = {"nimi": "Anna", "ikä": 20}
print(henkilo["nimi"]) # hakee arvon avaimella -> Anna
henkilo["ikä"] = 21    # muuttaa arvon
henkilo["kaupunki"] = "Helsinki"  # lisää uuden avain-arvo -parin
print(henkilo)         # {'nimi': 'Anna', 'ikä': 21, 'kaupunki': 'Helsinki'}

# Tuple (tuple) – järjestetty mutta muuttumaton
opiskelija = ("Matti", 25, "Tietojenkäsittely")
print(opiskelija[0])   # hakee ensimmäisen alkion -> Matti
# opiskelija[1] = 26   # tämä aiheuttaisi virheen, tuple ei muokattavissa



#Lista: muokattava, järjestetty, voi lisätä, poistaa, muuttaa alkioita.
#Sanakirja: tietoja avain-arvo -pareina, muokattava, ei indeksiä vaan avain.
#Tuple: järjestetty mutta ei muokattavissa, turvallinen tallentaa muuttumattomia tietoja.

#12.Oliot

#A.Jos meni liian vaikeaksi liian nopeasti, voit jättää koodiesimerkit pois ja
#  kertoa vain lyhyesti teoriatasolla. Oliot ovat vaikeita – erityisesti 
# jos et ole koodannut aikaisemmin.


#Olio on kuin todellisen maailman esine ohjelmassa. Se sisältää ominaisuuksia (muuttujia) ja
#  toimintoja (metodeja/funktioita).
#Luokka (class) on kuin olion malli tai suunnitelma. Se kertoo, mitä ominaisuuksia ja
#  toimintoja olioilla on.

#Olio (object) on luokan toteutus, konkreettinen instanssi. Esimerkiksi Auto-luokka 
# määrittelee ominaisuuksia kuten väri ja merkki, ja autoni on yksi Auto-olio, 
# jolla on omat arvonsa.
#Periytyminen tarkoittaa, että uusi luokka voi saada ominaisuuksia ja toimintoja 
# toiselta luokalta, mutta voi myös muokata niitä.
#Jäsenmuuttujat ja jäsenfunktiot ovat luokan sisällä määriteltyjä muuttujia ja funktioita,
#  joita olio käyttää.
#Suojatut jäsenet (esim. _nimi tai __nimi) rajoittavat suoraa ulkopuolista muokkausta, 
# mutta luokka voi tarjota kontrolloidut metodit muuttamiseen.



#B. Mikä on olio? Miksi oliot ovat olemassa?

#Olio on ohjelmoinnissa “esine”, jolla on ominaisuuksia (tietoa, kuten nimi, ikä, väri) ja
#  toimintoja (metodeja, kuten aja(), tulosta()).
#Miksi oliot ovat olemassa:
#Ne auttavat järjestämään koodin loogisiin kokonaisuuksiin.
#Mahdollistavat uudelleenkäytön ja helpottavat ohjelman ylläpitoa.
#Tukevat periytymistä, jolloin uusia olioita voidaan tehdä vanhojen pohjalta ilman,
#  että kaikkea koodia tarvitsee kirjoittaa uudelleen.

#C. Mitä tarkoitetaan periytymisellä? Miksi sitä käytetään?

#Periytyminen tarkoittaa, että yksi luokka (aliluokka) voi periä ominaisuudet ja 
# toiminnot toiselta luokalta (yliluokka).
#Miksi sitä käytetään:
#Vähentää koodin toistoa.
#Mahdollistaa yhteisten toimintojen jakamisen useille luokille.
#Helpottaa ohjelman laajentamista ja ylläpitoa.

#Esimerkki:
#Jos sinulla on luokka Eläin ja luokka Koira perii Eläin, Koira saa automaattisesti 
# Eläin-luokan ominaisuudet (esim. nimi, ikä) ja metodit (esim. liiku()), 
# eikä niitä tarvitse kirjoittaa uudelleen.

#D. Miten luokka ja olio liittyvät toisiinsa? Miten määritellään
#  oma luokka? Miten siitä luodaan olio?

#uokka on kuin malli tai suunnitelma: se määrittelee, millaisia ominaisuuksia
#  (muuttujia) ja toimintoja (metodeja) oliolla on.
#Olio on luokan yksittäinen toteutus, konkreettinen esimerkki luokasta.


class Koira:
    def __init__(self, nimi):
        self.nimi = nimi
    def hauku(self):
        print(self.nimi + " sanoo: Hau!")

k = Koira("Rex")
k.hauku()  # Tulostaa: Rex sanoo: Hau!

#class Koira: määrittelee luokan.
#__init__ alustaa oliolle ominaisuudet (nimi, ikä).
#self viittaa juuri luotuun olioon.
#koira olio eli konkreettisia koiria luokasta Koira.


#E. Miten luokan/olion jäsenmuuttujat ja -funktiot toimivat?

#Selitetään lyhyesti:
#Jäsenmuuttuja (attribute) on muuttuja, joka kuuluu tietylle oliolle tai luokalle. 
# Se säilyttää olioon liittyvää tietoa.
#Jäsenfunktio (metodi) on funktio, joka kuuluu luokkaan ja 
# voi käyttää tai muuttaa jäsenmuuttujia.

class Auto:
    def __init__(self, merkki):
        self.merkki = merkki

    def nayta(self):
        print(self.merkki)

auto = Auto("Toyota")
auto.nayta()  # Tulostaa: Toyota

#merkki = jäsenmuuttuja
#nayta() = jäsenfunktio, joka näyttää muuttujan arvon

#F. Miten jäsenmuuttujat suojataan siten, että kukaan ulkopuolinen ei muuta niitä 
# hallitsemattomasti? Miten voidaan tarjota mahdollisuus muuttaa niitä tavalla, 
# jota luokka voi hallita (esim. pituuteen ei pysty laittamaan negatiivisia arvoja)?

class Henkilo:
    def __init__(self, ika):
        self.__ika = ika

    def get_ika(self):
        return self.__ika

    def set_ika(self, uusi_ika):
        if uusi_ika >= 0: self.__ika = uusi_ika

h = Henkilo(25)
print(h.get_ika())  # 25
h.set_ika(-5)       # ei muuta
h.set_ika(30)
print(h.get_ika())  # 30


#__ika = suojattu muuttuja (ei voi muuttaa suoraan ulkopuolelta)
#get_ika() = luokan hallitsema tapa lukea arvo
#set_ika() = luokan hallitsema tapa muuttaa arvo turvallisesti (esim. 
# tarkistus negatiiviselle luvulle)

#G. Miten periytyminen toteutetaan? Kerro myös metodien (jäsenfunktioiden) 
# ylikirjoittamisesta.

# Perusluokka
class Elain:
    def aantele(self):
        print("Ääni!")

# Aliluokka perii Elain-luokan
class Koira(Elain):
    def aantele(self):  # ylikirjoitus
        print("Hau hau!")

Koira().aantele()  # tulostaa: Hau hau!

#Selitys:
#Aliluokka perii yliluokan ominaisuudet.
#Metodia voi ylikirjoittaa aliluokassa muuttamaan käyttäytymistä.