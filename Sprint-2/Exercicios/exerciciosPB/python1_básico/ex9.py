class Lampada:
    def __init__(self, ligada: bool):
        self.ligada = ligada

    def liga(self):
        self.estado = True

    def desliga(self):
        self.estado = False

    def esta_ligada(self):
        return self.estado

lamp = Lampada(False)
lamp.liga()
print("A lâmpada está ligada?", lamp.esta_ligada())
lamp.desliga()
print("A lâmpada ainda está ligada?", lamp.esta_ligada())

