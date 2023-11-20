numeros = []
par = []
impar = []

while True:
    print("="*30)
    print("{:^30}".format("listinha de numeros"))
    print("="*30)

    numero = int(input("digite um numero: "))
    numeros.append(numero)  

    #par
    if numero % 2 ==0:
        par.append(numero)
    else:
        impar.append(numero)
    #impar

    while True:
        resposta =  input("quer continuar? [S/N]: ").upper().strip()
        print()
        if resposta == "S" or resposta == "N":
            break
        else:
            print("resposta incorreta, tente novamente..")
    if resposta == "N":
        print("Encerrando...")
        break

print("lista completa: {}".format(numeros))
print("pares: {}".format(par))
print("impares: {}".format(impar))    
