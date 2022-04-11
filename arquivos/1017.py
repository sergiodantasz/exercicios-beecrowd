tempo = int(input())
velocidade_media = int(input())

distancia = velocidade_media * tempo
combustivel = distancia / 12

print(f'{combustivel:.3f}')
