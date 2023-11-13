


timesFutebol = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Fortaleza', 'Fluminense', 'Internacional', 
                'Grêmio', 'São Paulo', 'Sport', 'Ceará', 'Atlético Paranaense', 'Bahia', 'Corinthians', 
                'Juventude', 'Cuiabá', 'América Mineiro', 'Santos', 'Chapecoense', 'Vasco da Gama', 'Botafogo')

#5 primeiros da tupla
cincoPrimeiros = []
quatroUltimos = []
OrdemAlfabetica = []
procuraAlgo = []

for time in timesFutebol[:5]:
    
    cincoPrimeiros.append(time)
print("os 5 primeiros da lista são: {}".format(cincoPrimeiros))
print("\n")
#4 ultimos da lista
for time in timesFutebol[-4:]:
    quatroUltimos.append(time)
print("os ultimos 4 times são: {}".format(quatroUltimos))
print("\n")
#lista em ordem alfabetica
ordemAlfabetica = sorted(timesFutebol)
print("a lista em ordem alfabetica é \n assim: {}".format(ordemAlfabetica))
print("\n")
#por padrão dizer a ordem que o chapecoense se encontra na tupla. e pergunte se o usuario quer saber a ordem de outro 

if "Chapecoense" in timesFutebol:
   local = timesFutebol.index("Chapecoense")
   print(local)
else:
    print("ta aqui não")