salario = float(input("Insira o valor da hora do salário em reais: "))
por = salario * 5 / 100

des = salario * 7 / 100
total = salario + por - des

print(f"O salário do funcionário será: ", total, "reais")