import random


listaAleatoria = []
dicionario = {}

print("== {} ==".format("RANKING DOS JOGADORES"))

# for cont in range(1, 5):
#     aleatorio =  random.randrange(1, 7)
#     listaAleatoria.append(aleatorio)
  
# dicionario.copy(listaAleatoria)

# for posicao, valor in enumerate(listaAleatoria, start=1):
#     print(f"{posicao}° lugar: jogador{posicao} com {valor}")
   
#print(f"valores sorteado: {aleatorio}")
   


for cont in range(1, 5):
    aleatorio = random.randrange(1, 7)
    dicionario[f"jogador{cont}"] = aleatorio

for posicao, (jogador, valor) in enumerate(dicionario.items(), start=1):
    print(f"{posicao}° lugar: {jogador} com {valor}")