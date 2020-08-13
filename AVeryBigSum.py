#działa prawidłowo
import random

def aVeryBigSum(ar):
    #n = random.randint(1, 10)
    n = len(ar)
    print('Liczba elementów tablicy: ', n)
    tab = ar
    licznik = 0
    suma = 0
    while licznik < n:
        # tab.append(random.randint(0, 10**10))
        suma = suma + tab[licznik]
        print(tab[licznik])
        licznik = licznik + 1

    print(tab)
    print('Suma = ', suma)
    return suma


ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

aVeryBigSum(ar)
