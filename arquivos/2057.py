entrada = input().split()

saida = int(entrada[0])
tempo = int(entrada[1])
fuso = int(entrada[2])

chegada = saida + tempo + fuso

if chegada >= 24:
    chegada = abs(24 - chegada)
elif chegada <= -1:
    chegada = abs(24 + chegada)

print(chegada)
