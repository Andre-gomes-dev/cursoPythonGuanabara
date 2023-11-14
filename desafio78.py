valores = []
for i in range(0,5):
    valor = input("digite um valor para a posição {}: ".format(i))
    valores.append(valor)
maior =  max(valores)
menor =  min(valores)    
print("os valores digitados são: ".format(valores))    
print("o maior valor foi: {}".format(maior))
print("o menor valor foi: {}".format(menor))