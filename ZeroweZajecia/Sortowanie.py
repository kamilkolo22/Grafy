import numpy as np
import timeit
import random as rand


def QuickSort(tablica):
    # sortowanie szybkie
    def QSort(d, g):
        # pomocnicza procedura - sortuje fragment od d do g
        i = d
        j = g
        x = tablica[np.random.randint(d, g)]
        while i <= j:
            while tablica[i] < x:
                i += 1
            while tablica[j] > x:
                j -= 1
            if i <= j:
                t = tablica[i]
                tablica[i] = tablica[j]
                tablica[j] = t
                i += 1
                j -= 1
            if d < j:
                QSort(d, j)
            if i < g:
                QSort(i, g)
    QSort(0, len(tablica)-1)
    return tablica


def test1(n=100):
    tablica1 = [np.random.randint(1, 100000) for i in range(n)]
    QuickSort(tablica1)


def test2(n=100):
    tablica2 = [np.random.randint(1, 100000) for i in range(n)]
    tablica2.sort()


np.random.seed(100)
# print(QuickSort([1,3,5,4]))
# print(timeit.timeit(stmt=test2, number=1000))
# print(timeit.timeit(stmt=test1, number=1000))
tablica = [np.random.randint(1, 100000) for i in range(100)]
ar = np.array(tablica)
print(ar)
print(np.percentile(ar, 50))
