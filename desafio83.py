expressao = input("digite a expressão: ")
direito = 0
esquerdo = 0
for valor in expressao:
    if valor == "(":
        direito +=1
    elif valor == ")":
        esquerdo  +=1    

if direito > esquerdo or esquerdo > esquerdo:
    print("expressão invalida")
else:
    print("expressão valida")    

