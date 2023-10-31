pesos = []
i = 1


#iteração para adcionar os pesos a lista
while i <= 5:
    addPeso = input("peso da {}° pessoa ".format(i))
    pesos.append(addPeso)
    i +=1

#realizando a logica de maior e menor peso:
maiorPeso = max(pesos)
menorPeso = min(pesos)

#jogando na tela os resultados
print("o maior peso é: {} e o menor peso é: {}".format(maiorPeso, menorPeso))