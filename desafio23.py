numero = int(input("digite um numero"))
print("analisando o numero: {}".format(numero))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero //100 % 10
milhar = numero // 1000 % 10
print( unidade, dezena, centena, milhar)