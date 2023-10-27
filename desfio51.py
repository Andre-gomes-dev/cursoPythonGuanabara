priTermo = int(input("primeiro termo: "))
razao = int(input("razao: "))
decimo =  priTermo + (10 - 1 ) * razao
for i in range (priTermo, decimo + razao, razao):
    print(priTermo)
    priTermo += razao
     