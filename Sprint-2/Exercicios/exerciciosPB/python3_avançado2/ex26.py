def pares_ate(n:int):
    for i in range(2, n + 1, 2):
        yield i

for numero in pares_ate(10):
    print(numero)
