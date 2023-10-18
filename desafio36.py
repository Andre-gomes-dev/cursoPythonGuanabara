valorCasa = float(input("valor da casa"))
salario = float(input("seu salario: "))
anosDevedor = int(input("quantos anos pretende pagar: "))


porcentagem =  (salario * 30) /100 
prestacaoMensal =  valorCasa / (anosDevedor * 12) 

print(porcentagem)

if prestacaoMensal <= porcentagem:
     print("a prestação será de: {:.2f}".format(prestacaoMensal))
     print("emprestimo aprovado")
else:
     print("prestação será de {:.2f}".format(prestacaoMensal))
     print("emprestimo negado")