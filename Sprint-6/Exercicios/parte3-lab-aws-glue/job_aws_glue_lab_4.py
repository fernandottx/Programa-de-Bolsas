import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import upper, col, count, desc, sum as _sum
from pyspark.sql import functions as F
from awsglue.job import Job

# Parâmetros de entrada
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_path = args['S3_INPUT_PATH']
output_path = args['S3_TARGET_PATH']

# Leitura do CSV com separador padrão e cast necessário
df_raw = spark.read.option("header", "true").option("delimiter", ",").csv(input_path)

# Verifique o schema original
print("Schema original:")
df_raw.printSchema()

# Cast na coluna quantidade para inteiro
df_cast = df_raw.withColumn("total", col("total").cast("int"))

# Converter nomes para MAIÚSCULO
df_upper = df_cast.withColumn("nome", upper(col("nome")))

# Contagem total de linhas
print(f"Total de linhas no DataFrame: {df_upper.count()}")

# Nome feminino com mais registros
df_fem = df_upper.filter(col("sexo") == "F")
mais_feminino = df_fem.orderBy(desc("total")).select("nome", "ano", "total").first()
print(f"Nome feminino com mais registros: {mais_feminino['nome']} em {mais_feminino['ano']} ({mais_feminino['total']} registros)")

# Nome masculino com mais registros
df_masc = df_upper.filter(col("sexo") == "M")
mais_masculino = df_masc.orderBy(desc("total")).select("nome", "ano", "total").first()
print(f"Nome masculino com mais registros: {mais_masculino['nome']} em {mais_masculino['ano']} ({mais_masculino['total']} registros)")

# Contagem de nomes agrupados por ano e sexo (total de linhas, não soma)
agrupado_ano_sexo = df_upper.groupBy("ano", "sexo").agg(count("*").alias("total"))
agrupado_ordenado = agrupado_ano_sexo.orderBy(col("ano").desc())
print("Contagem de nomes agrupados por ano e sexo (ano decrescente):")
agrupado_ordenado.show()

# Total de registros por ano (soma da total) — 10 primeiros anos
total_por_ano = df_upper.groupBy("ano").agg(_sum("total").alias("total"))
print("Total de registros por ano (primeiros 10, ordenado por ano crescente):")
total_por_ano.orderBy(col("ano").asc()).show(10)

# Escrita no S3 em JSON, particionado por sexo e ano
df_upper.write.mode("overwrite").partitionBy("sexo", "ano").json(f"{output_path}/frequencia_registro_nomes_eua")

print(f"Dados salvos com sucesso em {output_path}/frequencia_registro_nomes_eua")

job.commit()

# --S3_INPUT_PATH s3://lab-aws-glue-449060491526/lab-glue/input/nomes.csv
# --S3_TARGET_PATH s3://lab-aws-glue-449060491526/lab-glue