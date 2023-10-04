numero = int(input("digite um número para ver sua tabuada: "))

print("-----------------")
i = 1
while i <= 10:
    multiplicado = numero * i
    print(numero, "x", i, "=", multiplicado)
    i += 1
print("-----------------")
