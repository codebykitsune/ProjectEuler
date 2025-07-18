def distinct_powers(a,b):
    return a ** b

def main(n):
    list_a = []
    for a in range(2,n+1):
        for b in range(2,n+1):
            num = distinct_powers(a,b)
            list_a.append(num)       
    list_a = set(list_a)
    print(len(list_a))

main(100)

