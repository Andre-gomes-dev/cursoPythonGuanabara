print("---------FATORIAL CALCULATOR-----------")
numero = int(input("digite um numero: "))

fatorial = int(numero)
print("fatorial de {}!".format(fatorial))
while numero >1 :
    print("{}x".format(numero))
    numero -=1
    fatorial *= numero
print("x1\n=",fatorial)
