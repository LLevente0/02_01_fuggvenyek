"""4. Feladat
Írj egy programot, amelyben van egy 'kerulet' nevű függvény,
 amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is!
  Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó,
  és számolja ki a kerületét (0 tetszőleges paraméter: négyzet,
  1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!"""


def kerulet(a, *b):
    if len(b) == 0:
        return 4 * a
    elif len(b) == 1:
        return 2 * (a + b[0])
    elif len(b) == 2:
        return a + b[0] + b[1]
    else:
        return a + sum(b)




print(f'Négyzet kerülete: {kerulet(5)}')  # a = 5

print(f'Téglalap kerülete: {kerulet(5, 10)}')

print(f'Háromszög kerülete: {kerulet(3, 4, 5)}')

print(f'Sokszög kerülete: {kerulet(2, 3, 4, 5)}')