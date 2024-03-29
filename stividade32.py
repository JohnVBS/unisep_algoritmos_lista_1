valor = float(input("Valor total das compras: "))
dez = valor * 10/100
# desconto de 10%
desconto = valor - dez
# parcelamonto de 3x sem juros
parcela = valor / 3
# comissão à vista
com = desconto * 5/100
comissão = desconto + com
# comissão parcelada
com2 = valor * 5/100
comissao2 = valor + com2

print(f'''AQUI ESTÃO OS VALORES DAS FORMAS DE PAGAMENTO
[ 1 ] Valor com desconto de 10%: {desconto}
[ 2 ] Valor parcelado em 3x sem juros: {parcela}
[ 3 ] Valor da comissão à vista: {comissão}
[ 4 ] Valor de comissão parcelada: {comissao2}''')
