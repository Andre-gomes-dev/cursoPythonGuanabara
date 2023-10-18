
numeros = []
i = 1
armazenador = 0
while i <3:
   armazenador = int(input("{}° numero: ".format(i)))
   numeros.append(armazenador)
   i += 1

maior =  max(numeros)


if numeros[0] > numeros[1]:
   print("o PRIMEIRO numero é maior e seu valor é: {}".format(maior))
elif numeros[0] == numeros[1]:
   print("os numeros são iguais, e seus respectivos valores são: {}".format(maior))   
else:
   print("o SEGUNDO maior numero é maior e seu valor  é: {}".format(maior))

      