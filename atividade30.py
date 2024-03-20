valor = float(input("Insira o valor da hora de trabalho em reais: "))
nh = float(input("Insira agora, o número de horas trabalhadas no mês: "))
bruto = valor * nh #4,272
acréscimo = bruto * 10 / 100 #427.2
total = bruto + acréscimo #4,699.2
print(f"O valor total do salário do funcionário mais 10% de acréscimo será: ", total, "reais")