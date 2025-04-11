class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = ""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)

# A classe usa property para controlar o acesso ao atributo privado __nome. 
# O getter e setter permitem leitura e escrita seguras do atributo.
