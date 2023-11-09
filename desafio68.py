from operator import contains
import random

aleatorio =  random.randint(0, 10)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("VAMOS JOGAR PAR OU IMPAR ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
numero = int(input("diga um numero de 0 a 10:  "))
escolha = input("PAR ou IMPAR? [P/I]: ").upper().strip()

#variaveis
jogo = int(aleatorio + numero)
vitoria = ""
jogador = ""
computador = ""


#logica de par ou impar
if jogo % 2 == 0:
    vitoria = "PAR"
elif jogo %2 == 1:
    vitoria = "IMPAR"    
#atribuição referente a par e impar
if escolha == "P":
     jogador = "PAR"
     computador = "IMPAR"
elif escolha == "I":
     jogador =  "IMPAR"
     computador = "PAR"
else:
     print("digite uma opção válida")

#logica do vencedor

if vitoria in jogador:
      print("voce venceu")
elif vitoria in computador:
      print("computador venceu")     

print("o seu numero é: {} e o computador escolheu {}, logo deu {},  resultando em: {} ".format(numero, aleatorio, jogo, vitoria))

    

#logica de divisao para saber se é par ou impar


#logica de vencedor