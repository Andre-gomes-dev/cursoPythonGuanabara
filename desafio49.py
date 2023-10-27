numero =  int(input("digite um numero para fazermos a tabuada 2.0"))
for i in range(1, 11):
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))