import random, time, os, names

random.seed(40)
qtd_nomes_unicos = 39080
qtd_nomes_aleatorios = 10000000

aux=[]

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f'Gerando {qtd_nomes_aleatorios} nomes aleatórios')

dados=[]

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open("Sprint-6/Exercicios/parte1-geração-e-massa-de-dados/etapa3/nomes_aleatorios.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines([f'{dado}\n' for dado in dados])