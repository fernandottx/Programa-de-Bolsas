def my_map(lista, f):
    resultado = []
    for item in lista:
        resultado.append(f(item))
    return resultado

def potencia_de_dois(x):
    return x ** 2

entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
saida = my_map(entrada, potencia_de_dois)
print(saida)

