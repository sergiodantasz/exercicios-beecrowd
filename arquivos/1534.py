while True:
    try:
        tamanho = int(input())

        string3 = ''
        for i in range(tamanho):
            if i != tamanho - 1:
                string3 += '3' * tamanho + '\n'
            else:
                string3 += '3' * tamanho

        string1 = ''
        passo1 = 0
        for i, c in enumerate(string3):
            if i == passo1:
                string1 += '1'
                passo1 += tamanho + 2
            else:
                string1 += c

        string2 = ''
        passo2 = tamanho - 1
        for i, c in enumerate(string1):
            if i == passo2:
                string2 += '2'
                passo2 += tamanho
            else:
                string2 += c

        print(string2)
    except EOFError:
        break
