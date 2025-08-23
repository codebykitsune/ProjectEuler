def factorize(n): 
    list_of_primes = {}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            c = 0
            while n % i == 0:
                c += 1
                n //= i
            list_of_primes[i] = c
    if n != 1:
        list_of_primes[n] = 1

    return list_of_primes

n = 1000000
c = 4
for i in range(2,n):
    flag = True
    for j in range(c):
        length = len(factorize(i+j))
        if length != c:
            flag = False
    if flag == True:
        print(i)
        break
