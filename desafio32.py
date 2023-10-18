import datetime

agora = datetime.datetime.now()
ano = agora.strftime("%Y")
analise = int(input("qual ano voce quer analisar? \ndigite 0 caso queira ver o ano atual\ndigite: "))
if analise == 0:
    testeBissexto = int(ano)  % 4 
    print("o ano atual é: {} ".format(ano))
    
    if testeBissexto == 0:
        print("o ano {} é bissexto".format(ano))
    else:
        print("o ano {} não é bissexto".format(ano))    

else: 
    testeBissexto = analise % 4 

    if testeBissexto == 0:
        print("o ano {} é bissexto".format(analise))
    else:
        testeBissexto = analise % 4
        print("o ano {} não é bissexto".format(analise))  