um = int(input("Digite o valor que o primeiro amigo apostou: "))
dois = int(input("Digite o valor que o segundo amigo apostou: "))
tres = int(input("Digite o valor que o terceiro amigo apostou: "))
valor = int(input("Digite o valor do prêmio: "))

vtrês = um+dois+tres

p1 = (um * 100) / vtrês
p2 = (dois * 100) / vtrês
p3 = (tres * 100) / vtrês

t1 = (valor * p1) // 100
t2 = (valor * p2) // 100
t3 = (valor * p3) // 100

print(f'''
O primeriro amigo receberá: {t1} reais
O segundo amigo receberá: {t2} reais
O terceiro amigo receberá: {t3} reais
''')