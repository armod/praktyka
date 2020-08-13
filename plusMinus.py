#działa

def plusMinus(arr):
    tablica = arr
    print('Rozmiar tablicy: ',len(tablica))
    positive = 0
    negative = 0
    zero = 0
    for i in tablica:
        print(i, end=' ')
        if i>0:
            positive = positive+1
        if i<0:
            negative = negative+1
    print("\n")
    print('Pozytywnych: ', positive)
    print('Negatywnych: ', negative)
    print(format(positive/len(tablica), '.6f'))
    #print(round(positive/len(tablica), 6))
    #print(round(negative/len(tablica), 6))
    print(format(negative/len(tablica), '.6'))
    print(format((len(tablica)-positive-negative)/len(tablica), '.6f'))


arr = [-4, 3, -9, 0, 4, 1]

plusMinus(arr)
