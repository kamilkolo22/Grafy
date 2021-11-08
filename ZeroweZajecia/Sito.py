import numpy as np


def Liczby_pierwsze(n):
    lista = [x for x in range(1, n+1)]
    for i in lista:
        pass


def Sito(n):
    tablica = np.ones(n+1)
    i = 2
    while i <= np.sqrt(n):
        if tablica[i] == 1:
            j = i ** 2
            while j <= n:
                tablica[j] = 0
                j += i
        i += 1
    return [i for i in range(2, n+1) if tablica[i] == 1]


print(Sito(10))
