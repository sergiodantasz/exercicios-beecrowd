n = int(input())

h = 0
m = 0
s = 0

while n > 0:
    if n >= 3600:
        h += 1
        n -= 3600
    elif n >= 60:
        m += 1
        n -= 60
    else:
        s += 1
        n -= 1

print(f'{h}:{m}:{s}')
