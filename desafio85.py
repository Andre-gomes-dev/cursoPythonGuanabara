i = 1
valores = [[], []]
while i<=7:
    valor = int(input("digite o {}° ".format(i)))
    if valor % 2 == 0:
        valores[0].append(valor)
    elif valor % 2 == 1:
          valores[1].append(valor) 
    i+=1
print(valores)
