salario = float(input())

if salario <= 400:
    novo_salario = salario * 1.15
    p = 15
elif salario <= 800:
    novo_salario = salario * 1.12
    p = 12
elif salario <= 1200:
    novo_salario = salario * 1.10
    p = 10
elif salario <= 2000:
    novo_salario = salario * 1.07
    p = 7
else:
    novo_salario = salario * 1.04
    p = 4

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {novo_salario - salario:.2f}')
print(f'Em percentual: {p} %')
