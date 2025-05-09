# Análise de Dados – Consultas Ambulatoriais

Este projeto realiza três análises exploratórias sobre uma base de dados contendo informações de **consultas médicas ambulatoriais** da região Nordeste entre Janeiro e Março de 2024, armazenada em um bucket AWS S3.

A base inclui os seguintes campos:
- `especialidade`
- `município`
- `idade`
- `sexo`
- `data da consulta`
- `hora da consulta`

---

## Requisitos

- Python 3.7+
- Permissões de leitura no bucket S3
- Bibliotecas:
  - `boto3`
  - `pandas`
  - `numpy`

Instale com:

```
pip install boto3 pandas numpy matplotlib
```

## Fonte dos dados

Página do site 'dados.gov.br' de onde fazer o download dos dados:

https://www.gov.br/ebserh/pt-br/hospitais-universitarios/regiao-nordeste/huol-ufrn/acesso-a-informacao/dados-abertos-1/05%20-%20Consultas%20Ambulatoriais/05-consultas-ambulatoriais-referencia_-janfevmar-de-2024.csv/view

O arquivo ca.csv está localizado no bucket S3:

`s3://programa-de-bolsas-fernando/etapa1/ca.csv`

## Análises Realizadas

Análise 1 - Total de consultas de todo o período por especialidade para crianças e idosos do sexo feminino de todos os municípios da região Nordeste.
Esta análise filtra os dados com dois critérios:

- Sexo igual a "Feminino"

- Para crianças e idosos, respectivamente: 
    - Idade menor ou igual a 12 anos
    - Idade maior ou igual a 60 anos

E em seguida realiza uma agregação por especialidade, contabilizando o número de consultas para esse grupo.

Técnicas utilizadas:

- Operadores lógicos `&` e `|` 

- Função de agregação: `groupby().size()`

[Clique aqui para visualizar o resultado da análise 1](analise1.csv)

[Clique aqui para visualizar o gráfico do resultado da análise 1](analise1.png)

Análise 2 – Classificação por faixa etária e conversão de tipos. Esta análise usa uma condicional para classificar cada paciente como:

- Maior de idade (idade ≥ 18)

- Menor de idade (idade < 18)

E também converte a coluna de idade de int para float.

Técnicas utilizadas:

- `np.where()` (condicional)

- `.astype(float)` (conversão de tipo)

[Clique aqui para visualizar o resultado da análise 2](analise2.csv)

[Clique aqui para visualizar o gráfico do resultado da análise 2](analise2.png)

Análise 3 – Consultas realizadas em março com especialidade contendo 'urologia'. 

Filtra todas as consultas:

- Realizadas no mês de março

- Cuja especialidade contenha a palavra "urologia"

Técnicas utilizadas:

- `.dt.month` (função de data)

- `.str.strip()` (função de string)

[Clique aqui para visualizar o resultado da análise 3](analise3.csv)

[Clique aqui para visualizar o gráfico do resultado da análise 3](analise3.png)