def verificar_operacao(expressao):
    if '+' in expressao:
        return 'soma'
    elif '-' in expressao:
        return 'subtração'
    elif '*' in expressao:
        return 'multiplicação'
    else:
        return 'divisão'


def soma(expressao):
    fracao1 = str()
    fracao2 = str()

    for i, c in enumerate(expressao):
        if c == '+':
            fracao1 = expressao[:i - 1].replace(' ', '')
            fracao2 = expressao[i + 2:].replace(' ', '')
            break

    n1 = int()
    d1 = int()

    for i, c in enumerate(fracao1):
        if c == '/':
            n1 = int(fracao1[:i])
            d1 = int(fracao1[i + 1:])

    n2 = int()
    d2 = int()

    for i, c in enumerate(fracao2):
        if c == '/':
            n2 = int(fracao2[:i])
            d2 = int(fracao2[i + 1:])

    numerador_soma = (n1 * d2) + (n2 * d1)
    denominador_soma = d1 * d2

    resultado = f'{numerador_soma}/{denominador_soma}'

    return resultado


def subtracao(expressao):
    fracao1 = str()
    fracao2 = str()

    for i, c in enumerate(expressao):
        if c == '-':
            fracao1 = expressao[:i - 1].replace(' ', '')
            fracao2 = expressao[i + 2:].replace(' ', '')
            break

    n1 = int()
    d1 = int()

    for i, c in enumerate(fracao1):
        if c == '/':
            n1 = int(fracao1[:i])
            d1 = int(fracao1[i + 1:])

    n2 = int()
    d2 = int()

    for i, c in enumerate(fracao2):
        if c == '/':
            n2 = int(fracao2[:i])
            d2 = int(fracao2[i + 1:])

    numerador_subtracao = (n1 * d2) - (n2 * d1)
    denominador_subtracao = d1 * d2

    resultado = f'{numerador_subtracao}/{denominador_subtracao}'

    return resultado


def multiplicacao(expressao):
    fracao1 = str()
    fracao2 = str()

    for i, c in enumerate(expressao):
        if c == '*':
            fracao1 = expressao[:i - 1].replace(' ', '')
            fracao2 = expressao[i + 2:].replace(' ', '')
            break

    n1 = int()
    d1 = int()

    for i, c in enumerate(fracao1):
        if c == '/':
            n1 = int(fracao1[:i])
            d1 = int(fracao1[i + 1:])

    n2 = int()
    d2 = int()

    for i, c in enumerate(fracao2):
        if c == '/':
            n2 = int(fracao2[:i])
            d2 = int(fracao2[i + 1:])

    numerador_multiplicacao = n1 * n2
    denominador_multiplicacao = d1 * d2

    resultado = f'{numerador_multiplicacao}/{denominador_multiplicacao}'

    return resultado


def divisao(expressao):
    i_barras = []

    for i, c in enumerate(expressao):
        if c == '/':
            i_barras.append(i)

    i_barra = i_barras[1]

    fracao1 = expressao[:i_barra - 1].replace(' ', '')
    fracao2 = expressao[i_barra + 2:].replace(' ', '')

    n1 = int()
    d1 = int()

    for i, c in enumerate(fracao1):
        if c == '/':
            n1 = int(fracao1[:i])
            d1 = int(fracao1[i + 1:])

    n2 = int()
    d2 = int()

    for i, c in enumerate(fracao2):
        if c == '/':
            n2 = int(fracao2[:i])
            d2 = int(fracao2[i + 1:])

    numerador_divisao = n1 * d2
    denominador_divisao = n2 * d1

    resultado = f'{numerador_divisao}/{denominador_divisao}'

    return resultado


def mdc(numerador, denominador):
    while denominador != 0:
        resto = numerador % denominador
        numerador = denominador
        denominador = resto

    return numerador


def simplificar(expressao):
    numerador = int()
    denominador = int()

    for i, c in enumerate(expressao):
        if c == '/':
            numerador = int(expressao[:i])
            denominador = int(expressao[i + 1:])

    mdc_fracao = mdc(numerador, denominador)

    numerador //= mdc_fracao
    denominador //= mdc_fracao

    resultado = f'{numerador}/{denominador}'

    return resultado


n = int(input())

for _ in range(n):
    fracao = input()

    verificacao = verificar_operacao(fracao)

    if verificacao == 'soma':
        r = soma(fracao)
        s = simplificar(r)
        print(f'{r} = {s}')

    elif verificacao == 'subtração':
        r = subtracao(fracao)
        s = simplificar(r)
        print(f'{r} = {s}')

    elif verificacao == 'multiplicação':
        r = multiplicacao(fracao)
        s = simplificar(r)
        print(f'{r} = {s}')

    else:
        r = divisao(fracao)
        s = simplificar(r)
        print(f'{r} = {s}')
