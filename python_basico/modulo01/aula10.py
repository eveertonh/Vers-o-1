#aqui o professor está usando o polimorfismo
print("*"*20, "soma", "*"*20)

n1 = int(input("DIgite o primeiro número:> "))
n2 = int(input("DIgite o segundo número:> "))

soma = n1 + n2

n3 = int(input("DIgite o primeiro número:> "))
n4 = int(input("DIgite o segundo número:> "))

subtracao = n3 - n4

n5 = int(input("DIgite o primeiro número:> "))
n6 = int(input("DIgite o segundo número:> "))

multiplicacao = n5 * n6

n7 = int(input("DIgite o primeiro número:> "))
n8 = int(input("DIgite o segundo número:> "))

divisao = n7 / n8

print("*"*20, "RESULTADOS", "*"*20)
print(f"a soma entre {n1} e {n2} é {soma}")
print(f"a subtracao entre {n3} e {n4} é {subtracao}")
print(f"a multiplicacao entre {n5} e {n6} é {multiplicacao}")
print(f"a divisao entre {n7} e {n8} é {divisao}")