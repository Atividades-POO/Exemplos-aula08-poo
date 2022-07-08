#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 08/07/2022
#
# classe aluno
class Aluno(Pessoa): # herda de Pessoa (classe base) e tem seus atributos e metodos herdados
  def __init__(self, nome, idade, matricula): # construtor da classe Aluno (subclasse)
    super().__init__(nome, idade) # chama o construtor da classe base (Pessoa)
    self.matricula = matricula # atributo da classe Aluno (subclasse)

  def falar(self): # metodo da classe Aluno (subclasse) que sobrescreve o metodo da classe base (Pessoa)
    print("Olá, meu nome é " + self.nome) # imprime o nome da classe Aluno (subclasse) e não o nome da classe base (Pessoa)
    print("Minha matrícula é " + self.matricula)  # imprime a matricula da classe Aluno (subclasse) e não a matricula da classe base (Pessoa)
    super().falar() # chama o metodo da classe base (Pessoa) que é o metodo falar() da classe Pessoa (classe base)