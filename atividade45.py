nome = str(input("Nome do aluno: "))
prova = float(input("Nota da prova: "))
qual = float(input("Nota qualitativa: "))

media = (prova * 2 + qual) // 3

print(f"A média de {nome} na disciplina de ED, será : ", media)