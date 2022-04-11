n = int(input())

print(n)

qtd_100 = 0
qtd_50 = 0
qtd_20 = 0
qtd_10 = 0
qtd_5 = 0
qtd_2 = 0
qtd_1 = 0

while n > 0:
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
    else:
        qtd_1 += 1
        n -= 1

print(f'{qtd_100} nota(s) de R$ 100,00')
print(f'{qtd_50} nota(s) de R$ 50,00')
print(f'{qtd_20} nota(s) de R$ 20,00')
print(f'{qtd_10} nota(s) de R$ 10,00')
print(f'{qtd_5} nota(s) de R$ 5,00')
print(f'{qtd_2} nota(s) de R$ 2,00')
print(f'{qtd_1} nota(s) de R$ 1,00')
