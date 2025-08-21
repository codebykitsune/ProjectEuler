def isPan(n):
    d = len(str(n))
    s = [i for i in str(n)]

    f = True
    for i in range(1, d+1):
        if s.count(str(i)) != 1:
            f = False
    return f

def sieve(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


pan_prime = []
for i in range(1234567, 7654321):
    if isPan(i) == True:
        if sieve(i) == True:
            pan_prime.append(i)
            
print(len(pan_prime))
print(max(pan_prime))