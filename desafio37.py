
print("escolha uma das bases para conversão: ")
opcao  = input("sua opção: ")
numero = int(input("digite um numero inteiro: "))

conversor = []
divisaoResto = 0
if opcao == 1: #binario
  while numero >0: 
        divisaoResto =  numero  % 2
        conversor.append(divisaoResto)
        numero =  numero  // 2
        print(numero)              
else:
    print("escolha uma opção valida") 

print(conversor)   
