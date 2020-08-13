#rozwiązanie prawidłowe

def porownaj_tablice(a, b):
    wynik = []
    #tablicaAlice = []
    #tablicaBob = []
    tablicaAlice = a
    tablicaBob = b
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
        licznik = licznik + 1

    print('Punkty Alice : ', punktyAlice, ', punkty Boba : ', punktyBob)
    wynik.append(punktyAlice)
    wynik.append(punktyBob)
    print(type(wynik))
    return wynik

#podaj liczby oddzielone spacją
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

print(porownaj_tablice(a, b))