# Importa as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Lê o CSV original usando pandas
df = pd.read_csv("csv_limpo.csv")

# Q1 ---------------------------------------

# Conta quantas vezes cada artista aparece
contagem_artistas = df["Artist"].value_counts()

# Encontra o maior número de aparições
max_aparicoes = contagem_artistas.max()

# Obtem os artistas com esse número de aparições
artistas_mais_frequentes = contagem_artistas[contagem_artistas == max_aparicoes].index.tolist()

# Filtrar o DataFrame com esses artistas
df_filtrado = df[df["Artist"].isin(artistas_mais_frequentes)]

# Calcula a média do faturamento bruto (Actual gross) para esses artistas
media_artistas = df_filtrado.groupby("Artist")["Actual gross"].mean()

# Montar o DataFrame final com as colunas solicitadas
df_colunas = pd.DataFrame({
    "Artist": media_artistas.index,
    "Appearances": contagem_artistas[media_artistas.index].values,
    "Average Actual Gross": media_artistas.values
})

# Ordena pela média de faturamento bruto e mostra o artista no topo
df_ordenado = df_colunas.sort_values(by="Average Actual Gross", ascending=False).head(1)

# Redefine os índices
df1 = df_ordenado.reset_index(drop=True)

# Q2 ---------------------------------------

# Filtra turnês que aconteceram em apenas um ano
tour_um_ano = df[df["Start year"] == df["End year"]]

# Ordena pela média de faturamento bruto em ordem decrescente
tours_ordenados = tour_um_ano.sort_values(by="Average gross", ascending=False)

# Seleciona a primeira linha (maior média)
top_tour_um_ano = tours_ordenados.head(1)

# Redefine os índices
df2 = top_tour_um_ano.reset_index(drop=True)

# Q3 ---------------------------------------

# Cria nova coluna com o valor ajustado por show
df["Adjusted gross per show"] = df["Adjusted gross (in 2022 dollars)"] / df["Shows"]

# Ordena os dados com base nessa nova coluna, do maior para o menor
ordenado = df.sort_values(by="Adjusted gross per show", ascending=False)

# Seleciona os 3 primeiros
top_3 = ordenado.head(3)

# Seleciona as colunas relevantes: Artista, Turnê e o lucro por show
df3 = top_3[["Artist", "Tour title", "Adjusted gross per show"]]

# Redefine os índices
df3 = df3.reset_index(drop=True)

# Exporta para um arquivo txt seguindo o padrão preestabelecido
with open("./volume/respostas.txt", "w", encoding="utf-8") as f:
    f.write("Q1:\n\n")
    f.write(df1.to_string(index=False))
    f.write("\n\nQ2:\n\n")
    f.write(df2.to_string(index=False))
    f.write("\n\nQ3:\n\n")
    f.write(df3.to_string(index=False))

# Q4 ---------------------------------------

# Calcula somatório do faturamento bruto por artista
somatorio_faturamento_bruto = df.groupby("Artist")["Actual gross"].sum()

# Interseção: artista que mais aparece e tem maior somatório
artista_mais_frequente = contagem_artistas.idxmax()
artista_maior_somatorio = somatorio_faturamento_bruto.idxmax()

# Se forem diferentes, pega a que atende ambos critérios
if artista_mais_frequente == artista_maior_somatorio:
    artista_alvo = artista_mais_frequente
else:
    # Filtra entre os que mais aparecem, qual tem maior soma
    max_aparicoes
    top_artistas = contagem_artistas[contagem_artistas == max_aparicoes].index
    artista_alvo = somatorio_faturamento_bruto[top_artistas].idxmax()

# Filtra turnês da artista escolhida
artista_df = df[df["Artist"] == artista_alvo]

# Agrupa por ano e soma o faturamento
faturamento_por_ano = artista_df.groupby("Start year")["Actual gross"].sum()

# Plota gráfico de linhas
plt.figure(figsize=(10, 5))
plt.plot(faturamento_por_ano.index, faturamento_por_ano.values, marker='o', color='purple')
plt.title(f'Faturamento por ano das turnês de {artista_alvo}')
plt.xlabel("Ano de Início da Turnê")
plt.ylabel("Faturamento Bruto (Actual gross)")
plt.grid(True)
plt.tight_layout()
plt.savefig("./volume/Q4.png")  # <<< Exporta para PNG
plt.close()

# Q5 ---------------------------------------

# Agrupa por artista e somar o número total de shows
shows_por_artista = df.groupby("Artist")["Shows"].sum()

# Ordena os artistas pelo total de shows (do maior para o menor)
top_5_shows = shows_por_artista.sort_values(ascending=False).head(5)

# Cria o gráfico de colunas com matplotlib
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
plt.bar(top_5_shows.index, top_5_shows.values, color="skyblue")

# Adiciona título e rótulos
plt.title("Top 5 artistas com mais shows")
plt.xlabel("Artista")
plt.ylabel("Total de Shows")
plt.xticks(rotation=45)  # Rotaciona os nomes para melhor visualização
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("./volume/Q5.png")  # <<< Exporta para PNG
plt.close()