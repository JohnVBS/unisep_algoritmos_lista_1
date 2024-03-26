G1 = float(input("Insira o valor da primeira avaliação: "))
G2 = float(input("Insira o valor da segunda avaliação: "))

media = (G1 + (G2 * 2)) / 3

if media >= 7:
    {
        print(f"Parabéns, você passou! Sua média é: ", {media})
    }
else:
    {
        print(f"Que pena, você não passou! Sua média é: ", {media})
    }