def serch_number(d_n):
    x = ""
    for i in range(1, 1000000):
        x += str(i)
    return x[d_n-1]

def main():
    result = 1
    i = 1
    while i < 1000001:
        num = int(serch_number(i))
        result *= num
        i *= 10
    return result
print(main())