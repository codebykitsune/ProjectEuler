import math

def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5 + 1), 2):
            if n % i == 0:
                return False
        return True

number = 3
primes = [2]
f = True
while f:
    if is_prime(number):
        primes.append(number)
    else:
        for p in primes:
            val = (number - p) / 2
            # valが正の整数で、かつ平方数であるかチェック
            if val > 0 and val == int(val):
                sqrt_val = math.sqrt(val)
                if sqrt_val == int(sqrt_val):
                    # 条件を満たす組み合わせが見つかったので、このnumberのチェックは終了
                    # 次の奇数 (number += 2) へ進む
                    break
        else:
            # forループがbreakされずに最後まで実行された場合
            # = どの素数pを使っても条件を満たさなかった
            print(number)
            # 目的の数値が見つかったので、whileループを終了する
            break
    number += 2