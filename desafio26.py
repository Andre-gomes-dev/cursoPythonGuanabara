recebe = input("Digite uma Frase: ")
frase = recebe.lower()
#regras de negocio
contagem = frase.count("a")
primeiroValor = frase.find("a")
ultimoValor = frase.rfind("a")

#prints
print(contagem)
print(primeiroValor)
print(ultimoValor)




