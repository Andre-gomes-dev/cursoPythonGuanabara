from datetime import datetime 
anos =[]
idades = []
contagemMaiorIdade = 0
contagemMenorIdade = 0
#confg de ano
agora = datetime.now()
anoAtual = int(agora.strftime("%Y"))


#logica de pedir o ano
i = 1
while i <=7:
        perguntaAno = int(input("em que ano a {}° nasceu?".format(i)))
        anos.append(perguntaAno) 
        idade =  anoAtual - perguntaAno 
        idades.append(idade)
        i+=1

#logica para saber quem é maior de idade
for i in idades:
        if i >=18:
            contagemMaiorIdade += 1 
        else:
           contagemMenorIdade += 1        

print("a quantidade de pessoas maior de idade é: {} ".format(contagemMaiorIdade))
print("a quantidade de pessoas menor de idade é: {} ".format(contagemMenorIdade))
