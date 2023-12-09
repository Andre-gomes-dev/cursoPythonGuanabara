lista = []
pessoas = []

while True:
    nome  = input("NOME: ")
    nota1 = float(input("NOTA1: "))
    nota2 = float(input("NOTA2: "))
    pessoas.append(nome)
    pessoas.append(nota1)
    pessoas.append(nota2)

    while True: 
        resposta =  input("quer continuar? [s/n]").lower().strip()
        if resposta == "s" or resposta ==  "n":
            break
        else:
            print("alternativa incorreta, tente novamente...")    



    if resposta == "s":
        print()
        print("continuando...")
        lista.append(pessoas[:])
        pessoas.clear()
    elif resposta == "n":
        print()
        print("saindo...")
        lista.append(pessoas[:])
        pessoas.clear
        break


#logica de print da lista

print("N° ","  Nome      ", " Média", end=" ")
print()
print("="*30) 



for posicao, elemento in  enumerate(lista):
   notas = lista[posicao][1], lista[posicao][2] 
   media =  sum(notas) /  len(notas)
   arredondaMedia =  round(media, 1) 
   print(f"{posicao}   {lista[posicao][0]}        {arredondaMedia:<4}") 


#LOGICA DE pedir notas de alunos
while True:
    posicao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if posicao == 999:
        print("encerrando")
        print("<<< VOLTE SEMPRE >>>")
        break
    else:
        print("="*30)
        print(f"notas de {lista[posicao][0]}  são [{lista[posicao][1]}, {lista[posicao][2]}]")
        print("="*30)
        

