import random

#arrays
jogadas = [0,1,2]
tipoJoken = ["PEDRA", "PAPEL", "TESOURA"]

#interação com usuario
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
jogada = int(input("qual é a sua jogada"))

#interação da maquina ao capturar um numero aleatorio
jokenpo = random.randint(0, len(jogadas))
juncaoJoken = [tipoJoken[i] for i in jogadas]

print(juncaoJoken[jokenpo])
print(jokenpo)



