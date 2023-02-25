#lista
import random

n1 = input("Digite seu nome:>")
n2 = input("Digite seu nome:>")
n3 = input("Digite seu nome:>")
n4 = input("Digite seu nome:>")

Alunos = [n1, n2, n3, n4]

#trazer os dados de forma aleatória
random.shuffle(Alunos)

print (Alunos)