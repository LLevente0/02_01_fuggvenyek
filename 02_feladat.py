"""2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek
(egész számok) között van páros, ellenkező esetben a visszatérési érték False!
A program tartalmazza a függvény hívását is!"""


def paros_e(szamok):
    #  index = 0
    # while index < len(szamok):
    #  if szamok[index] % 2 == 0:
    #     return True
    # index = index + 1
    #else:
    #return False

    # index = 0
    # for szam in szamok:
    #     if szamok[index] % 2 == 0:
    #         return True
    #     index = index + 1
    #
    # return False

    for index in range(len(szamok)):
        if szamok[index] % 2 == 0:
            return True

    return False

    # for szam in szamok:
    #     if szam % 2 == 0:
    #         return True
    #
    # return False


num = [3, 5, 9]
print(paros_e(num))
