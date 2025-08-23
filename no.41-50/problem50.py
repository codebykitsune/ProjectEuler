max_n = 1000000 #上限

def sieve(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes =[]
for i in range(max_n):
    if sieve(i):
        primes.append(i)
# print(primes)
primes_set = set(primes)

primes_sum = [0]
current_sum = 0
for k in primes:
    current_sum += k
    primes_sum.append(current_sum)

# print(primes_sum)
N = len(primes)
max_len = 0
result_prime = 0

for i in range(1, N + 1):
    for j in range(i):
        current_sum = primes_sum[i] - primes_sum[j]
        if current_sum >= max_n:
            break

        num_terms = i - j
        if num_terms > max_len and current_sum in primes_set:
            max_len = num_terms
            result_prime = current_sum

print(max_len)
print(result_prime)
