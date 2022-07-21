while True:
    try:
        tamanho = int(input())

        matriz0 = ''
        for i in range(tamanho):
            if i != tamanho - 1:
                matriz0 += '0' * tamanho + '\n'
            else:
                matriz0 += '0' * tamanho

        matriz2 = ''
        passo2 = 0
        for i, c in enumerate(matriz0):
            if i == passo2:
                matriz2 += '2'
                passo2 += tamanho + 2
            else:
                matriz2 += c

        matriz3 = ''
        passo3 = tamanho - 1
        for i, c in enumerate(matriz2):
            if i == passo3:
                matriz3 += '3'
                passo3 += tamanho
            else:
                matriz3 += c

        quadrado1 = int(tamanho / 3)

        i_inicio = quadrado1 * (tamanho + 2)
        i_final = i_inicio + tamanho - 2 * quadrado1 - 1

        final = tamanho ** 2 - tamanho * quadrado1 + int(tamanho / 3)

        matriz1 = ''
        for i, c in enumerate(matriz3):
            if i > final:
                matriz1 += c
            else:
                if i_inicio <= i <= i_final:
                    matriz1 += '1'
                else:
                    matriz1 += c
                if i == i_final:
                    i_inicio += tamanho + 1
                    i_final += tamanho + 1

        i4 = len(matriz1) // 2
        matriz4 = ''
        for i, c in enumerate(matriz1):
            if i == i4:
                matriz4 += '4'
            else:
                matriz4 += c

        print(matriz4)
        print()

    except EOFError:
        break
