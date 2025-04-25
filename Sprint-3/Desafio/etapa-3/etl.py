# Importa as bibliotecas necessárias
import pandas as pd
import re

# Lê o CSV original usando pandas
df = pd.read_csv("concert_tours_by_women.csv")

# Renomeia a coluna "Adjustedgross (in 2022 dollars)" para "Adjusted gross (in 2022 dollars)"
df.rename(columns={"Adjustedgross (in 2022 dollars)": "Adjusted gross (in 2022 dollars)"}, inplace=True)

# Remove [qualquer coisa]
df["Tour title"] = df["Tour title"].apply(lambda x: re.sub(r'\[.*?\]', '', x))
# Remove tudo que não for letra, numero ou espaço
df["Tour title"] = df["Tour title"].apply(lambda x: re.sub(r'[^\w\s]', '', x))
# Normaliza múltiplos espaços
df["Tour title"] = df["Tour title"].apply(lambda x: re.sub(r'\s+', ' ', x).strip())

# Converte valores monetários para float (removendo $, vírgulas e letras)
def limpar_e_converter(valor):
    valor_str = re.sub(r'[^\d.]', '', str(valor))
    return float(valor_str)

# Separa as colunas que são consideradas como monetárias
colunas_monetarias = [
    "Actual gross",
    "Adjusted gross (in 2022 dollars)",
    "Average gross"
]

# Aplica a função às três colunas monetárias
for col in colunas_monetarias:
    df[col] = df[col].apply(limpar_e_converter)

# Extrai "Start year" e "End year" da coluna "Year(s)"
def extrair_anos(anos):
    if "-" in anos: # Para apenas as células que contém a pontuação '-'
        partes = anos.split("-") # Separa em 2 partes, antes e depois da pontuação '-'
        return pd.Series([int(partes[0]), int(partes[1])]) # Retorna os respectivos anos às colunas
    else: # Para apenas as células que não contém a pontuação '-'
        return pd.Series([int(anos), int(anos)]) # Retorna o mesmo ano para ambas as colunas
    
# Aplica a função à coluna "Year(s)"
df[["Start year", "End year"]] = df["Year(s)"].apply(extrair_anos)

# Seleciona as colunas que devem aparecer no Dataframe limpo
colunas_importantes = [
    "Rank",
    "Actual gross",
    "Adjusted gross (in 2022 dollars)",
    "Artist",
    "Tour title",
    "Shows",
    "Average gross",
    "Start year",
    "End year"
]

# Cria um novo Dataframe limpo baseado nas colunas preestabelecidas
df = df[colunas_importantes]

# Imprime o Dataframe limpo
print(df)

# Salva o DataFrame limpo em um novo arquivo CSV.
df.to_csv("csv_limpo.csv", index=False)