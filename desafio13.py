salario = float(input("qual é o salario do funcionario: "))
porcentagem = (salario *15) / 100
aumento = salario + porcentagem
print("um funcionario que ganhava R${}, com 15% De aumento, passa a receber R${:.2f}".format(salario, aumento))
