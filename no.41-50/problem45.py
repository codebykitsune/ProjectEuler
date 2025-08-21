def is_pentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

f = True
i = 144
while f:
    hexagonal_num = i * (2 * i -1)

    if is_pentagonal(hexagonal_num):
        print(hexagonal_num)
        break

    i += 1

