sequencia =  int(input("ate onde quer contar?"))
i =0
anterior = 0
fibonacci = [0, 1]
while len(fibonacci) < sequencia:
    calculo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(calculo)
print(fibonacci)