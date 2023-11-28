import random

jogos = []
megaSena = []

print("="*40)
print("{:^40}".format("joga Na megaSena"))
print("="*40)

jogo = int(input("quantos jogos voce quer sortear: "))
print("sorteando {} jogos".format(jogo))
print(f"-=-=-= sorteando {jogo:5^} jogos -=-=-=")


#sorteio

# for valor in range(0, jogo):
#     for cont in range(1, 7):
#         aleatorio = random.randrange(1, 60)
#         jogos.append(aleatorio)
#     megaSena.append(jogos[:])
#     jogos.clear()

# for posicao, valor in enumerate(megaSena):
#     print(f"jogo{posicao}: {valor} ")



#solução chatgpt sem repetições de numeros, analisar e ver como posso melhorar sem alterar minha solução por completo.
for _ in range(jogo):
    jogo = random.sample(range(1, 61), 6)  # Seleciona 6 números sem repetição de 1 a 60
    megaSena.append(jogo)

for posicao, valor in enumerate(megaSena):
    print(f"Jogo {posicao + 1}: {valor}")






