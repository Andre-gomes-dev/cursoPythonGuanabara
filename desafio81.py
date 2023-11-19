valores = []
valoresInverso = []
resposta = ""

while True:   
    print("="*30)
    print("{:^30}".format("valores.com"))
    print("="*30)

    valor = int(input("digite um valor: "))
    valores.append(valor)
    

    while True: 
        resposta = input("quer continuar? [S/N]: ").upper().strip()
        print()
        if resposta == "S" or resposta == "N":
            break
        else:
            print()
            print("valor incorreto tente novamente...")    
    if resposta == "N":
        break   
#total de valores
totalValores =len(valores)

#valor 5 na lista
if 5 in valores:
    print("o valor 5 está presente na lista")
else: 
    print("o valor 5 NÃO esta na lista")    

#5 valores em decrescente
for i in reversed(valores):
    valoresInverso.append(i)

print("a lista ao contraria é: {}".format(valoresInverso))
print("voce digitou: {} valores".format(totalValores))

