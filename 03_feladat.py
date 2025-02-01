"""3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok'
nevű függvényt, amely a paraméterként átvett listában megvizsgálja,
hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A
 program tartalmazza a függvény hívását is!"""


def harommal_oszthatok(lista):
    hanyszor_fordul_elo = 0
    for index in range(len(lista)):
        if lista[index] % 3 == 0:
            hanyszor_fordul_elo += 1
    print(hanyszor_fordul_elo)



szamok = [3, 4, 5, 6]
harommal_oszthatok(szamok)

