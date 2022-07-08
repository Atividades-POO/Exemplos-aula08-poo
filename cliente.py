#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 08/07/2022
#
# importa a classe Pessoa02 como P2
from pessoa02 import Pessoa02 as P2

# classe cliente (subclasse)
class Cliente(P2):

  def comprar(self):
    return f"O objeto {self.nomeClasse} comprando algo!"