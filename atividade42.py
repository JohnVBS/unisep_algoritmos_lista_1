fab = float(input("Insira o custo de fábrica: "))
dis = (fab * 12) / 100
imp = (fab * 45) / 100
dis2 = fab - dis
imp2 = fab - imp

total = fab + dis2 + imp2

print(f"O custo ao consumidor do carro será: ", total)