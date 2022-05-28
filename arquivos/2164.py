def fibonacci(n):
    f = ((((1 + 5 ** (1 / 2)) / 2) ** n) - (((1 - 5 ** (1 / 2)) / 2) ** n)) / (5 ** (1 / 2))
    return f


print(f'{fibonacci(int(input())):.1f}')
