nome = input()
salario_fixo = float(input())
vendas = float(input())

bonus = vendas * 0.15

total = salario_fixo + bonus

print(f'TOTAL = R$ {total:.2f}')
