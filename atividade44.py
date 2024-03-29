car = 50
nome = str(input("Nome do vendedor: "))
carros = int(input("Número de carros vendidos: "))
valor = float(input("Valor total das vendas: "))
mes = int(input("Mês: "))
venda = (valor * 5) / 100
comissao = car * carros
mess = mes * 500

salario = mess + venda + comissao
print(f"O salário final do {nome} no tempo de {mes} meses é: ", "R${:,.2f}".format(salario))