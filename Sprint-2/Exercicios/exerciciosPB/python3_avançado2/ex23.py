def calcular_valor_maximo(operadores,operandos) -> float:
    operacoes = map(lambda op: eval(f"{op[1][0]}{op[0]}{op[1][1]}"), zip(operadores, operandos))
    return max(operacoes)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
print(calcular_valor_maximo(operadores, operandos))

