produto1 = input()
produto2 = input()

produto1_lista = produto1.split(' ')
valor1 = int(produto1_lista[1]) * float(produto1_lista[2])

produto2_lista = produto2.split(' ')
valor2 = int(produto2_lista[1]) * float(produto2_lista[2])

valor_total = valor1 + valor2

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')
