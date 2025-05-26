with open('estudantes.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

relatorio = []

for linha in linhas:
    partes = linha.strip().split(',')
    nome = partes[0]
    notas = sorted(map(int, partes[1:]), reverse=True)[:3]
    media = round(sum(notas) / 3, 2)
    relatorio.append((nome, notas, media))

for nome, notas, media in sorted(relatorio, key=lambda x: x[0]):
    print(f"Nome: {nome} Notas: {notas} Média: {media}")

