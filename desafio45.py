import random

#arrays
jogadas = [0,1,2]
tipoJoken = ["PEDRA", "PAPEL", "TESOURA"]

#interação com usuario
print("=================================\n")
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
jogada = int(input("qual é a sua jogada"))
print("================================")

#interação da maquina ao capturar um numero aleatorio
jokenpo = random.randint(0, len(jogadas))
juncaoJoken = [tipoJoken[i] for i in jogadas]

print("o computador escolheu: {} ".format(juncaoJoken[jokenpo]))
print("voce escolheu: {} ".format(juncaoJoken[jogada]))

#computadorVitorias
if juncaoJoken[jokenpo] == "PAPEL" and juncaoJoken[jogada] == "PEDRA":
     print()
     print("papel venceu a Pedra")
     print("computador venceu")   
if juncaoJoken[jokenpo] == "PEDRA" and juncaoJoken[jogada] == "TESOURA":
    print()
    print("pedra venceu tesoura")
    print("computador venceu")
if juncaoJoken[jokenpo] == "TESOURA" and juncaoJoken[jogada] == "PAPEL":
    print("tesoura vence papel")
    print("computador venceu")
#JogadorVitorias
if juncaoJoken[jogada] == "PAPEL" and juncaoJoken[jokenpo] == "PEDRA":
    print()
    print("papel venceu a Pedra")# da pra por .format e adaptar as {} 
    print("jogador venceu")

if juncaoJoken[jogada] == "PEDRA" and juncaoJoken[jokenpo] == "TESOURA":
    print()
    print("pedra venceu tesoura")
    print("jogador venceu")

if juncaoJoken[jogada] == "TESOURA" and juncaoJoken[jokenpo] == "PAPEL":
    print()
    print("tesoura vence papel")
    print("jogador venceu")
#Empates
if juncaoJoken[jogada] == "PAPEL" and juncaoJoken[jokenpo] == "PAPEL":
    print()
    print("EMPATE!, PAPEL E PAPEL")

if juncaoJoken[jogada] == "TESOURA" and juncaoJoken[jokenpo] == "TESOURA":
    print()
    print("EMPATE, TESOURA E TESOURA")

if juncaoJoken[jogada] == "PEDRA" and juncaoJoken[jokenpo] == "PEDRA":
    print()
    print("EMPATE!, PEDRA E Pedra")

#papel pedra
#tesoura papel
#pedra tesoura


