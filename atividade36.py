num = int(input("Digite um número inteiro de 4 dígitos: "))
a = num//1000 % 10
b = num//100 % 10
c = num//10 % 10
d = num//1 % 10

print('', a,'\n', b,'\n', c,'\n', d)