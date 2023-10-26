#numero =  input("digite algum numero")
impar = []
i = 0
soma = 0
#primeiro achar o impar
while i <= 500:
        resultado = i /  3
        if i % 2 == 1 and  resultado.is_integer:   
                impar.append(i)
                soma = soma + i
        i+=1
print(len(impar)) 
print(soma)   