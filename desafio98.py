

#metodos

#contagem de 1 a 10
def contanormal():
    print("Contagem de 1 ate 10, contando de  1 em 1 ")
    for valor in range(1,11):
        print(f"{valor}",end=" ")
    print("fim!")    
    print("-="*20)
    #contagem regressiva de 10 a 0, de 2 em 2
    print("Contagem de 10 ate 0, contando de  2 em 2 ")
    for valor in range(10,0, -2):
            print(f"{valor}", end=" ")
    print("fim!")  
    print("-="*20)



def contaPersonalizada(inicio, fim, passo):
     print("-="*20)
     print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
     if inicio > fim:
        for valor in range(inicio, fim, -passo):
          print(f"{valor} ", end=" ")  
     else:
        for valor in range(inicio, fim, passo):
          
          print(f"{valor} ", end=" ")  
     print("fim")     

contanormal()
print("Agora é a sua vez de personalizar a contagem! ")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contaPersonalizada(inicio, fim, passo)

#opcao de personalizar contagem
#inicio /  fim /  passo


#resultado da contagem personalizada