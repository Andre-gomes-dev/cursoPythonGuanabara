from datetime import datetime

agora =  datetime.now()
anoAtual = int(agora.year)
agenciaTrab =  dict
nome = input("Nome: ")
AnoNasc =  int(input("Ano de Nascimento: "))
CartTrabalho = int(input("Carteira de Trabalho (0 não possui): "))

#logica para saber idade
idade = anoAtual -  AnoNasc

agenciaTrab = {"Nome": nome, "AnoNasc": idade}


if CartTrabalho == 0:
     #ctps tem o valor 0
      print()
else:
     AnoContrat = int(input("Ano de contratação: "))
     Salario =  int(input("Salário: "))
     agenciaTrab["AnoContrat"] = AnoContrat
     agenciaTrab["Salario"] = Salario





#printando valores na tela
for posicao, (dicionario, valor) in enumerate(agenciaTrab.items()):
      print(f"-{dicionario} tem  o valor {valor}")
# 

#retorno do objeto

