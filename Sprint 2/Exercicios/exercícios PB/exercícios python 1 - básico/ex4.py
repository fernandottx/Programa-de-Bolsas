def remove_duplicados(lista):
    return list(set(lista))

lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
resultado = remove_duplicados(lista_teste)
print(resultado)

# A função usa set() para eliminar duplicatas da lista. 
# Depois converte de volta para lista, sem garantir a ordem dos elementos.
