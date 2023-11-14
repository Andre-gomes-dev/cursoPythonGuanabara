valores = []
while True: 
    
    valor = int(input("digite um valor: "))

    if valor in valores:
        print("não vou adcionar")
        print()
    else:
        valores.append(valor)
        print("valor adcionado")
        print()
    while True:

        resposta = input("quer continuar? [S/N]: ").upper().strip()
        print()
        if resposta == "S" or resposta == "N":
            break
        else:
            print("resposta incorreta, tente denovo.")
            print()
    if resposta == "N":
        break
print()
print("os valores digitados foram: {}".format(valores))    