-- ETAPA 1: NORMALIZAÇÃO DA BASE DE DADOS

-- Tabela de Clientes
CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(40),
    estado VARCHAR(40),
    pais VARCHAR(40)
);

INSERT INTO Cliente VALUES (1, 'João Silva', 'São Paulo', 'SP', 'Brasil');
INSERT INTO Cliente VALUES (2, 'Maria Souza', 'Rio de Janeiro', 'RJ', 'Brasil');

-- Tabela de Carros
CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    km INT,
    classificacao VARCHAR(50),
    marca VARCHAR(80),
    modelo VARCHAR(80),
    ano INT
);

INSERT INTO Carro VALUES (1, 50000, 'Sedan', 'Toyota', 'Corolla', 2020);
INSERT INTO Carro VALUES (2, 30000, 'SUV', 'Honda', 'HR-V', 2021);

-- Tabela de Combustível
CREATE TABLE Combustivel (
    idCombustivel INT PRIMARY KEY,
    tipo VARCHAR(20)
);

INSERT INTO Combustivel VALUES (1, 'Gasolina');
INSERT INTO Combustivel VALUES (2, 'Diesel');

-- Tabela de Vendedores
CREATE TABLE Vendedor (
    idVendedor INT PRIMARY KEY,
    nome VARCHAR(15),
    sexo SMALLINT,
    estado VARCHAR(40)
);

INSERT INTO Vendedor VALUES (1, 'Carlos', 1, 'SP');
INSERT INTO Vendedor VALUES (2, 'Fernanda', 2, 'RJ');

-- Tabela de Locações
CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idCombustivel INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

INSERT INTO Locacao VALUES (1, 1, 1, 1, 1, '2024-03-01', '10:00:00', 3, 150.00, '2024-03-04', '12:00:00');
INSERT INTO Locacao VALUES (2, 2, 2, 2, 2, '2024-03-02', '14:00:00', 5, 200.00, '2024-03-07', '16:00:00');

-- ETAPA 2: CONVERSÃO PARA MODELO DIMENSIONAL

-- Tabela Dimensão Cliente
CREATE TABLE Dim_Cliente (
    idCliente INT PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(40),
    estado VARCHAR(40),
    pais VARCHAR(40)
);

INSERT INTO Dim_Cliente SELECT * FROM Cliente;

-- Tabela Dimensão Carro
CREATE TABLE Dim_Carro (
    idCarro INT PRIMARY KEY,
    km INT,
    classificacao VARCHAR(50),
    marca VARCHAR(80),
    modelo VARCHAR(80),
    ano INT
);

INSERT INTO Dim_Carro SELECT * FROM Carro;

-- Tabela Dimensão Combustível
CREATE TABLE Dim_Combustivel (
    idCombustivel INT PRIMARY KEY,
    tipo VARCHAR(20)
);

INSERT INTO Dim_Combustivel SELECT * FROM Combustivel;

-- Tabela Dimensão Vendedor
CREATE TABLE Dim_Vendedor (
    idVendedor INT PRIMARY KEY,
    nome VARCHAR(15),
    sexo SMALLINT,
    estado VARCHAR(40)
);

INSERT INTO Dim_Vendedor SELECT * FROM Vendedor;

-- Tabela Fato Locação
CREATE TABLE Fato_Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idCombustivel INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Dim_Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Dim_Carro(idCarro),
    FOREIGN KEY (idCombustivel) REFERENCES Dim_Combustivel(idCombustivel),
    FOREIGN KEY (idVendedor) REFERENCES Dim_Vendedor(idVendedor)
);

INSERT INTO Fato_Locacao SELECT * FROM Locacao;
