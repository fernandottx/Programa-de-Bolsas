import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, lit, year, concat_ws, to_date

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'TRUSTED_FILMES_LOCAL_PATH',
    'TRUSTED_SERIES_LOCAL_PATH',
    'REFINED_FATO_OBRA_LOCAL_PATH',
    'REFINED_DIM_ARTISTA_LOCAL_PATH',
    'REFINED_DIM_TEMPO_LOCAL_PATH'
])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df_movies = spark.read.parquet(args['TRUSTED_FILMES_LOCAL_PATH']).withColumn("tipo", lit("movie"))
df_series = spark.read.parquet(args['TRUSTED_SERIES_LOCAL_PATH']).withColumn("tipo", lit("series"))

df_completo = df_movies.unionByName(df_series) \
    .filter(col("genero").isin("crime", "war"))

df_fato_obra_local = df_completo.select(
    "id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "anoTermino",
    "tempoMinutos", "genero", "notaMedia", "numeroVotos", "tipo"
)

df_fato_obra_local.write.mode("overwrite").parquet(args['REFINED_FATO_OBRA_LOCAL_PATH'])

df_dim_artista_local = df_completo.select(
    col("id").alias("id_obra"),
    "nomeArtista", "generoArtista", "personagem", "anoNascimento",
    "anoFalecimento", "profissao", "titulosMaisConhecidos"
)

df_dim_artista_local.write.mode("overwrite").parquet(args['REFINED_DIM_ARTISTA_LOCAL_PATH'])

df_tempo = (
    df_completo
    .select(col("anoLancamento").cast("int").alias("ano"))
    .filter(col("ano").isNotNull())
    .dropDuplicates()
    .withColumn("data", to_date(concat_ws("-", col("ano"), lit("01"), lit("01"))))
    .withColumn("mes", lit(None).cast("int"))
    .withColumn("dia", lit(None).cast("int"))
    .withColumn("trimestre", lit(None).cast("int"))
)

df_tempo.write.mode("overwrite").parquet(args['REFINED_DIM_TEMPO_LOCAL_PATH'])

job.commit()
