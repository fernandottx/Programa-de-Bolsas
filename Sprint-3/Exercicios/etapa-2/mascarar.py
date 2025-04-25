# Importa o módulo que permite gerar hashes
import hashlib

while True:
    texto = input("Digite uma string para mascarar com SHA-1: ")  # Recebe entrada do usuário
    hash_sha1 = hashlib.sha1(texto.encode())  # Converte para bytes e gera o hash SHA-1
    print("Hash SHA-1:", hash_sha1.hexdigest())  # Mostra o hash no terminal em hexadecimal