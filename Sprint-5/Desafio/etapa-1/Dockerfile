FROM python:3.11-slim

WORKDIR /app

COPY uploader.py .
COPY data/ ./data/

RUN pip install --no-cache-dir boto3

CMD ["python", "uploader.py"]