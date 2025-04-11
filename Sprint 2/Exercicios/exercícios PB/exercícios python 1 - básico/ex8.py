def imprime_parametros(*args, **kwargs):
    for arg in args:
        print(f"{arg}")
    for chave, valor in kwargs.items():
        print(f"{valor}")

imprime_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

# A função usa *args para capturar parâmetros não nomeados e **kwargs para nomeados, 
# imprimindo cada um separadamente.
