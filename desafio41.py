import datetime 
agora = datetime.datetime.now()
anoString = agora.strftime("%Y")
anoAtual = int(anoString)
senioridade = ""


anoNasc = int(input("ano de nascimento: "))
idade =  anoAtual - anoNasc 
print(idade)

if idade <= 9:
    senioridade = "MIRIM"
    print("sua categoria é: {}".format(senioridade))
elif idade <=14:    
    senioridade =  "INFANTIL"
    print("sua categoria é: {}".format(senioridade))

elif idade <=19:    
    senioridade =  "JUNIOR"
    print("sua categoria é: {}".format(senioridade))    
elif  idade <=25:
   senioridade =  "SENIOR"
   print("sua categoria é: {}".format(senioridade))
else:
    senioridade =  "MASTER"
    print("sua categoria é: {}".format(senioridade))
#dizer a idade
#dizer a classificação


