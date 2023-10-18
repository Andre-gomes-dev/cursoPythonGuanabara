dias = float(input("quantos dias alugados"))
kilometros  = float(input("quantos kilometros rodados"))

preco = (dias * 60)   + (0.15 * kilometros)
print("o valor a ser pago pelo aluguel é: R${}".format(preco))
