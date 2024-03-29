h = int(input("Digite um valor inteiro em horas: "))
m = int(input("Digite um valor inteiro em minutos: "))
s = int(input("Digite um valor inteiro em segundos: "))
duracao = int(input("Agora, a duração da experiência em segundos: "))

hs = duracao // 3600
min = (duracao - (hs * 3600)) // 60
seg = duracao - (hs * 3600) - (min * 60)

hf = h + hs
mf = m + min
sf = s + seg

print("O horário do término da experiência será ", hf, "hs :", mf, "min :", sf, "seg")