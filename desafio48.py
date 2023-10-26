#numero =  input("digite algum numero")
impar = []
i = 0
soma = 0
#primeiro achar o impar
while i <= 500:
        if i % 2 == 1:
            impar.append(i)
            soma = impar[i]
        i+=1
print(impar) 
print(soma)   