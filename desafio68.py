from operator import contains
import random

aleatorio =  random.randint(0, 10)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("VAMOS JOGAR PAR OU IMPAR ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
numero = int(input("diga um numero de 0 a 10:  "))
escolha = input("PAR ou IMPAR? [P/I]: ").upper().strip()

jogo = aleatorio + numero
vitoria = ""
if jogo % 2 == 0:
    vitoria = "PAR"
    vencedor = 
elif jogo %2 == 1:
    vitoria = "IMPAR"

print("o seu numero é: {} e o computador escolheu {}, logo deu {},  resultando em: {} ".format(numero, aleatorio, jogo, vitoria))

    
if escolha == "P":
     jogador = "PAR"
     computador = "IMPAR"
elif escolha == "I":
     jogador =  "IMPAR"
     computador = "PAR"
else:
     print("digite uma opção válida")
#logica de divisao para saber se é par ou impar


#logica de vencedor