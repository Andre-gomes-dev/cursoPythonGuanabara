from  random import randint
from numpy import sort

numeros = list()
def numerosAleatorios(): 
  
    for valor in range(0,6):
        num = int(randint(0,120))
        numeros.append(num)  
    print(numeros)      
    

    numerosAleatorios()
def maior(*numero):
    for valor in numero:
        print(f"{valor}", end=" ")

