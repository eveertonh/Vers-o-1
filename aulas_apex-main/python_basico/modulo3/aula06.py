from time import sleep

nome = input("Digite seu nome:> ")
sobrenome = input("Digite seu sobrenome:> ")
idade = int(input("Digite sua idade:> "))
            
for lista in range(0,2): 
    nota = int(input("Digite a sua nota:> "))
# acumulando as notas digitadas
    lista_notas = [nota]
#calculando a média
    media = sum(lista_notas)/ len(lista_notas)

situacao = "Reprovado tente novamente"

if media >= 7:
    sleep(2)
    for c in range(0, 10):
        print('*')
        sleep(1)
situacao = "parabens voce foi aprovado"

#arquivando as variaveis no dicionario
dicionario = {"nome" : nome, "sobrenome" : sobrenome, "idade" : idade, "media" : media, "situacao" : situacao }

print(f"{dicionario['nome']} {dicionario['sobrenome']} {dicionario['idade']} {dicionario['situacao']}")





