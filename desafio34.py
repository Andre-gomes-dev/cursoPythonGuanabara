salario = int(input("qual é o valor do salario: "))

if salario <= 1250:
    SalarioComum = (salario * 15) / 100
    print("baseado no seu salario considerado comum, o seu aumento é de: {}".format(SalarioComum))
else:
    salarioAlto = (salario * 10) / 100
    print("baseado no seu salario considerado alto, o seu aumento é de R${}".format(salarioAlto))
