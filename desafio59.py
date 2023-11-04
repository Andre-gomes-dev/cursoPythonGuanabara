#inputs
valor1 = 0
valor2 = 0

#variaveis
somar = 0
multiplicar = 0
numeros = []
maior = 0

print("digite dois valores \n")
valor1 = int(input("primeiro valor: "))
valor2 = int(input("segundo valor:  "))

def digitaValor(valor1, valor2):
    while True:
       
        print("[1] somar")
        print("[2] multiplicar")
        print("[3] maior")
        print("[4] novos numeros")
        print("[5] sair do programa")

        opcao = int(input("qual é a sua opção"))

        if opcao == 1:
            somar = valor1 + valor2
            print("a soma dos valores {} e {} é: {}".format(valor1, valor2, somar))
        elif opcao == 2:
            multiplicar = valor1 * valor2
            print("o multiplicação dos valores {} e {}, resultou em: {}".format(valor1, valor2, multiplicar))
        elif opcao == 3:
            numeros.append(valor1)
            numeros.append(valor2)  
            maior = max(numeros)
            print("entre o numero {} e {} o maior valor é; {}".format(valor1, valor2, maior))
        elif opcao == 4:
            print("digite dois valores \n")
            valor1 = int(input("primeiro valor: "))
            valor2 = int(input("segundo valor:  "))
            continue
        elif opcao == 5:
            print("")
            break
        else:
             print("escolha uma opção valida, tente denovo")    

while True:
    digitaValor(valor1, valor2)
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() == 's':
        break
    else:
        print("vamos continuar")
print("programa finalizado com sucesso! ")                 