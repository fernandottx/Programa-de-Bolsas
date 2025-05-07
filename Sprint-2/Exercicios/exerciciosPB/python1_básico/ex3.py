primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, (primeiro, sobre, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{i} - {primeiro} {sobre} está com {idade} anos")