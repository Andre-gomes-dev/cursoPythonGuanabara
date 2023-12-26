def calcTerreno(largura, comprimento):
    tamanhoString = len("Controle de Terrenos")
    print("-"*tamanhoString)
    resultado = largura * comprimento
    print(f"A área de um terreno de {largura}x{comprimento} é de {resultado}m²")

largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))    
calcTerreno(largura, comprimento)
