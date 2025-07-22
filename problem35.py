def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i +=2 
    return True

list_test = []
for i in range(1,101):
    if is_prime(i):
        list_test.append(i)

def is_circular(n):
    if n < 10:
        return n
    n_str = str(n)
    for j in n_str:
        new_n = j
