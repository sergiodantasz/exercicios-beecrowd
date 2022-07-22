estados = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

ddd = int(input())

estado = estados.get(ddd)

print(estado if estado is not None else 'DDD nao cadastrado')
