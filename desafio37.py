import math
print("escolha uma das bases para conversão: ")
print("1 para binario")
print("2 para octadecimal")
print("3 hexadecimal")
opcao  = int(input("sua opção: "))
numero = int(input("digite um numero inteiro: "))

conversor = []
divisaoResto = 0
if opcao == 1: #binario
  while numero >0: 
        divisaoResto =  numero  % 2
        conversor.append(divisaoResto)
        numero =  numero  // 2
  print(conversor)                
#octa
elif opcao == 2:
  testeOcta = oct(numero)[2:]
  print(testeOcta)

#hexadecimal
elif opcao == 3:
  testeHexa =  hex(numero)[2:]
  print(testeHexa)
#tratamento leve de erro
else:
    print("escolha uma opção valida") 

