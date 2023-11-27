matriz = [0,0,0], [0,0,0], [0,0,0]
paresTot= 0
for cont in range(0,3):
    for cont2 in range(0, 3):
     matriz[cont] [cont2] = int(input(f"adcione um valor na matriz: [{cont} {cont2}]: "))
     if matriz[cont] [cont2] %2 == 0:
            paresTot +=1

somaColuna = 0
for cont in range(0,3 ):
    
    for cont2 in range(0, 3):
        print(f"[{matriz[cont][cont2]:^5}]", end=" ")  
    print()   



#encontrar valores pares no total
print(f"o total de numeros pares na matriz é: {paresTot}")

#soma dos valores da terceira coluna
somaTercColuna = []
somaTercColuna.append(matriz[0][2])
somaTercColuna.append(matriz[1][2])
somaTercColuna.append(matriz[2][2])
somaColuna = sum(somaTercColuna)
print(f"o valor da terceira coluna é {somaColuna}")


#o maior valor da segundaLinha (1)
maiorValorsegunColuna = []
maiorValorsegunColuna.append(matriz[1][0])
maiorValorsegunColuna.append(matriz[1][1])
maiorValorsegunColuna.append(matriz[1][2])
maiorValor = max(maiorValorsegunColuna)

print(f"o maior valor da matriz é: {maiorValor}")
