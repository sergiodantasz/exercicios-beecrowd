salario = float(input())

if salario > 2000:
    i1 = i2 = i3 = 0
    if salario > 4500:
        v1 = salario - 4500
        salario -= v1
        i1 = v1 * 0.28
    if salario > 3000:
        v2 = salario - 3000
        salario -= v2
        i2 = v2 * 0.18
    if salario > 2000:
        v3 = salario - 2000
        salario -= v3
        i3 = v3 * 0.08
    i_final = i1 + i2 + i3
    print(f'R$ {i_final:.2f}')
else:
    print('Isento')
