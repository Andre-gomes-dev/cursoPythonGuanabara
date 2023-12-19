
pessoas = {}
lista = []
quantidadePessoas = 0
acimadamedia= dict()
while True:
    nome =  input("Nome: ")
    while True:
        sexo =  input("Sexo: [M/F] ").upper().strip()
        if sexo == "M" or sexo == "F":
            idade = int(input("Idade: "))
            pessoas = {"nome":nome, "sexo": sexo, "idade": idade}
            break
        else:
            print("ERRO! Por favor, digite apenas M ou F")
       
    lista.append(pessoas)
    while True:
        resposta = input("Quer continuar? [S/N]: ").upper().strip()
        if resposta == "S" or resposta == "N":
            break  
        else:
            print()
            print("ERRO ! digite apenas S ou N\n")
            
    if resposta == "N":
        print("Encerrando..")
        break
    elif resposta == "S":
        print("continuando...")
       

       #somaquantidadePessoas
quantidadePessoas = len(lista)

#media
idades = [pessoa["idade"] for pessoa in lista]
mediaIdades = float(sum(idades) / len(idades))

# todas as mulheres cadastradas


mulheres = [pessoa["nome"] for pessoa in lista if pessoa["sexo"] == "F"]


# lista de pessoas acima da media    

acimadamedia =  [pessoa for pessoa in lista if pessoa["idade"] > mediaIdades]



#find nomes no dicionario

#prints
print(f"A) Ao todo temos {quantidadePessoas} pessoas cadastradas.") 
print(f"B) A média de idade é: {round(mediaIdades, 2)}")
print(f"C) As mulheres cadastradas foram: {mulheres}")
print(f"D) Lista das Pessoas que estão acima da media  {acimadamedia}")
