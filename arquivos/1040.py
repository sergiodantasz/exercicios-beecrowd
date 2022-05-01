notas = input().split()

n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')

    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')

    media_final = (media + nota_exame) / 2
    if media_final >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')
