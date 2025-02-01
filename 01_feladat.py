"""1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat)
összeadja és az összegükkel tér vissza!
A program tartalmazza a függvény hívását is!"""

def osszegzo(lista):
    #sum(lista)
    osszeg = 0
    for szam in lista:
        osszeg += szam
    return osszeg


print(osszegzo([3, 4, 5]))


"""2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek
(egész számok) között van páros, ellenkező esetben a visszatérési érték False! 
A program tartalmazza a függvény hívását is!"""



