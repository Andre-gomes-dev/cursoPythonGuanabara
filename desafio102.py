def fatorial(valor, show=True):
        multiplica = 1
        for contador in range(valor, 1, -1):
            multiplica *= contador 
            if show:
                print(f" {contador}", end=" x")    
        print(f"{multiplica}") 
          
           
            




#programa principal
valor = int(input("digite o valor fatorial!: "))
fatorial(valor, show=False)
#chamar a function