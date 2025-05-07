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


# Usam a função max() para identificar qual ator possui o maior valor na chave "avg_per_movie".
# key=lambda ator: ator["avg_per_movie"] informa que o critério de comparação deve ser a média de bilheteria por filme.
# O resultado (ator_maior_media) será o dicionário completo com os dados do ator.
ator_maior_media = max(dados_atores, key=lambda ator: ator["avg_per_movie"])

# Exibe a mensagem formatada com nome do ator e valor da média
print(
    f"O ator com a maior média de receita bruta por filme é {ator_maior_media['actor']} "
    f"com uma média de ${ator_maior_media['avg_per_movie']:.2f} milhões por filme."
)
