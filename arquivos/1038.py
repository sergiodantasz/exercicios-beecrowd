entrada = input().split()

codigo = int(entrada[0])
qtd = int(entrada[1])

produtos = {
    1: 4,
    2: 4.5,
    3: 5,
    4: 2,
    5: 1.5
}

total = produtos[codigo] * qtd

print(f'Total: R$ {total:.2f}')
