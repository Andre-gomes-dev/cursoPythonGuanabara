time = list()
jogador = dict()
partidas = list()
while True: 
    jogador.clear()
    jogador["nome"] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogadas: "))
    partidas.clear()
    for partida in range(0, tot):
        partidas.append(int(input(f"Quantos gols na partida {partida}? ")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas) 
    time.append(jogador.copy())

    resposta = ""   
    #saida para repetir ou sair do loop
    while resposta not in ["S", "N"]:
        resposta =  input("Quer continuar? [S/N]: ").upper()[0]
        if resposta not in ["S", "N"]:
            print("D'igite apenas S ou N")
        elif resposta == "N":
            print("saindo")
            break   
        elif resposta == "S":
            print("continue") 
            continue 
    
    if resposta == "N":
            break       
    
print("-="*30)
print("cod", end=" ")
for valor in jogador.keys():
    print(f"{valor:<15}", end=" ")
print()    
print("-"*40)


for chave, valor in enumerate(time):
    print(f"{chave:>3} " , end ='')
    for dado in valor.values():
        print(f"{str(dado):<15}", end = '')
    print()    
print("="*40)

while True:
    buscador =  int(input("Mostrar dados de qual jogador? [999] para stopar"))
    if buscador == 999:
        break
    if buscador >= len(time):
        print(f"erro nao existe jogador com codigo  ao lado: {buscador}")
    else:
<<<<<<< HEAD
        print("-- LEVANTAMENTO DE JOGADOR")
=======
        print(f"-- LEVANTAMENTO DE JOGADOR {time[buscador]["nome"]}:")
        for indc, quantGols in enumerate(time[buscador]["gols"]):
           print(f"no jogo {indc+1} fez {quantGols}") 
    print("-"*40)       
>>>>>>> ac7076192f9b7151de8f93d4c9a5489528815bf1
#tasks
    #colocar valores no dicionario e inserir numa lista.




