def conta_vogais(texto:str)-> int:
    return len(list(filter(lambda c: c.lower() in 'aeiou', texto)))

print(conta_vogais("Compass UOL é incrível"))

