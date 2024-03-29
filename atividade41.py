com = float(input("Digite o valor do comprimento do terreno: "))
lar = float(input("Agora, o valor da largura do mesmo: "))
tela = float(input("Agora, o valor em reais do metro de tela: "))

dim = com*2 + lar*2
preco = tela * dim
print("O custo para cercar o terreno será:", preco, "reais")