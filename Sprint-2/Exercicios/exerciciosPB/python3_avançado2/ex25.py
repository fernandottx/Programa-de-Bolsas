def maiores_que_media(conteudo: dict) -> list:
    media = sum(conteudo.values()) / len(conteudo)
    filtrados = filter(lambda item: item[1] > media, conteudo.items())
    return sorted(filtrados, key=lambda item: item[1])

conteudo = {
    'Arroz': 4.99,
    'Feijão': 3.49,
    'Macarrão': 2.99,
    'Leite': 3.29,
    'Pão': 1.99
}

resultado = maiores_que_media(conteudo)
for produto, valor in resultado:
    print(f"{produto}: {valor}")

