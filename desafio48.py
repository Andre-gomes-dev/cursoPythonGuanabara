impar = []
soma = 0
#primeiro achar o impar

for i in range(1, 501, 2):
    if i % 3 == 0:
        impar.append(i)
        soma += i
print("o tamanho dos numeros primos é: {} ".format(len(impar)))   
print("a soma de todos esses numeros é: {} ".format(soma))      