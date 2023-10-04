carteira = float(input("quanto dinheiro voce tem na carteira?"))
dolarHoje = 5.04
valorConversao = carteira / dolarHoje
print("com {} você pode comprar U${:.2f}".format(carteira,valorConversao))