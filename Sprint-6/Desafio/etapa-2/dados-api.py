from datetime import datetime
import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import lit

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'RAW_API_PATH', 'TRUSTED_API_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

hoje = datetime.today()
ano, mes, dia = hoje.year, hoje.month, hoje.day

raw_api_path = args['RAW_API_PATH']
trusted_api_path = args['TRUSTED_API_PATH']

spark_df = spark.read.option("multiline", "true").json(raw_api_path)

spark_df = spark_df.withColumn("ano", lit(ano)) \
                   .withColumn("mes", lit(mes)) \
                   .withColumn("dia", lit(dia))
                   
df_api = DynamicFrame.fromDF(spark_df, glueContext, "df_api")

glueContext.write_dynamic_frame.from_options(
    frame=df_api,
    connection_type="s3",
    format="parquet",
    connection_options={
        "path": trusted_api_path,
        "partitionKeys": ["ano", "mes", "dia"]
    },
    transformation_ctx="trusted_api_sink"
)

job.commit()

# --RAW_API_PATH: s3://data-lake-do-fernando/Raw/TMDB/JSON/filmes-crime-guerra/2025/05/24/fa35b5e1.json
# --TRUSTED_API_PATH: s3://data-lake-do-fernando/Trusted/TMDB/PARQUET/filmes-crime-guerra/