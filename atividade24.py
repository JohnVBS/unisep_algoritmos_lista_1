cat1 = float(input("Insira o valor do primeiro cateto: "))
cat2 = float(input("Insira o valor do segundo cateto: "))

import math
hip = math.sqrt(cat1 * cat1 + cat2 * cat2)
print(f"O valor da hipotenusa deste triângulo é: ", {hip})