#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 08/07/2022
#
# importar as classes
from aluno import Aluno

# instanciar a classe Aluno (subclasse)
# aluno01 = Aluno("nome", idade, "matricula", nota1, nota2)
a1 = Aluno("Davi", 20, "12345", 80, 90) # instancia o objeto a1 da classe Aluno (subclasse)
a2 = Aluno("Maria", 21, "54321", 70, 80) # instancia o objeto a2 da classe Aluno (subclasse)

a1.falar() # chama o metodo falar() da classe Aluno (subclasse)
a1.imprimir_dados() # chama o metodo imprimir_dados() da classe Aluno (subclasse)

print('__________________________________________________')
a2.falar() # chama o metodo falar() da classe Aluno (subclasse)
a2.imprimir_dados() # chama o metodo imprimir_dados() da classe Aluno (subclasse)


#############################################################################################################################
print('###########################################')

# importar a classe cliente (subclasse)
from cliente import Cliente as C # importa a classe Cliente como C

# instanciar a classe Cliente (subclasse)
cliente01 = Cliente("nome", idade, "matricula", nota1, nota2)


