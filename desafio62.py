priTermo = int(input("primeiro termo: "))
razao = int(input("razao: "))
countTermos = 0
escolha = 10


while True:
    decimo =  priTermo + (escolha - 1 ) * razao
        #10 TERMOS DA PA
    for i in range (priTermo, decimo + razao, razao):
        print(priTermo)
        countTermos +=1 
        priTermo += razao
    print("PAUSA")
    escolha = int(input("quantos termos voce quer mostrar a mais? "))
   
    if escolha == 0:
        print("saindo do programa...")
        break
    else:
        priTermo = decimo + razao  
        escolha +=1
    #ADCIONANDO MAIS TERMOS
   
print("foram calculados {} termos".format(countTermos))
    # escolha = input("quantos termos voce quer mostrar a mais? ")    
    # if escolha == 0:
    #     print("saindo do programa...")
    #     break
    # else:
    #    continue 

