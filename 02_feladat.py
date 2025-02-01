"""2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek
(egész számok) között van páros, ellenkező esetben a visszatérési érték False!
A program tartalmazza a függvény hívását is!"""


def paros_e(szamok):
    if any(n % 2 == 0 for n in szamok):
        return True
    else:
        return False


num = [3, 4, 5]
print(paros_e(num))