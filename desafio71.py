from itertools import count
from operator import index
import math
print("=-=-=-=-=-=-=-=--=-=-=-=-=-=--==-=-=--=-=-=-=-")
print("                   BANCO CEV                ")
print("=-=-=-=-=-=-=-=--=-=-=-=-=-=--==-=-=--=-=-=-=-")

cedulas = [50, 10, 1]
valor =int(input("digitar o valor retirado: "))
# teste = list(valor)
# tamanho = len(valor)

#logica de divisao do valor com o tamanho da palavra:

calculo50 = valor // 50
total = calculo50 * 50

valor10 = valor  - total 
calcula10 =  valor10 // 10

valor5 =  valor
print(calculo50, calcula10, valor10)

# print(tamanho)