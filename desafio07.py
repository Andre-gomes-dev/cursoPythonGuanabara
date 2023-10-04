nota01 = float(input("primeira nota do aluno"))
nota02 = float(input("segunda nota do aluno"))

media= (nota01  + nota02) / 2
print("A média entre{:.1f} e {:.1f} é igual a {:.1f}".format(nota01, nota02, media))
print(round(media))