from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("Sprint-6/Exercicios/parte1-geração-e-massa-de-dados/etapa3/nomes_aleatorios.txt", header=False, inferSchema=True)

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes.printSchema()

df_nomes.show(10)