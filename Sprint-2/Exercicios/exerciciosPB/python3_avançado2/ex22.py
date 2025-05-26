def calcula_saldo(lancamentos) -> float:
    from functools import reduce
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    return reduce(lambda acc, val: acc + val, valores)

lancamentos = [(200, 'D'), (300, 'C'), (100, 'C')]
print(calcula_saldo(lancamentos))

