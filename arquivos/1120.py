while True:
    entrada = input().split()

    digito_falha = entrada[0]
    numero = entrada[1]

    if digito_falha == '0' and numero == '0':
        break

    saida = numero.replace(digito_falha, '')
    if saida == '':
        saida = 0
    elif int(saida) == 0:
        saida = 0
    saida = int(saida)

    print(saida)
