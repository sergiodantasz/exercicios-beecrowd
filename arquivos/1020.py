idade_dias = int(input())

a = 0
m = 0
d = 0

while idade_dias > 0:
    if idade_dias >= 365:
        a += 1
        idade_dias -= 365
    elif idade_dias >= 30:
        m += 1
        idade_dias -= 30
    else:
        d += 1
        idade_dias -= 1

print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{d} dia(s)')
