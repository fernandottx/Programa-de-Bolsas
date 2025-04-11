speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

valores_unicos = list(set(speed.values()))
print(valores_unicos)

# O código usa speed.values() para acessar os valores e set() para remover duplicatas. 
# Em seguida, converte de volta para lista.
