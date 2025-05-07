# Usa imagem base com Python
FROM python:3.10-slim

# Define diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do host para o container
COPY job.py .
COPY csv_limpo.csv .

# Instala as dependências necessárias
RUN pip install pandas matplotlib

# Executa o script quando o container roda
CMD ["python", "job.py"]
