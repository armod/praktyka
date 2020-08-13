#działa

def diagonalDifference(arr):
    #print(len(arr))
    sumaA = 0
    sumaB = 0
    wynik = 0
    for i in range(len(arr)):
        print('')
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
            if i==j:
                sumaA = sumaA + arr[i][j]
            if i+j==len(arr)-1:
                sumaB = sumaB + arr[i][j]
    print('\n\nSuma A =', sumaA)
    print('Suma B =', sumaB)
    wynik = (sumaA - sumaB)
    print('Wynik =', abs(wynik))
    return abs(wynik)

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

diagonalDifference(arr)