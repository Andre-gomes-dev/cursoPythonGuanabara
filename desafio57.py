#entrada de uma string que seja apenas M ou F(usar upper)
sexo = ""
genero = ""
#condição e loop
valido =  False

sexo = input("Informe seu sexo [M/F]: ").upper().strip()

while valido == False:
    if sexo  != "M" and sexo != "F":
       sexo = input("dados invalidos, digite seu sexo: ").upper().strip()
    elif sexo  == "M" or sexo == "F":
        valido = True

#Jogando o genero na tela
if sexo == "M":
    genero = "Masculino"
elif sexo == "F":
    genero = "Feminino"   


print("sexo {} registrado com sucesso ".format(genero))               
