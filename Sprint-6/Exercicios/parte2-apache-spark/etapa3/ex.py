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

df_nomes.show(10)
