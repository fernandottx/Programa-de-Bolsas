import json

with open('person.json', 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)

# O código abre o arquivo JSON, faz o parsing com json.load() 
# e imprime o conteúdo em formato de dicionário.
