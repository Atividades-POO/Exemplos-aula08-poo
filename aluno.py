#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 08/07/2022
#
# classe aluno
class Aluno(Pessoa): # herda de Pessoa (classe base) e tem seus atributos e metodos herdados
  def __init__(self, nome, idade, matricula, nota1: int, nota2: int): # construtor da classe Aluno (subclasse)
    super().__init__(nome, idade) # chama o construtor da classe base (Pessoa)
    self.matricula = matricula # atributo da classe Aluno (subclasse)


  def falar(self): # metodo da classe Aluno (subclasse) que sobrescreve o metodo da classe base (Pessoa)
    print("Olá, meu nome é " + self.nome) # imprime o nome da classe Aluno (subclasse) e não o nome da classe base (Pessoa)
    print("Minha matrícula é " + self.matricula)  # imprime a matricula da classe Aluno (subclasse) e não a matricula da classe base (Pessoa)
    super().falar() # chama o metodo da classe base (Pessoa) que é o metodo falar() da classe Pessoa (classe base)

  # getters
  @property
  def matricula(self):
    return self._matricula

  @property
  def nota1(self):
    return self._nota1

  @property
  def nota2(self):
    return self._nota2


  # setters
  @matricula.setter
  def matricula(self, matricula):
    self._matricula = matricula

  @nota1.setter
  def nota1(self, nota1):
    self._nota1 = nota1

  @nota2.setter
  def nota2(self, nota2):
    self._nota2 = nota2

  # metodo que imprime a matricula do aluno
  def imprimir_matricula(self):
    print("Minha matrícula é " + self.matricula)

  # metodo que verfica se o aluno foi aprovado ou retido
  def verificar_aprovacao(self):
    media = (self.nota1 + self.nota2) / 2
    if media >= 7:
      return "Parabéns, você foi aprovado!"
    else:
      return "Infelizmente você foi retido!"

  # metodo que imprime a media do aluno
  def imprimir_media(self):
    media = (self.nota1 + self.nota2) / 2
    return f"Sua média é {media}"  # retorna a media do aluno

  # metodo que imprime dados do aluno
  def imprimir_dados(self):
    self.imprimir_matricula()
    print(self.verificar_aprovacao())
    print(self.imprimir_media())