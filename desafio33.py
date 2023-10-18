numeros  = []
i = 1
while i <=3:
   valor = input("{}o valor? ".format(i))
   numeros.append(valor)
   i+=1 

print("o menor valor da lista é: {}".format(min(numeros)))
print("o maior valor da lista é: {}".format(max(numeros)))

