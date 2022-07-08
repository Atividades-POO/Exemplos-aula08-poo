#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 08/07/2022
#
# classe base pessoa02
class Pessoa02:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    self.nomeClasse = self.__class__.__name__ # nome da classe

  def falando(self):
    return f"O objeto {self.nomeClasse}, fala: Olá, meu nome é {self.nome}"

  # getters
  @property
  def nome(self):
    return self._nome

  @property
  def idade(self):
    return self._idade


  # setters
  @nome.setter
  def nome(self, valor):
    self._nome = valor

  @idade.setter
  def idade(self, valor):
    self._idade = valor
