valores = input()

valores = valores.split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

try:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print('Impossivel calcular')
    else:
        den = 2 * a

        num_x1 = -b + delta ** 0.5
        num_x2 = -b - delta ** 0.5

        x1 = num_x1 / den
        x2 = num_x2 / den

        print(f'R1 = {x1:.5f}')
        print(f'R2 = {x2:.5f}')
except ZeroDivisionError:
    print('Impossivel calcular')
