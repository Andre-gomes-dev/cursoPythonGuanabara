precoProduto= float(input("qual é o preço do produto?: "))
desconto= (precoProduto * 5) / 100
precoOFF= precoProduto - desconto
print("O prodduto que custava R${}, na promoção com desconto de 5% vai custar: R${:.2f}".format(precoProduto, precoOFF))