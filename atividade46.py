nome = str(input("Nome do aluno: "))
prova = float(input("Nota da primeira avaliação: "))

# 7 = (prova + x * 2) / 3
# prova1 + 2x = 21
# 2x = 21 - prova1
# x = (21 - prova1) / 2

seg = (21 - prova) / 2

# EXEMPLO: prova1 + (prova2 * 2) / 3 = 7
# 5 + (8*2) / 3 = 7
# Logo, se a prova1 = 5, então prova2 = 8

print(f"A nota que {nome} precisa tirar na segunda avaliação para passar é: ", seg)