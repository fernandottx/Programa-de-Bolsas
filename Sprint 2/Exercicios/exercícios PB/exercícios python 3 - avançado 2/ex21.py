def conta_vogais(texto:str)-> int:
    return len(list(filter(lambda c: c.lower() in 'aeiou', texto)))

print(conta_vogais("Compass UOL é incrível"))

#A função usa 'filter' com 'lambda' para selecionar apenas vogais e 'len' para contar quantas são. 
# Caracteres acentuados são ignorados conforme solicitado.  