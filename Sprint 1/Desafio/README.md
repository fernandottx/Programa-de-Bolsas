# Instruções

Projeto: Normalização e Modelo Dimensional para Banco de Dados de Locação de Veículos

- Descrição

Este projeto tem como objetivo transformar um banco de dados relacional de uma concessionária em um modelo otimizado, utilizando duas etapas:

Normalização para eliminar redundâncias e garantir integridade dos dados.

Conversão para um Modelo Dimensional, permitindo análises avançadas e criação de relatórios eficientes.

O banco de dados gerencia locações de veículos, armazenando informações sobre clientes, carros, vendedores e transações.

- Tecnologias Utilizadas

Banco de Dados: SQLite

Linguagem: SQL

Modelo de Dados: Modelo Relacional e Modelo Dimensional

Ferramentas: DBeaver, DB Browser for SQLite

- Estrutura do Banco de Dados

1. Modelo Normalizado

O modelo normalizado divide os dados em tabelas para evitar redundâncias:

Tabelas Criadas:

Cliente (idCliente, nome, cidade, estado, pais)

Carro (idCarro, km, classificacao, marca, modelo, ano)

Combustivel (idCombustivel, tipo)

Vendedor (idVendedor, nome, sexo, estado)

Locacao (idLocacao, idCliente, idCarro, idCombustivel, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)

2. Modelo Dimensional

O modelo dimensional foi estruturado para otimizar a análise de dados.

Tabelas Dimensão:

Dim_Cliente (idCliente, nome, cidade, estado, pais)

Dim_Carro (idCarro, km, classificacao, marca, modelo, ano)

Dim_Combustivel (idCombustivel, tipo)

Dim_Vendedor (idVendedor, nome, sexo, estado)

Tabela Fato:

Fato_Locacao (idLocacao, idCliente, idCarro, idCombustivel, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)

- Como Usar

1. Configuração

Instale o SQLite (caso não tenha instalado).

Utilize o DB Browser for SQLite ou DBeaver para visualizar e manipular o banco de dados.

2. Importação do Banco de Dados

Baixe o arquivo concessionaria.sqlite.

Abra o arquivo no DB Browser for SQLite.

Execute as consultas SQL conforme desejado.

3. Inserindo Dados Exemplo

INSERT INTO Cliente VALUES (1, 'João Silva', 'São Paulo', 'SP', 'Brasil');
INSERT INTO Carro VALUES (1, 50000, 'Sedan', 'Toyota', 'Corolla', 2020);
INSERT INTO Combustivel VALUES (1, 'Gasolina');
INSERT INTO Vendedor VALUES (1, 'Carlos', 1, 'SP');
INSERT INTO Locacao VALUES (1, 1, 1, 1, 1, '2024-03-01', '10:00:00', 3, 150.00, '2024-03-04', '12:00:00');

🔹 Desenvolvido por: Fernando Teixeira
🔹 Contato: fernando.tx@outlook.com



