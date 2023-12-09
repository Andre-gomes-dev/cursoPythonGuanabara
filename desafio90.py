
situacao = ["Aprovado", "Reprovado"]

nome = input("Nome: ")
media = float(input(f"Média de {nome}: "))
if media >= 7:
    del(situacao[1])
elif media <7:
    del(situacao[0])   

aprova = {"nome: ": nome, "media": media, "situacao": situacao}

for key, val in aprova.items():
    print(f"{key} é igual a {val}")

