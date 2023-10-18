import  random
alunos = []
i = 1
while i  <= 4:

    alunos.append(input("{}° aluno,: ".format(i)))
    i += 1
print("o aluno escolhido foi: {}".format(random.choice(alunos)))
