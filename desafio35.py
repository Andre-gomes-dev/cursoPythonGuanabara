segmentos = []
i = 1
while i <= 3:
    valor = float(input("{}o segmento: ".format(i)))
    i += 1
    segmentos.append(valor)
if segmentos[0] < segmentos[1] + segmentos[2]:
    if segmentos[1] < segmentos[0] + segmentos[2]:
        if segmentos[2] < segmentos[0] + segmentos[1]:
            print("da pra formar um triangulo")
        else:
            print("nao forma um triangulo")



