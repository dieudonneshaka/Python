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

