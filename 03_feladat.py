"""3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok'
nevű függvényt, amely a paraméterként átvett listában megvizsgálja,
hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A
 program tartalmazza a függvény hívását is!"""


# def harommal_oszthatok(lista):
#     hanyszor_fordul_elo = 0
#     for index in range(len(lista)):
#         if lista[index] % 3 == 0:
#             hanyszor_fordul_elo += 1
#     return hanyszor_fordul_elo
#
#
#
# szamok = [3, 4, 5, 6]
# print(harommal_oszthatok(szamok))



"""3.2 Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat 
tárolja el a program egy listában, és ezt értékelje ki a függvény! 
(Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)"""

def harommal_oszthatok(lista):
    hanyszor_fordul_elo = 0
    for index in range(len(lista)):
        if lista[index] % 3 == 0:
            hanyszor_fordul_elo += 1
    return hanyszor_fordul_elo


szamok = []
def szam_hozzaadas():
    szam = int(input("Adj meg számokat! "))
    szamok.append(szam)
    print(szamok)

folytat = True
while folytat == True:
    szam_hozzaadas()
    if any(n < 0 for n in szamok):
        break

print(f"\nA listában {harommal_oszthatok(szamok)} darab 3-mal osztható szám van.")