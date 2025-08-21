# {/* <p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
# <p>Find the sum of all the primes below two million.</p> */}
##エラトネスのふるい
## sieve of eratosthenes
def sieve_of_eratosthenes(n):
    a = [True] * (n +1)
    a[0] = a[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if a[i]:
            start = i * i
            step = i
            end = n + 1
            for j in range(start, end, step):
                a[j] = False
    return a

def is_circular_prime(n):
    num = str(n)
    for j in range(len(num)):
        if not is_prime[int(num)]:
            return False
        num = num[1:] + num[0]
    return True

def main():
    MAX = 1000000
    global is_prime
    is_prime = sieve_of_eratosthenes(MAX)
    count = 0
    result = []
    for i in range(2,MAX):
        if is_circular_prime(i):
            result.append(i)
            count += 1
    print(count)
    print(result)

main()


