n = int(input())

quantia_total = 0

coelhos = 0
ratos = 0
sapos = 0

for _ in range(n):
    quantia_tipo = input().split()

    quantia = int(quantia_tipo[0])
    tipo = quantia_tipo[1]

    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

    quantia_total += quantia

percentual_coelhos = coelhos / quantia_total * 100
percentual_ratos = ratos / quantia_total * 100
percentual_sapos = sapos / quantia_total * 100

print(f'Total: {quantia_total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')
