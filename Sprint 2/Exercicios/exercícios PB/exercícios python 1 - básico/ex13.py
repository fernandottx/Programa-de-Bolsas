import random

random_list = random.sample(range(500), 50)

random_list.sort()

valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list) / len(random_list)
meio = len(random_list) // 2
mediana = (random_list[meio - 1] + random_list[meio]) / 2 if len(random_list) % 2 == 0 else random_list[meio]

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")

# O código usa funções nativas para calcular mínimo, máximo, média e 
# ordena a lista para obter a mediana. A mediana é a média dos dois valores 
# centrais se a lista for par.