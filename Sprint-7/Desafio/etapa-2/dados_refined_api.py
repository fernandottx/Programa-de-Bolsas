import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, to_date, year, month, dayofmonth, quarter, lit, lower
from pyspark.sql.types import DateType

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'TRUSTED_OBRA_API_PATH',
    'TRUSTED_CAST_API_PATH',
    'TRUSTED_CREW_API_PATH',
    'REFINED_FATO_OBRA_API_PATH',
    'REFINED_DIM_ARTISTA_API_PATH',
    'REFINED_FATO_PARTICIPACAO_API_PATH',
    'REFINED_DIM_TEMPO_API_PATH'
])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df_obra = spark.read.parquet(args['TRUSTED_OBRA_API_PATH'])

df_obra_filtrada = df_obra.filter(
    lower(col("genero_principal")).isin("crime", "guerra")
)

df_fato_obra = df_obra_filtrada.withColumn("data_lancamento", to_date(col("data_lancamento")))

df_fato_obra.write.mode("overwrite").parquet(args['REFINED_FATO_OBRA_API_PATH'])

df_cast = spark.read.parquet(args['TRUSTED_CAST_API_PATH'])
df_crew = spark.read.parquet(args['TRUSTED_CREW_API_PATH'])

df_artistas_cast = df_cast.select(
    col("ator_id").alias("artista_id"),
    col("nome"),
    col("genero"),
    col("popularidade")
)

df_artistas_crew = df_crew.select(
    col("tecnico_id").alias("artista_id"),
    col("nome"),
    lit(None).cast("int").alias("genero"),
    col("popularidade")
)

df_dim_artista = df_artistas_cast.unionByName(df_artistas_crew)

df_dim_artista.write.mode("overwrite").parquet(args['REFINED_DIM_ARTISTA_API_PATH'])

obra_ids_filtradas = df_fato_obra.select("obra_id").distinct()

df_part_cast = df_cast.select(
    col("tmdb_id").alias("obra_id"),
    col("ator_id").alias("artista_id"),
    lit("cast").alias("tipo_participacao"),
    col("personagem"),
    lit(None).cast("string").alias("funcao"),
    col("departamento")
).join(obra_ids_filtradas, "obra_id")

df_part_crew = df_crew.select(
    col("tmdb_id").alias("obra_id"),
    col("tecnico_id").alias("artista_id"),
    lit("crew").alias("tipo_participacao"),
    lit(None).cast("string").alias("personagem"),
    col("funcao"),
    col("departamento")
).join(obra_ids_filtradas, "obra_id")

df_fato_participacao = df_part_cast.unionByName(df_part_crew)

df_fato_participacao.write.mode("overwrite").parquet(args['REFINED_FATO_PARTICIPACAO_API_PATH'])

df_tempo = (
    df_fato_obra
    .select(to_date(col("data_lancamento")).alias("data"))
    .filter(col("data").isNotNull())
    .dropDuplicates()
    .withColumn("ano", year(col("data")))
    .withColumn("mes", month(col("data")))
    .withColumn("dia", dayofmonth(col("data")))
    .withColumn("trimestre", quarter(col("data")))
)

df_tempo.write.mode("overwrite").parquet(args['REFINED_DIM_TEMPO_API_PATH'])

job.commit()
