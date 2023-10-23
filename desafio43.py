# Abaixo de 17	Muito abaixo do peso
# Entre 17 e 18,49	Abaixo do peso
# Entre 18,5 e 24,99	Peso normal
# Entre 25 e 29,99	Acima do peso
# Entre 30 e 34,99	Obesidade I
# Entre 35 e 39,99	Obesidade II (severa)
# Acima de 40	Obesidade III (mórbida)

import math
estatistica = ""
peso = float(input("o seu peso: "))
altura =  float(input("a sua altura: "))
imc =  peso / (altura * altura)
print("o seu imc é: {:.1f}".format(imc))

if imc < 17:
    estatistica =  "Muito Abaixo do peso"
    print("voce está: {}.".format(estatistica))
elif imc < 18.5:
    estatistica =  "Abaixo do peso"
    print("voce esta: {}".format(estatistica))   
elif imc < 25:
    estatistica =  "Peso Normal"
    print("voce esta: {}".format(estatistica))     
elif imc < 30:
    estatistica =  "Acima do peso"
    print("voce esta: {}".format(estatistica))   
elif imc < 35:
    estatistica =  "Obesidade I"
    print("voce esta: {}".format(estatistica))   
elif imc < 40:
    estatistica =  "Obesidade II(SEVERA)"
    print("voce esta: {}".format(estatistica))   
elif imc >=40:
    estatistica =  "Obesidade III(MÓRBIDA)"
    print("voce esta: {}".format(estatistica))        