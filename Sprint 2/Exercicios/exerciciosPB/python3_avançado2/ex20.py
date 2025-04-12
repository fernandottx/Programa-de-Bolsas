with open("number.txt") as f:
    numeros = list(map(int, f))

pares = list(filter(lambda x: x % 2 == 0, numeros))
maiores_pares = sorted(pares, reverse=True)[:5]

print(maiores_pares)
print(sum(maiores_pares))
