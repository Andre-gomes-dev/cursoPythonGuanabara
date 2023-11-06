
#looping mostrando a tabuada
while True:
    print("\n--------TABUADA-----------")
    print("regras: caso queira parar digite numero negativo, ex: -2")
    print("caso queira calcular a tabuada de algum numero apenas digite abaixo...")
    numero = int(input("qual numero: "))

    if numero <0:
        print("finalizando tabuada...")
        break
    elif numero >0:
        for i in range(1, 11):
            multiplicado = numero * i
            print("{}x{} ={} ".format(numero, i, multiplicado))
    print("\n-------------------------------")        
#caso seja digitado algum valor negativo o looping ira encerrar.