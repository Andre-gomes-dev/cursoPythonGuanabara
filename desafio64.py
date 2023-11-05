sequencia = [0]
somaTotal = 0

while True:
        numero = int(input("digite um numero [999 para parar]: "))
        if numero != 999:
            sequencia.append(numero)
        else:
            print("finalizando..")
            break    
tamanho = len(sequencia) - 1
somaTotal = sum(sequencia)
print(somaTotal)
print(sequencia)
print(tamanho)

print("voce digitou {} numeros, e a soma entre eles foi:  {}".format(tamanho, somaTotal))