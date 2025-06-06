from datetime import datetime
import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import lit

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'RAW_FILMES_PATH', 'RAW_SERIES_PATH', 'TRUSTED_FILMES_PATH', 'TRUSTED_SERIES_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

hoje = datetime.today()
ano, mes, dia = hoje.year, hoje.month, hoje.day

raw_filmes_path = args['RAW_FILMES_PATH']
raw_series_path = args['RAW_SERIES_PATH']
trusted_filmes_path = args['TRUSTED_FILMES_PATH']
trusted_series_path = args['TRUSTED_SERIES_PATH']

df_filmes = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="csv",
    format_options={"withHeader": True},
    connection_options={"paths": [raw_filmes_path]},
    transformation_ctx="df_filmes"
)

df_filmes_spark = df_filmes.toDF() \
    .withColumn("ano", lit(ano)) \
    .withColumn("mes", lit(mes)) \
    .withColumn("dia", lit(dia))

df_filmes_final = DynamicFrame.fromDF(df_filmes_spark, glueContext, "df_filmes_final")

glueContext.write_dynamic_frame.from_options(
    frame=df_filmes_final,
    connection_type="s3",
    format="parquet",
    connection_options={
        "path": trusted_filmes_path,
        "partitionKeys": ["ano", "mes", "dia"]
    },
    transformation_ctx="trusted_filmes_sink"
)

df_series = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="csv",
    format_options={"withHeader": True},
    connection_options={"paths": [raw_series_path]},
    transformation_ctx="df_series"
)

df_series_spark = df_series.toDF() \
    .withColumn("ano", lit(ano)) \
    .withColumn("mes", lit(mes)) \
    .withColumn("dia", lit(dia))

df_series_final = DynamicFrame.fromDF(df_series_spark, glueContext, "df_series_final")

glueContext.write_dynamic_frame.from_options(
    frame=df_series_final,
    connection_type="s3",
    format="parquet",
    connection_options={
        "path": trusted_series_path,
        "partitionKeys": ["ano", "mes", "dia"]
    },
    transformation_ctx="trusted_series_sink"
)

job.commit()

# --RAW_FILMES_PATH: s3://data-lake-do-fernando/Raw/Local/CSV/Movies/2025/05/24/movies.csv
# --RAW_SERIES_PATH: s3://data-lake-do-fernando/Raw/Local/CSV/Series/2025/05/24/series.csv
# --TRUSTED_FILMES_PATH: s3://data-lake-do-fernando/Trusted/Local/PARQUET/Movies/
# --TRUSTED_SERIES_PATH: s3://data-lake-do-fernando/Trusted/Local/PARQUET/Series/