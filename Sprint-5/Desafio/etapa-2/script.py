import requests
import boto3
import json
import os
from datetime import datetime
from uuid import uuid4

CHAVE_API = os.environ['TMDB_API_KEY']
BUCKET_S3 = 'data-lake-do-fernando'
GENERO_IDS = [80, 10752]  # Crime = 80, Guerra = 10752
ANO_INICIO = 1900
ANO_FIM = 2000

s3 = boto3.client('s3')

def buscar_filmes_por_ano(ano, pagina=1):
    url = 'https://api.themoviedb.org/3/discover/movie'
    parametros = {
        'api_key': CHAVE_API,
        'language': 'pt-BR',
        'sort_by': 'popularity.desc',
        'include_adult': False,
        'include_video': False,
        'page': pagina,
        'primary_release_year': ano,
        'with_genres': ','.join(map(str, GENERO_IDS))
    }
    resposta = requests.get(url, params=parametros)
    return resposta.json()

def buscar_detalhes_filme(filme_id):
    url = f'https://api.themoviedb.org/3/movie/{filme_id}'
    parametros = {'api_key': CHAVE_API, 'language': 'pt-BR'}
    resposta = requests.get(url, params=parametros)
    return resposta.json()

def buscar_creditos_filme(filme_id):
    url = f'https://api.themoviedb.org/3/movie/{filme_id}/credits'
    parametros = {'api_key': CHAVE_API, 'language': 'pt-BR'}
    resposta = requests.get(url, params=parametros)
    return resposta.json()

def salvar_no_s3(dados):
    agora = datetime.now()
    ano, mes, dia = agora.strftime('%Y'), agora.strftime('%m'), agora.strftime('%d')
    caminho = f'Raw/TMDB/JSON/filmes-crime-guerra/{ano}/{mes}/{dia}/{str(uuid4())[:8]}.json'
    corpo = json.dumps(dados, ensure_ascii=False)
    s3.put_object(Bucket=BUCKET_S3, Key=caminho, Body=corpo)
    print(f"Arquivo salvo com sucesso: s3://{BUCKET_S3}/{caminho}")

def lambda_handler(evento=None, contexto=None):
    todos_os_dados = []
    print('\nColetando dados...')

    for ano in range(ANO_INICIO, ANO_FIM + 1):
        for pagina in range(1, 3):  
            dados = buscar_filmes_por_ano(ano, pagina)

            for filme in dados.get('results', []):
                detalhes = buscar_detalhes_filme(filme['id'])

                generos = detalhes.get('genres', [])
                if not generos or generos[0]['id'] not in (80, 10752):
                    continue

                creditos = buscar_creditos_filme(filme['id'])

                diretor = None
                for pessoa in creditos.get('crew', []):
                    if pessoa.get('job') == 'Director':
                        diretor = pessoa.get('name')
                        break

                atores = creditos.get('cast', [])
                atores_principais = [ator.get('name') for ator in atores]

                genero_feminino_presente = any(ator.get('gender') == 1 for ator in atores)

                filme_extraido = {
                    'id': detalhes.get('id'),
                    'titulo': detalhes.get('title'),
                    'data_lancamento': detalhes.get('release_date'),
                    'genero_principal': generos[0]['name'] if generos else None,
                    'generos': generos,
                    'descricao': detalhes.get('overview'),
                    'nota_media': detalhes.get('vote_average'),
                    'total_votos': detalhes.get('vote_count'),
                    'popularidade': detalhes.get('popularity'),
                    'duracao': detalhes.get('runtime'),
                    'idiomas_falados': detalhes.get('spoken_languages'),
                    'paises_producao': detalhes.get('production_countries'),
                    'empresas_producao': detalhes.get('production_companies'),
                    'colecao': detalhes.get('belongs_to_collection'),
                    'diretor': diretor,
                    'atores_principais': atores_principais,
                    'orcamento': detalhes.get('budget'),
                    'receita': detalhes.get('revenue'),
                    'genero_feminino_presente': genero_feminino_presente
                }

                todos_os_dados.append(filme_extraido)

                if len(todos_os_dados) == 100:
                    salvar_no_s3(todos_os_dados)
                    todos_os_dados = []

    if todos_os_dados:
        salvar_no_s3(todos_os_dados)

if __name__ == "__main__":
    lambda_handler()
