valores = input()

valores_lista = valores.split(' ')

a = int(valores_lista[0])
b = int(valores_lista[1])
c = int(valores_lista[2])

maior = max(a, b, c)

print(f'{maior} eh o maior')
