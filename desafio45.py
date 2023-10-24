import random

jogadas = [0,1,2]
jogada = int(input("qual é a sua jogada"))

print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")

jokenpo = random.randint(0, len(jogadas))
print(jokenpo)


