jogadorNome  = input("Nome do Jogador: ")
partidasJogd = int(input(f"Quantas partidas {jogadorNome} jogou: "))
gols = []


for cont in range(0, partidasJogd):
    golsPartida = int(input(f"Quantos gols na partida {cont} "))
    gols.append(golsPartida)
somaGols = sum(gols)
detalhesPartida = {"nome": jogadorNome, "gols": gols, "total": somaGols}

    #prints
print("-="*20)   
print(detalhesPartida)
print("-="*20)    


for posicao, (dicionario, valor) in enumerate(detalhesPartida.items()):
    print(f"O campo {dicionario} tem o valor: {valor}")

print("-="*20)    


print(f"O jogador {jogadorNome} jogou {partidasJogd}")  
for posicao, valor in enumerate(gols):
    print(f"=> Na partida{posicao}, fez {valor} gols.")
