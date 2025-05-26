# Abre o arquivo actors.csv no modo leitura ("r") e com codificação UTF-8. 
# A função readlines() carrega todas as linhas do arquivo como uma lista de strings.
with open("Sprint 2/Exercicios/exerciciosPB/actors.csv", "r", encoding="utf-8") as file:
    linhas = file.readlines()

# Começa a definição de uma função chamada analisa_linha_csv, que vai quebrar a linha do CSV 
# respeitando vírgulas que possam estar dentro de aspas. Criamos uma lista campos para 
# armazenar os campos, uma variável current para montar o campo atual e
# um booleano dentro_aspas para saber se estamos dentro de aspas.
def analisa_linha_csv(linhas):
    campos = []
    atual = ''
    dentro_aspas = False
# Itera caractere por caractere na linha:
# Se encontrar uma aspas ("), alterna o estado de inside_quotes (entrando ou saindo de um campo entre aspas).
# Se encontrar uma vírgula fora de aspas, finaliza o campo atual.
# Se for qualquer outro caractere, adiciona ao campo atual.
    for x in linhas:
        if x == '"':
            dentro_aspas = not dentro_aspas
        elif x == ',' and not dentro_aspas:
            campos.append(atual.strip())
            atual = ''
        else:
            atual += x
# Após terminar a linha, adiciona o último campo à lista campos e retorna
# a lista contendo todos os campos separados corretamente.
    campos.append(atual.strip())
    return campos

# Inicializa uma lista chamada dados_atores onde cada item será um dicionário
# com os dados de um ator.
dados_atores = []

# Ignora a primeira linha (cabeçalho) e percorre as demais. 
# Remove espaços extras e quebras de linha com strip() e usa a função analisa_linha_csv()
# para obter os campos corretamente.
for linha in linhas[1:]:
    partes = analisa_linha_csv(linha.strip())
# Extrai os valores das colunas para variáveis. Convertendo os valores numéricos (float ou int)
# e armazenando o nome do ator e o filme de maior bilheteria como string.
    try:
        actor = partes[0]
        total_gross = float(partes[1])
        number_of_movies = int(partes[2])
        avg_per_movie = float(partes[3])
        top_movie = partes[4]
        gross = float(partes[5])
# Cria um dicionário com os dados do ator e adiciona na lista dados_atores
        dados_atores.append({
            "actor": actor,
            "total_gross": total_gross,
            "number_of_movies": number_of_movies,
            "avg_per_movie": avg_per_movie,
            "top_movie": top_movie,
            "gross": gross
        })
# Se houver qualquer erro (como dado inválido), mostra a linha com erro e a mensagem de exceção. 
    except Exception as e:
        print("Erro ao processar linha:", partes)
        print("Erro:", e)


# Cria a variável media_total para acumular os valores da coluna Average per Movie
# (média de receita por filme para cada ator).
media_total = 0.0

# Cria um contador para armazenar quantos atores/atrizes estão no dataset.
num_atores = 0

# Usa um for para percorrer cada item da lista dados_ator.
for ator in dados_atores:
# Adiciona o valor da chave "avg_per_movie" (média por filme do ator atual) ao total acumulado.
    media_total += ator["avg_per_movie"]
# A cada iteração, incrementa o contador de atores.
    num_atores += 1

# Calcula a média geral dividindo a soma total das médias pelo número de atores.
media_geral = media_total / num_atores

# Exibe a mensagem formatada com o valor da média
print(f"A média de receita bruta por filme considerando todos os atores é de ${media_geral:.2f} milhões.")
