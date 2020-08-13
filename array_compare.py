import random

def porownaj_tablice():
    rozmiar_tablicy = random.randint(1, 100)
    print(rozmiar_tablicy)
    wynik = []
    licznik = 0
    tablicaAlice = []
    tablicaBob = []
    while licznik <= rozmiar_tablicy:
        tablicaAlice.append(random.randint(1, 100))
        tablicaBob.append(random.randint(1, 100))
        licznik = licznik + 1
    print('Tabela Alice: ', tablicaAlice)
    print('Tabela Boba:  ', tablicaBob)

    licznik = 0
    punktyAlice = 0
    punktyBob = 0
    for i in tablicaAlice:
        if tablicaAlice[licznik] > tablicaBob[licznik]:
            punktyAlice = punktyAlice + 1
        if tablicaAlice[licznik] < tablicaBob[licznik]:
            punktyBob = punktyBob + 1
        if tablicaAlice[licznik] == tablicaBob[licznik]:
            print("remis!")
        licznik = licznik + 1

    print('Punkty Alice : ', punktyAlice, ', punkty Boba : ', punktyBob)
    wynik.append(punktyAlice)
    wynik.append(punktyBob)
    #print(wynik)
    return wynik

print(porownaj_tablice())