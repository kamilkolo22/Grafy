import timeit as tm


def Fibo(n):
    a1, a2 = 0, 1
    while n > 1:
        temp = a2
        a2 += a1
        a1 = temp
        n -= 1
    return a1


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def Fibo_rek(n):
    if n < 2:
        return n
    else:
        return Fibo_rek(n-1) + Fibo_rek(n-2)


def Fibo_lista(n=10):
    if n == 0:
        return None
    elif n == 1:
        return [0]
    else:
        lista = [0, 1]
        for i in range(2, n):
            lista.append(lista[-1] + lista[-2])
        return lista


# for i in range(1, 10):
#     #print(Fibo(i))
#     print(Fibo_rek(i))
print(tm.timeit(stmt=Fibo_lista))

