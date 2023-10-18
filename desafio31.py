distanciaViagem = int(input("qual a distancia da viagem? "))

if distanciaViagem <200: 
    viagemComum = distanciaViagem * 0.50
    print("o preço da sua viagem, resultou em: R${:.2f}".format(viagemComum))
else:
    viagemLonga = distanciaViagem * 0.45
    print("o preço da sua viagem, resultou em: R${:.2f}".format(viagemLonga))