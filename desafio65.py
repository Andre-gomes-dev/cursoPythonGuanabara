
#variaveis
maiorValor =0
menorValor = 0
countNumeros = 0
media = 0
numeros = []
while True:
    numero = int(input("digite um número"))
    numeros.append(numero)
    ask = input("quer continuar?").lower().strip()
    if ask == "s":
        continue
    elif ask == "n":
        print("finalizando....")
        break   
    else:
        print("digite uma opção valida...")   
        continue
    #logica de media e quantidade de numeros
countNumeros = len(numeros)    
media = sum(numeros) / countNumeros
    #maior valor e menor
maior = max(numeros)
menor = min(numeros)
    #prints
print("voce digitou {} números e a média foi {}".format(countNumeros, media)) 
print("o maior valor foi {} e o menor foi {}".format(maior, menor))
