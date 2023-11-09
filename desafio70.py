escolha = ""
countProdutoAcima1000 = 0
precoProdutos = []
#looping
while True:
    print("-=-=-=-=-=-=--=-=-=-=--=-=-=-=-= - -=-=")
    print("      LOJA SUPER BARATÃO        ")
    print("-=-=-=-=-=-=--=-=-=-=--=-=-=-=-= - -=-=")

    


    produtoNome = input("Nome do Produto: ")
    produtoPreco = int(input("Preço: "))
    precoProdutos.append(produtoPreco)

    if produtoPreco >1000:
        countProdutoAcima1000 +=1

    escolha = input("Quer continuar [S/N]: ").upper().strip()

    if escolha == "S":
        print("continuando...\n")
        continue
    elif escolha == "N":
        break
    else:
        print("opçao invalida")


#prints
print("o total da compra foi: {}".format(sum(precoProdutos)))
print("Temos {} produto(s) custando mais de R$1000".format(countProdutoAcima1000))
print("o produto mais barato é: {}".format(min(precoProdutos)))
#total da compra
#produtos acima de 1000
# mais barato