
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




juncao =  list(zip(nomes, pesos))
maior =  max(juncao)
menor =  min(juncao[1])
tamanho =  len(juncao)
for valor in juncao:
     if valor == maior[1]:
         print(valor[0]) 
     
print("oi maior peso foi: {}".format(maior))
print("o menor peso foi: {}".format(menor))
print("ao todo foram cadastradas: {}".format(tamanho))
