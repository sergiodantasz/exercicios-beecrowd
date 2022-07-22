horas = [int(h) for h in input().split()]

h_i, h_f = horas

duracao = h_f - h_i

if duracao <= 0:
    duracao += 24

print(f'O JOGO DUROU {duracao} HORA(S)')
