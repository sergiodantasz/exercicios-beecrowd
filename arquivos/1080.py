numeros = []

for _ in range(100):
    numero = int(input())
    numeros.append(numero)

maior = max(numeros)
posicao = numeros.index(maior) + 1

print(maior)
print(posicao)
