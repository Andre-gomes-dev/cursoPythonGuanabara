import math
numero = int(input("digite um numero: "))
i = 1
countPrimo = 0
#verificando se 
while i <=numero:
    if numero % i == 0:
        countPrimo +=1    
    print("{}".format(i))
    i+=1

if countPrimo == 2:
    alternante =  "É PRIMO"
else:
    alternante = "NÃO É PRIMO"        
print("o numero {}, foi divisivel {} vezes e ele: {} ".format(numero, countPrimo, alternante))  


#raizQuadrada = math.sqrt(numero)
#-1print(raizQuadrada)