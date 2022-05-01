dados = input().split()

a = float(dados[0])
b = float(dados[1])
c = float(dados[2])

perimetro = a + b + c
area = ((a + b) * c) / 2

if a + b > c and a + c > b and b + c > a:
    print(f'Perimetro = {perimetro:.1f}')
else:
    print(f'Area = {area:.1f}')
