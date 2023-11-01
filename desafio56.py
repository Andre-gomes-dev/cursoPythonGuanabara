import numpy as np

#entrada de arrays e variaveis
nomes = []
idades = []
sexos = []
i= 1

nome = ""
idade = 0
sexo = ""
menos20 = 0
#looping pedindo as informações das pessoas
while i <=4:
    
    print("-------{}° Pessoa --------".format(i))
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ")
    
    if sexo == "F" and idade <20:
        menos20 += 1
    #adcionando no array
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
    
    i+=1


#verificação da média de idade do grupo.
media  = np.mean(idades)

#verificar o homem mais velho e dizer sua idade e nome.
maior =  max(idades)
posicaoMaior =  idades.index(maior)
nomeMaior =  nomes[posicaoMaior]
#dizer quantas mulheres são no total


#imprimir tudo
print("a média de idade do grupo é de: {}".format(media))
print("O homem mais velho tem {} anos e se chama: {}".format(maior, nomeMaior))
print("Ao todo são {} mulheres com menos de 20 anos".format(menos20))
