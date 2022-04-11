n = float(input())

qtd_100 = 0
qtd_50 = 0
qtd_20 = 0
qtd_10 = 0
qtd_5 = 0
qtd_2 = 0

qtd_1 = 0
qtd_050 = 0
qtd_025 = 0
qtd_010 = 0
qtd_005 = 0
qtd_001 = 0

while n >= 2:
    if n >= 100:
        qtd_100 += 1
        n -= 100
    elif n >= 50:
        qtd_50 += 1
        n -= 50
    elif n >= 20:
        qtd_20 += 1
        n -= 20
    elif n >= 10:
        qtd_10 += 1
        n -= 10
    elif n >= 5:
        qtd_5 += 1
        n -= 5
    elif n >= 2:
        qtd_2 += 1
        n -= 2

while n > 0:
    if n >= 1:
        qtd_1 += 1
        n -= 1
    elif n >= 0.50:
        qtd_050 += 1
        n -= 0.50
    elif n >= 0.25:
        qtd_025 += 1
        n -= 0.25
    elif n >= 0.10:
        qtd_010 += 1
        n -= 0.10
    elif n >= 0.05:
        qtd_005 += 1
        n -= 0.05
    elif n >= 0.01:
        qtd_001 += 1
        n -= 0.01
    else:
        n = round(n, 3)

print('NOTAS:')
print(f'{qtd_100} nota(s) de R$ 100.00')
print(f'{qtd_50} nota(s) de R$ 50.00')
print(f'{qtd_20} nota(s) de R$ 20.00')
print(f'{qtd_10} nota(s) de R$ 10.00')
print(f'{qtd_5} nota(s) de R$ 5.00')
print(f'{qtd_2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{qtd_1} moeda(s) de R$ 1.00')
print(f'{qtd_050} moeda(s) de R$ 0.50')
print(f'{qtd_025} moeda(s) de R$ 0.25')
print(f'{qtd_010} moeda(s) de R$ 0.10')
print(f'{qtd_005} moeda(s) de R$ 0.05')
print(f'{qtd_001} moeda(s) de R$ 0.01')
