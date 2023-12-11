import random


listaAleatoria = []

print("== {} ==".format("RANKING DOS JOGADORES"))

for cont in range(1, 5):
    aleatorio =  random.randrange(1, 7)
    listaAleatoria.append(aleatorio)


for posicao, valor in enumerate(listaAleatoria, start=1):
    print(f"{posicao}° lugar: jogador{posicao} com {valor}")
   

#print(f"valores sorteado: {aleatorio}")
   