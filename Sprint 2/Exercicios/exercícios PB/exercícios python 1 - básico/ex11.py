def divide_em_tres(lista):
    tamanho = len(lista) // 3
    return lista[:tamanho], lista[tamanho:2*tamanho], lista[2*tamanho:]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = divide_em_tres(lista)
print(parte1, parte2, parte3)

# A função calcula o tamanho de cada parte dividindo o total por 3 e 
# usa slicing para separar a lista. O resultado são três sublistas com partes iguais.
