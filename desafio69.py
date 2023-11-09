#cadastro com  idade e sexo
print("-=-=-=-=-=-=--=-=-=-=--=-=-=-=-= - -=-=")
print("      cadastro de pessoas        ")
print("-=-=-=-=-=-=--=-=-=-=--=-=-=-=-= - -=-=")

escolha = ""
pessoasTot = 0
mulheresCont = 0
homensCont = 0
pessoas18 = 0

#looping se quer continuar
while True:
  print("\n")
  print("-=-=-=-=-=-=--=-=-=-=--=-=-=-=-= - -=-=")
  print("      cadastro de pessoas        ")
  print("-=-=-=-=-=-=--=-=-=-=--=-=-=-=-= - -=-=")
  
  idade =  int(input("idade: "))
  sexo  =   input("sexo [M/F]").upper().strip()
  
  #logica de negocio
  if sexo == "F" and idade >20:
    mulheresCont +=1
  if sexo == "M":
    homensCont +=1
  if idade > 18:
    pessoas18 +=1


    #continuação do loopinmg
  escolha = input("quer continuar?: [S/N]").upper().strip()
  if escolha == "S":
    continue
  elif escolha == "N":
    pessoasTot +=1
    break
  else:
    print("escolha incorreta, programa encerrado")
    break 

#prints
print("total de pessoas com mais de 18 anos: {}".format(pessoas18))
print("Ao todo temos {}homen(s) cadastrados".format(homensCont))
print("e temos {} mulheres com menos de 20 anos".format(mulheresCont))