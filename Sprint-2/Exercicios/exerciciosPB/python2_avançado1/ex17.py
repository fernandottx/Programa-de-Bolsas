class Calculo:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

x = 4
y = 5
calc = Calculo()
print(f"Somando: {x}+{y} = {calc.somar(x, y)}")
print(f"Subtraindo: {x}-{y} = {calc.subtrair(x, y)}")

