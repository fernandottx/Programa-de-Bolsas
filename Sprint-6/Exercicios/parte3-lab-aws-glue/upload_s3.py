import boto3

bucket_name = 'lab-aws-glue-449060491526'
file_path = 'nomes.csv'
s3_key = 'lab-glue/input/nomes.csv'

s3 = boto3.client('s3')

s3.upload_file(file_path, bucket_name, s3_key)

print(f'Arquivo enviado para s3://{bucket_name}/{s3_key}')