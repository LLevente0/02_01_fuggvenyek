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


