def remove_duplicados(lista):
    return list(set(lista))

lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
resultado = remove_duplicados(lista_teste)
print(resultado)