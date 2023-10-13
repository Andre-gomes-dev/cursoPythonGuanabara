import math
alunos = [] 
i = 1

while i <= 4:
    print(i)
    alunos.append(input("{} o aluno: ".format(i)))
    i +=1 
    

alunos.sort()
print(alunos)