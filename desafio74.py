import random

numeros = []

for i in range(0,5):
    aleatorio = random.randint(0,100)
    numeros.append(aleatorio)
    
#maiior valor do array
maior = max(numeros)

#menor valor do array
menor =  min(numeros)

#prints
print("os numeros aleatorios foram: {}".format(numeros))
print("o maior numero foi: {}\n e o menor foi: {}".format(maior, menor))