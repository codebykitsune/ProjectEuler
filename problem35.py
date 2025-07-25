# {/* <p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
# <p>Find the sum of all the primes below two million.</p> */}
def summation_of_primes(n):
    a = [True] * (n +1)
    a[0] = a[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if a[i]:
            start = i * i
            step = i
            end = n + 1
            for j in range(start, end, step):
                a[j] = False
    r =[]
    for idx in range(len(a)):
        if a[idx]:
            r.append(idx)
    return r

rotation = set()

for k in range(10,100):
    k_str = str(k)
    num = [k[j:]+k[:j] for j in range(len(k_str))]
    rotation.add(num)

print(rotation)


