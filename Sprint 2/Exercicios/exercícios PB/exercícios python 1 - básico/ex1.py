a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

impares = []

for num in a:
    if num % 2 != 0:
        impares.append(num)

print(impares)

# Esse código percorre cada número da lista a, 
# verifica se ele é ímpar (num % 2 != 0) e, se for, adiciona à nova lista impares