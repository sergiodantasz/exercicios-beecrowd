n = int(input())

medias = []

for i in range(n):
    numeros = input().split()

    n1 = float(numeros[0])
    n2 = float(numeros[1])
    n3 = float(numeros[2])

    m = (n1 * 2 + n2 * 3 + n3 * 5) / 10

    medias.append(m)

for media in medias:
    print(round(media, 1))
