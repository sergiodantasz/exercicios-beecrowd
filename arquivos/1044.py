valores = input().split()

v1, v2 = [int(v) for v in valores]

if v1 % v2 == 0 or v2 % v1 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
