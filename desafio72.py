from num2words import num2words

def numerosExtenso(numero):
     numExtenso = num2words(numero, lang='pt_BR')
     return numExtenso



print("="* 30)
print('{:^30}'.format("Conversor em Extenso"))
print("="* 30)
while True:
    numero = int(input("digite um numero entre 0 e 20: "))
    if numero >=0 and numero <=20:
        print("numero aceito..")
        numExtenso = numerosExtenso(numero)
        print("o seu numero {}, em formato extenso é: {}".format(numero, numExtenso))
        resposta = input("quer continuar? [s/n]: ").lower().strip()
        
        if resposta == 's':
          print("vamos continuar...\n")
          print("="* 30)
          print('{:^30}'.format("Conversor em Extenso"))
          print("="* 30) 
          continue 
        else:
            print()
            print("encerrando programa...")
        break
    else:
        print("numero incorreto, tente novamente...") 
        continue


