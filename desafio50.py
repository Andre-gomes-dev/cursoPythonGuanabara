i = 1
soma = 0
while i <= 6:
    numero = int(input("digite o {}°numero: ".format(i)))
    if numero % 2 == 0:
        soma += numero
    i+=1
print(soma)