num = 1
den = 1

soma = 0

while num <= 39:
    soma += num / den
    num += 2
    den *= 2

print(f'{soma:.2f}')
