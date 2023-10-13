import math
angulo = float(input("Digite o angulo que voce deseja: "))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print("o angulo de {} tem o SENO de {:.2f}".format(angulo, seno))
print("o angulo de {} tem o COSSENO de{:.2f}".format(angulo, cosseno))
print("o angulo de {} tem a TANGENTE de{:.2f}".format(angulo, tangente))