from random import choice

n1 = input("Digite seu nome:>")
n2 = input("Digite seu nome:>")
n3 = input("Digite seu nome:>")
n4 = input("Digite seu nome:>")

lista = [n1, n2, n3, n4]

#fazer sorteio da lista
sorteado = choice(lista)

print(" "*20, "Nome Sorteado", " "*20)

print(f"{sorteado}")


if sorteado == n1:
    print("O nome sorteado foi o primeiro digitado")

if sorteado == n2:
    print("O nome sorteado foi o segundo digitado")

if sorteado == n3:
    print("O nome sorteado foi o terceiro digitado")

if sorteado == n4:
    print("O nome sorteado foi o quarto digitado")

#função len conta as unidades da lista
tamanho = len(lista)
print(len(lista))