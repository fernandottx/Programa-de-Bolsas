import boto3
import os
from datetime import datetime

BUCKET_NAME = 'data-lake-do-fernando'
CAMADA = 'Raw'
ORIGEM = 'Local'
FORMATO = 'CSV'

FILES = {
    "Movies": "data/movies.csv",
    "Series": "data/series.csv"
}

s3_client = boto3.client('s3')

today = datetime.today()
date_path = f"{today.year}/{today.month:02d}/{today.day:02d}"

def upload_s3(file_path, categoria):
    filename = os.path.basename(file_path)
    s3_key = f"{CAMADA}/{ORIGEM}/{FORMATO}/{categoria}/{date_path}/{filename}"
    print(f"Enviando {file_path} para s3://{BUCKET_NAME}/{s3_key}")

    s3_client.upload_file(file_path, BUCKET_NAME, s3_key)
    print("Upload realizado com sucesso.")

def main():
    for categoria, path in FILES.items():
        upload_s3(path, categoria)

if __name__ == "__main__":
    main()
