import  random
print("vou pensar em um numero entre 0 e 5")
numero = int(input("em que numero eu pensei?"))
aleatorio = int(random.randrange(6))


if numero == aleatorio:
    print("parabens, voce acertou")
else:
    print("infelizmente voce errou")    


