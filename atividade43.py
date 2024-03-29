ham = 3.00
che = 2.50
fri = 2.50
ref = 1.00
mil = 3.00

print("Insira a quantidade de cada produto que você consumiu")

hamburger = int(input("Hambúrguer :"))
cheeseburger = int(input("Cheeseburguer :"))
fritas = int(input("Fritas :"))
refrigerante = int(input("Refrigerante :"))
milkshake = int(input("Milkshake :"))

h = hamburger * ham
c = cheeseburger * che
f = fritas * fri
r = refrigerante * ref
m = milkshake * mil

total = h+c+f+r+m
print(f"O valor total da conta será: ", "R${:,.2f}".format(total))