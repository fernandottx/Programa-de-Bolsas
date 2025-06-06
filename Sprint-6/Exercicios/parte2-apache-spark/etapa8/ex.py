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

df_millenials = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994))

qtd_millenials = df_millenials.count()

print(f"Número de pessoas da geração Millenials: {qtd_millenials}")