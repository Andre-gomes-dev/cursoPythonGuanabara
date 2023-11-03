#Informações de auto-apresentação
import random
print("sou seu computador \n")

#regras: 
print("o jogo é bastante simples, vou pensar em um numero e voce tenta acertar")
print("escolha um numero entre 0 a 10")
numero = int(input("tente advinhar: "))

#logica do numero aleatorio
aleatorio = random.randint(0, 10)

validacao =  False
while validacao ==  False:
    if numero != aleatorio:
        if numero <aleatorio:
            print("mais...")
            numero = int(input("qual o palpite: "))
        elif numero > aleatorio:
            print("menos...")
            numero = int(input("qual o palpite: "))
    else:
        validacao = True
        print("era esse mesmo: {}".format(aleatorio))


