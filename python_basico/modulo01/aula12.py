from random import choice

n1 = input("Digite o nome:>")
n2 = input("Digite o nome:>")
n3 = input("Digite o nome:>")
n4 = input("Digite o nome:>")
n5 = input("Digite o nome:>")
n6 = input("Digite o nome:>")
n7 = input("Digite o nome:>")

lista = [n1, n2, n3, n4, n5, n6, n7]

sorteando = choice(lista)

print(f"O nome sorteado foi {sorteando}")
