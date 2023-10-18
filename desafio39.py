import datetime

#dates
data =  datetime.datetime.now()
anoAtual =  data.strftime("%Y")
#conversão
anoConvertido =  int(anoAtual)
#pedindo data de nascimento
anoNasc= int(input("ano de nascimento"))

#descobrindo idade
idade  = anoConvertido -  anoNasc 

#descobrindo quando deveria ter se alistado
anosDescobrir = idade - 18
deveAlistar = anoConvertido  - anosDescobrir
#descobrindo quando deve se alistar
anosFaltam = 18 - idade
deveriaAlistado = anoConvertido + anosFaltam
if idade == 18:
    print("deve se alistar, pois você tem: {}anos".format(idade))

elif  idade >18:
    print("ja passou do tempo de alistamento, pois voce tem: {}anos".format(idade))
    print("voce deveria ter se alistado no ano de: {}".format(deveriaAlistado))

elif  idade <18:
    print("ainda nao deve se alistar, pois você tem: {}anos".format(idade))
    print("você deve se alistar no ano de {} ".format(deveAlistar))
