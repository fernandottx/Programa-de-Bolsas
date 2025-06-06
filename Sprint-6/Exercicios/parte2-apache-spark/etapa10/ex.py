from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, floor, col, when

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("Sprint-6/Exercicios/parte1-geração-e-massa-de-dados/etapa3/nomes_aleatorios.txt", header=False, inferSchema=True)

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes = df_nomes.withColumn("Escolaridade_ID", floor(rand() * 3))

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(col("Escolaridade_ID") == 0, "Fundamental")
    .when(col("Escolaridade_ID") == 1, "Medio")
    .otherwise("Superior")
)

df_nomes = df_nomes.drop("Escolaridade_ID")

df_nomes = df_nomes.withColumn("Pais_ID", floor(rand() * 12))

df_nomes = df_nomes.withColumn(
    "Pais",
    when(col("Pais_ID") == 0, "Argentina")
    .when(col("Pais_ID") == 1, "Bolivia")
    .when(col("Pais_ID") == 2, "Brasil")
    .when(col("Pais_ID") == 3, "Chile")
    .when(col("Pais_ID") == 4, "Colombia")
    .when(col("Pais_ID") == 5, "Equador")
    .when(col("Pais_ID") == 6, "Guiana")
    .when(col("Pais_ID") == 7, "Paraguai")
    .when(col("Pais_ID") == 8, "Peru")
    .when(col("Pais_ID") == 9, "Suriname")
    .when(col("Pais_ID") == 10, "Uruguai")
    .otherwise("Venezuela")
)

df_nomes = df_nomes.drop("Pais_ID")

df_nomes = df_nomes.withColumn("AnoNascimento", floor(rand() * (2010 - 1945 + 1)) + 1945)

df_nomes = df_nomes.withColumn(
    "Geracao",
    when((col("AnoNascimento") >= 1944) & (col("AnoNascimento") <= 1964), "Baby Boomers")
    .when((col("AnoNascimento") >= 1965) & (col("AnoNascimento") <= 1979), "Geração X")
    .when((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994), "Millennials")
    .when((col("AnoNascimento") >= 1995) & (col("AnoNascimento") <= 2015), "Geração Z")
)

df_nomes.createOrReplaceTempView("pessoas")

df_geracoes_por_pais = spark.sql("""
    SELECT Pais, Geracao, COUNT(*) AS Quantidade
    FROM pessoas
    WHERE Geracao IS NOT NULL
    GROUP BY Pais, Geracao
    ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
""")

df_geracoes_por_pais.show(truncate=False)
