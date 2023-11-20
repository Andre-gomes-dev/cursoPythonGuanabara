
nomes = []
pesos = []

while True:


    print("="*30)
    print("{:^30}".format("cadastro"))
    print("="*30)

    nome = input("Nome: ")
    peso = int(input("Peso: "))
    nomes.append(nome)
    pesos.append(peso)

    while True:
        resposta = input("quer continuar? [S/N]: ").upper().strip()
        if resposta == "S" or resposta == "N":
                break
        
    if resposta == "N":
        break
maior =  max(pesos)
menor =  min(pesos)
tamanho =  len(nomes)




for valor in pesos:
     if valor == maior:
         print(valor) 
     
print("oi maior peso foi: {}".format(maior))
print("o menor peso foi: {}".format(menor))
print("ao todo foram cadastradas: {}".format(tamanho))