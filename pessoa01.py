#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 08/07/2022
#
# classe base pessoa
class Pessoa01:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

    def falar(self):
      print("Olá, meu nome é " + self.nome)

    # getters
    @property
    def nome(self):
      return self._nome

    @property
    def idade(self):
      return self._idade


    # setters
    @nome.setter
    def nome(self, nome):
      self._nome = nome

    @idade.setter
    def idade(self, idade):
      self._idade = idade
