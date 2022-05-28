valores = []

for _ in range(6):
    v = float(input())
    if v >= 1:
        valores.append(v)

qtd_positivos = len(valores)

print(f'{qtd_positivos} valores positivos')
