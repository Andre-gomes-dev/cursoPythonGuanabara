from itertools import count
from operator import index
import math
print("=-=-=-=-=-=-=-=--=-=-=-=-=-=--==-=-=--=-=-=-=-")
print("=" * 30)
print("                   BANCO CEV                ")
print("=-=-=-=-=-=-=-=--=-=-=-=-=-=--==-=-=--=-=-=-=-")
valor =int(input("digitar o valor retirado: "))
total =  valor
cedula = 50
totalCedula =  0

while True:
    if total >= cedula:
        total -=cedula
        totalCedula +=1
    else:
        if totalCedula> 0:
            print("total de {} cédulas de R${}".format(totalCedula, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break              


# 
# cedulas = [50, 20, 10, 1]
# valores = []
# impressao = []
# contagem = valor // cedulas[0]


# for cedula in cedulas:
#     cedula * valor


# for cedula in cedulas:
#   contagem =  valor // cedula
#   tentativa = contagem * cedula
#   impressao.append(contagem)
#   valores.append(tentativa)
#   total  = sum(valores)  
#   if total == valor:
#     break
#   else:
#     continue
