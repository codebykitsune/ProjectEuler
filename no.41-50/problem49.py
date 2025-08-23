#4桁の素数を見つける
#各数が他の数の順列になっているかどうかを確認
#https://taq.hatenadiary.jp/entry/2022/05/08/133000#Problem-47--Distinct-primes-factors-
import itertools

#素数判定
def sieve(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

#重複を許して組み合わせを得る
for i in itertools.combinations_with_replacement("0123456789", 4):

    numbers = []
    for j in itertools.permutations(i):
        if j[0] != "0":
            a = int("".join(j))

            if sieve(a) == True and a not in numbers:
                numbers.append(a)

    if len(numbers) >= 3:

        for j in numbers:
            for k in numbers:
                if j < k:
                    m = (j + k)//2
                    if m in numbers:
                        print(j, m,k)
