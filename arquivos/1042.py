valores = input().split()

valores_inicio = [int(valor) for valor in valores]
valores_crescentes = sorted([int(valor) for valor in valores])

for v in valores_crescentes:
    print(v)

print()

for v in valores_inicio:
    print(v)
