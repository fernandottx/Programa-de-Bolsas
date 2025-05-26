def soma_string_numeros(s):
    numeros = s.split(',')
    soma = sum(int(num) for num in numeros)
    return soma

entrada = "1,3,4,6,10,76"
resultado = soma_string_numeros(entrada)
print(resultado)

