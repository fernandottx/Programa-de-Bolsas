# Usa uma imagem base do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o script e o CSV para o diretório de trabalho
COPY etl.py .
COPY concert_tours_by_women.csv .

# Instala o pandas
RUN pip install --no-cache-dir pandas

# Executa o script Python
CMD ["python", "etl.py"]