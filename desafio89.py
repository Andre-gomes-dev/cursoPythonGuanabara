
#lista dentro da ouutra
#tirar a media
#imprimir no fim a media dos alunos
#loop para perguntar as medias especificas de cada aluno, e 999 para sair do loop



lista = [[]]
pessoa = []
while True: 
    nome  = input("Nome: ")
    nota1 = input("Nota1: ")
    nota2 = input("Nota2: ")
    pessoa.append(nome)
    pessoa.append(nota1)
    pessoa.append(nota2)


    while True:
        resposta = input("quer continuar? [s/n] ").lower().strip()
        if resposta == "s" or resposta == "n":
            break
        else:
            print("opção errada, tente novamente...")    
    if resposta  == "n":
        print("finalizando programa: ")
        break
    if resposta == "s":
        print("continuando...\n")
lista = pessoa[:]
print(lista)