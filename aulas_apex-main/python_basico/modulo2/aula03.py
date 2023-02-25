chopp = int(input("Digite quantos chopes você tomou na oktober:>"))


if chopp == 0 :
    print("voce não bebeu")

elif chopp >= 1 and chopp <= 5 :
    print("voce ja esta entrando na zona de risco")
    multa = chopp * 100
    print("você vai pagar {} reais de multa". format(multa))


elif chopp > 5 :
    print("você está alterado")
    multa = chopp * 100
    #print(f"você vai pagar {multa} reais de multa")
    print("você vai pagar {} reais de multa". format(multa))















