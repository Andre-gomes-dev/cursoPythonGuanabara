
numeros = []
posicao3 = 0

for i in range(0,4):
    valor = int(input("digite um valor"))
    numeros.append(valor)

#posicao do numero 3
if 3 in numeros:
   posicao3 =  numeros.index(3)
   print("o primeiro  numero 3 se encontra na posição: {}".format(posicao3))
else:
    print("numero 3 não encontrado")

#quantas vezes o numero 9 aparece
numero9 = numeros.count(9)
print("o numero 9 aparece {} vezes".format(numero9))

#quais foram os numeros pares
countPares = 0
for i in numeros:
   if i % 2 == 0:
       countPares +=1

if countPares >=1:
    print("a contagem de número pares foi: {}".format(countPares))
else:
    print("não há numeros pares")
    