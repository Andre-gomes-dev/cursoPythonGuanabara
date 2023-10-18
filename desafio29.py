velocidade = int(input("qual a velocidade atual do veiculo? "))

if velocidade >80:
    print("multado, a velocidade maxima local é 80km/h")
    taxaMulta= velocidade - 80
    multa = taxaMulta * 7
    print("voce foi multado em R${}".format(multa))
else:
    print("a sua velocidade é permitida")