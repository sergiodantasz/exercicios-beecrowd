caso = 1

while True:
    try:
        entrada = int(input())

        if entrada == 0:
            numeros = [0]
        else:
            numeros = []

            while True:
                sequencia = [entrada for _ in range(entrada)]
                for v in sequencia:
                    numeros.append(v)
                entrada -= 1
                if entrada == 0:
                    numeros.append(0)
                    numeros = numeros[::-1]
                    break

        qtd_numeros = len(numeros)
        if qtd_numeros > 1:
            print(f'Caso {caso}: {qtd_numeros} numeros')
        else:
            print(f'Caso {caso}: {qtd_numeros} numero')

        for i, numero in enumerate(numeros):
            if i == len(numeros) - 1:
                print(numero)
            else:
                print(numero, end=' ')
        print()

        caso += 1
    except EOFError:
        break
