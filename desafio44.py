print("==============lojas Andre==============")
precoCompras = float(input("preço das compras: "))


print("Formas de pagamento: ")
print("[1] á vista dinheiro/cheque")
print("[2] á vista cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")

opcao = int(input("qual é a opção? "))

if opcao == 1:
    porcentagem = (precoCompras * 10) / 100
    desconto =  precoCompras - porcentagem 
    print("como voce comprou a vista irá obter 10%. de desconto e o valor ficou: {}".format(desconto))
if opcao == 2:
    porcentagem = (precoCompras * 5) /100
    desconto = precoCompras - porcentagem
    print("como voce comprou a vista irá obter 10%. de desconto e o valor ficou: {}".format(desconto))
if opcao == 3:
    parcelamento = precoCompras / 2
    print("como voce escolheu parcelar a sua compra em 2x vezes, a parcela mensal ficou: {}".format(parcelamento))
if opcao == 4:
    print("[0] para 3x parcelas")
    print("[1] para mais parcelas") 
    parcelas= input("quantas parcelas? ")
    porcentagem = (precoCompras *20) / 100
    acrescimo = precoCompras + porcentagem
    print("como você escolheu pagar 3x no cartão, as parcelas terão 20%. de acrescimo, logo a mensalidade ficou: ".format(acrescimo))
 
