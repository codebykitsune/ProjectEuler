##ステップ
##素数判定の関数
##n² + a n + b この二次式の関数
##素数が連続で何回続くのかを調べる関数
##最後に|a| < 1000 かつ |b| ≤ 1000を回すメイン関数


##素数判定の関数　探索範囲をsqrt(n)に絞ると時間計算量がO(N**1/2)
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
        i +=2 ##偶数飛ばし
    return True

##Quadratic Primes
def quadratic_formula(a,b,n):
    return n ** 2 + a * n + b

##素数が連続で何回続くのかを調べる関数
def count_consecutive_primes(a,b):
    n = 0
    while True:
        ##なぜnotなのか
        if not is_prime(quadratic_formula(a,b,n)):
            return n
        n +=1

def main():
    TOP = 1000
    max_length = 0
    ##絶対値
    for a in range(-999, TOP):
        for b in range(-1000, TOP + 1):
            if count_consecutive_primes(a,b) > max_length:
                max_length = count_consecutive_primes(a,b)
                result = a * b
    print(result)

main()